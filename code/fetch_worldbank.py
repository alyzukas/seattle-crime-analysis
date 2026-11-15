"""Download the World Bank indicators used in international-crime-eda.ipynb.

Source: World Bank, World Development Indicators, public API (https://api.worldbank.org).

What it does
------------
For each indicator in INDICATORS it requests every country and aggregate for
START-END, and stacks the answers into one long CSV:

    data/worldbank_indicators_2000_2024.csv
    columns: iso3, country, year, indicator_code, indicator, value

One row = country (or World Bank aggregate) x year x indicator. Values are written
exactly as the World Bank returns them: nothing is filtered, filled or recalculated.
`indicator` is a short name we chose for each World Bank `indicator_code`.

Usage (from the repo root or from code/):

    python code/fetch_worldbank.py

The notebook only reads the CSV, so this script needs to be run again only to
refresh the data or to add an indicator. It uses the Python standard library only.
"""
import csv
import json
import time
import urllib.request
from pathlib import Path

START, END = 2000, 2024

# World Bank indicator code -> short column name used in the notebook
INDICATORS = {
    "NY.GDP.PCAP.PP.CD": "gdp_pc_ppp",          # GDP per capita, PPP (current international $)
    "SI.POV.GINI": "gini",                      # Gini index (income inequality)
    "SP.POP.TOTL": "population",                # total population
}

URL = "https://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page=20000&date={start}:{end}"
OUT = Path(__file__).resolve().parent.parent / "data" / f"worldbank_indicators_{START}_{END}.csv"


def fetch(code, tries=4, timeout=300):
    """Return the list of observations for one indicator (the API is slow at times, so retry)."""
    url = URL.format(code=code, start=START, end=END)
    for attempt in range(1, tries + 1):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as resp:
                payload = json.load(resp)
            if len(payload) < 2 or payload[1] is None:
                raise ValueError(f"World Bank API returned no data for {code}: {payload[0]}")
            meta, rows = payload
            if meta["pages"] != 1:
                raise ValueError(f"{code}: expected one page, got {meta['pages']}")
            return rows
        except ValueError:
            raise
        except Exception as err:  # network error or timeout
            if attempt == tries:
                raise
            print(f"  {code}: attempt {attempt} failed ({err}); retrying")
            time.sleep(5 * attempt)


def main():
    records = []
    for code, short in INDICATORS.items():
        rows = fetch(code)
        print(f"{code:20s} {short:20s} {len(rows):6d} rows")
        records += [(r["countryiso3code"], r["country"]["value"], int(r["date"]), code, short, r["value"]) for r in rows]
    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["iso3", "country", "year", "indicator_code", "indicator", "value"])
        w.writerows(records)
    print(f"wrote {len(records):,} rows to {OUT}")


if __name__ == "__main__":
    main()
