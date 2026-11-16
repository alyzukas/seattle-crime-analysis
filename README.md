# Seattle Crime Analysis
---

## Project Overview
🔗 **Live Site**: https://gpskentzos.github.io/DATA5310-FinalProject/

This project uses data visualization to tell one story about crime from three angles: Seattle, comparable U.S. cities, and the world. We start with neighborhood-level crime patterns in Seattle, compare Seattle to U.S. cities that look like it demographically and economically, and then place both against global trends.

The Seattle data alone could show what is happening in Seattle. Adding the comparison cities and the global data shows whether Seattle's patterns are unusual or part of a broader trend.

All visualizations, code, and write-ups are published on the project's GitHub Pages site.

- **Objective**: 
  - Build a clear, data-driven narrative about crime trends from 2010–2024 at the city, national, and global levels
  - Apply principles of visual design and perception (encoding choice, color, annotation, layout) to make each chart readable and honest
  - Choose the 10 most compelling visualizations and justify every design decision in a formal report
  - Present the story in an 8–10 minute recorded team presentation
  
- **Domain**: Data Visualization / Public Safety / Urban Analytics
  
- **Key Techniques:**
  - Exploratory data analysis (EDA) in Python
  - Data cleaning, filtering, and merging across multiple sources
  - Peer-city selection using U.S. Census ACS demographic and economic characteristics
  - Time-series, geographic, and comparative visualizations
  - Design justification grounded in perception and visualization theory



---

## Project Structure

```
seattle-crime-analysis/
│
├── data/
│   ├── data_cts_corruption_and_economic_crime.xlsx    # Updated world data code for project
│   └── data_cts_intentional_homicide.xlsx             # Updated world data code for project
│   └── data_cts_violent_and_sexual_crime.xlsx         # Added UN Crime Data and Sample Crime notebook
│   └── worldbank_indicators_2000_2024.csv             # Additional data for analysis
│   └── us_crime_clean.csv                             # Cleaned National Level Crime Data for project
│   └── us_census_clean.csv                            # Cleaned 2014-2024 Census Data for U.S. Economics and Housing Characteristics  
│
├── code/
│   ├── Seattle.ipynb                           # Seattle Level Data Preparation + EDA (Jennifer)
│   └── international-crime-eda.ipynb.ipynb     # Global Level Data Preparation + EDA (Paul)
│   └── fetch_worldbank.py                      # Updated world data code for project (Paul)
│   ├── national-prep.ipynb                # National Level Data Preparaton (Alyssa)
│   ├── national-eda.ipynb                 # [Pending] National Level Data EDA (Alyssa)
│   
│  
│
├── figures/                         # Exported final visualizations (PNG / HTML)
│
├── docs/                           
│   ├── .nojekyll              # Updated world data code for project
│   └── Seattle.html           # Moved seattle.html to the docs directory.
│   └── world.html             # Updated scatterplots
│   └── index.html             # Updated scatterplots
│   └── d
│   └── d
│
├── reports/
│   ├── Final_Report.pdf             # Formal report with 10 visualizations and design justification
│   └── Presentation_Slides.pdf      # Slides for the 8–10 minute recorded presentation
│
├── README.md                        # Project overview, data sources, usage
└── .gitignore
```
---

## Data Sources

| Dataset | Source | Used For |
| --- | --- | --- |
| SPD Crime Data | [data.seattle.gov](https://data.seattle.gov/) | Seattle incident-level crime trands |
| Crime Index| [crimeindex.org ](https://crimeindex.org/)| U.S. city crime rates over time |
| American Community Survey (5-year)| [U.S. Census Bureau](https://www.census.gov/programs-surveys/acs)| City characteristics for peer-city comparison |
| United Nations Office on Drugs and Crime | [data.unodc.org](https://data.unodc.org/datareport) | Various International data sets from UN |

- **Time Range** : 2010-2024

---

## Key Insights
( to be finalized after analysis )

---

## Visualizations
( to be updated after final visualizations have been built )

| Number | Visualization | Questions it answers |
| --- | --- | --- |
| 1 | ...enter title | ... enter question |
| b | ...enter title | ... enter question |
| b | ...enter title | ... enter question |
| 10 | ...enter title | ... enter question |




---

## Tools & Technologies

- Python (pandas, NumPy, matplotlib, seaborn, plotly)
- Google Colab / Jupyter Notebook
- GitHub & GitHub Pages
- ... add other tools
  
---

## Assumptions & Limitations

- Crime data reflects reported incidents only; reporting rates differ by city, country, and offense type
- Offense categories and definitions vary across sources, so some categories were grouped or standardized for comparison
- Peer cities are chosen on a limited set of ACS characteristics; other factors (policing, policy) also affect crime
- ACS 5-year estimates are averages over a period, not single-year values
- ... add any gaps in global data

---

## Authors

- **Alyssa Zukas** — [alyzukas@seattleu.edu](mailto:alyzukas@seattleu.edu)
- **Paul Skentzos** - [pskentzos@seattleu.edu](mailto:pskentzos@seattleu.edu)
- **Jennifer Poling** - [jpoling1@seattleu.edu](mailto:jpoling1@seattleu.edu)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Seattle University – *DATA 5310: Data Visualization (Fall 2026)*  
- Seattle Police Department and the City of Seattle Open Data Portal
- U.S. Census Bureau
- Crime Index
- United Nations Office on Drugs and Crime
- Python open-source community for enabling reproducible scientific analysis  


