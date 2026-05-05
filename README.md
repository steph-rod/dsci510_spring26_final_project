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

## Results

The analysis identified crime and drug arrest hotspots across California counties. A strong positive correlation (~0.88) was found between total crime and drug-related arrests, indicating that counties with higher crime levels also tend to have higher drug-related arrests. This correlation indicates an association between variables but does not imply causation.

Supporting analysis using openFDA data showed drug-related reports in major cities such as Los Angeles and San Diego, which are located within high-crime counties. 

## Installation

- No API key is required for the openFDA API
- Required Python packages are listed in `requirements.txt`

Install dependencies with:
pip install -r requirements.txt

## Running analysis

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