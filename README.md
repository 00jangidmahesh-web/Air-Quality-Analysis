#  Air Quality Analysis & Pollution Monitoring System

**Live Dashboard:** [Click here to view the live app](https://air-quality-analysis-7kcljdg69decax6icnj7zw.streamlit.app/)

##  Project Overview
This project is a data-driven interactive web dashboard built to analyze, monitor, and visualize air quality metrics across various states and locations. The system processes extensive environmental records to track pollutants like SO2, NO2, RSPM, and PM2.5, helping identify pollution trends, high-risk zones, and generating insights relevant to Environmental Impact Assessment (EIA) context.

## Key Features
- **Extensive Data Analysis:** Analyzed 1900+ environmental records containing various pollutants across multiple locations.
- **Robust Data Cleaning:** Handled messy real-world data by performing rigorous data cleaning, preprocessing, and missing value imputation. Fixed inconsistent data types and formatting issues.
- **Data Optimization (Parquet):** Converted the 60 MB raw CSV dataset into a highly compressed `.parquet` format, significantly reducing storage size and improving the dashboard's load time and performance on the cloud.
- **Interactive Visualizations:** Developed dynamic charts using Plotly to track city-wise pollution trends, area-type comparisons (Industrial vs. Residential), and pollutant distributions.
- **Real-Time Filtering:** Implemented Streamlit widgets allowing users to filter and view location-specific environmental metrics dynamically.

## Tech Stack
- **Language:** Python
- **Data Manipulation:** Pandas, NumPy, PyArrow
- **Data Visualization:** Plotly Express
- **Web Framework:** Streamlit
- **Data Storage:** Apache Parquet (Optimized for fast querying)

## How to Run Locally

If you want to run this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/Air-Quality-Dashboard.git](https://github.com/YOUR_GITHUB_USERNAME/Air-Quality-Dashboard.git)
   cd Air-Quality-Dashboard
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Future Scope
Integration with live AQI APIs for real-time data fetching.

Implementing Machine Learning models to predict future pollution levels based on historical data.

Adding geographic heatmaps for better spatial visualization of pollution density.
