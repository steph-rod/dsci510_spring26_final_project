# DSCI 510 Final Project

This project analyzes drug-related activity and its relationship with crime across California counties. The goal is to identify geographic hotspots and evaluate whether areas with higher drug activity also experience higher crime levels.

## Data sources

- California OpenJustice Crime Dataset (CSV)
  - Provides county-level crime data (violent and property crimes)
- California OpenJustice Arrest Dataset (CSV)
  - Provides county-level drug-related arrest data
- openFDA API (JSON)
  - Provides drug enforcement reports with city-level information
- Raw datasets are not included in the repository due to size and submission guidelines
- The pipeline demonstrates data processing and visualization using API data. 

## Analysis

This project analyzes the relationship between drug activity and crime across California counties using data from multiple sources.

The analysis process included the following steps:

- Data preprocessing:
  - Data from OpenJustice (crime and arrests) and the openFDA API (drug reports) were cleaned, filtered to the year 2024, and aggregated at the county level. A total crime feature was created by combining violent and property crime counts.
- Feature engineering:
  - Key variables were defined to represent crime and drug activity, including total crime, drug-related arrests, and drug-related reports.
- Data integration:
  - Datasets from different sources (county-level and city-level) were aligned and merged to enable comparison across geographic regions.
- Exploratory data analysis (EDA):
  - Visualizations such as scatter plots, bar charts, and geographic maps were used to identify patterns and trends.
- Statistical analysis:
  - A correlation analysis was performed to quantify the relationship between total crime and drug-related arrests, resulting in a strong positive correlation (r ≈ 0.88).
- Geospatial analysis:
  - Geographic visualization (using ArcGIS) was used to identify hotspots of crime and drug activity across California counties.

## Summary of Results

The analysis identified crime and drug arrest hotspots across California counties. A strong positive correlation (~0.88) was found between total crime and drug-related arrests, indicating that counties with higher crime levels also tend to have higher drug-related arrests. This correlation indicates an association between variables but does not imply causation.

Supporting analysis using openFDA data showed drug-related reports in major cities such as Los Angeles and San Diego, which are located within high-crime counties. 

## Installation

- No API key is required for the openFDA API
- Required Python packages are listed in `requirements.txt`

Install dependencies with:
pip install -r requirements.txt

## How to run 

From the `src/` directory run:
python main.py

This script runs the pipeline to fetch API data, process it and generate visualizations 

Results will be saved in:
- `results/` folder → visualizations (PNG)

## AI Usage

Portions of this project were developed with the assistance of generative AI tools (ChatGPT). AI was used to support:

- Merging datasets and computing correlation
- Data visualization using matplotlib

All code was reviewed, tested, and adapted to align with course concepts and lecture materials.