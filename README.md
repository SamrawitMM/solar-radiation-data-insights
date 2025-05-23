# solar-radiation-data-insights
Exploring solar radiation, weather conditions, and sensor performance data for analysis.

## 🎬 Streamlit App Demo

![Streamlit App Demo](dashboard/dashboard.gif)

---

## 📌 Project Goals

- Analyze solar irradiance components (GHI, DNI, DHI) across different regions.
- Examine environmental factors like temperature, wind, and humidity affecting solar potential.
- Identify seasonal and geographic patterns relevant to renewable energy deployment.
- Evaluate sensor data consistency and detect anomalies or outliers.
- Provide insights to support solar energy system planning and optimization.

## 📁 Project Structure

```plaintext
project-root/
├── .venv/                 # Python virtual environment 
├── data/                  # Raw and cleaned datasets 
├── notebooks/             # Jupyter notebooks for EDA and analysis
├── scripts/               # Standalone Python scripts (e.g., cleaning, processing)
├── src/                   # Source code for reusable modules and functions
├── tests/                 # Unit and integration tests
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md              # Project overview and setup instructions
└── .github/
    └── workflows/         # GitHub Actions CI/CD workflows
        └── ci.yml
```

The notebooks include descriptive statistics and correlation analysis of each location's wind and temperature parameters.

## 🧪 Features & Highlights

- 📊 **Jupyter Notebooks**:
  - Location-specific EDA (Benin, Sierra Leone, Togo)
  - Seasonal, diurnal, and annual trend visualizations
  - Correlation heatmaps between radiation and meteorological parameters

- ⚙️ **Data Processing Scripts**:
  - Cleaning of raw sensor data
  - Outlier detection and treatment

- 📉 **Visual Analysis**:
  - Boxplots, histograms, line charts, scatter plots, wind roses
  - 3D and multivariate plots for deeper insights

- 📈 **Comparative Insights**:
  - Regional solar potential comparisons
  - Suitability analysis for solar technology deployment (e.g., PV vs CSP)

## 📦 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SamrawitMM/solar-radiation-data-insights.git
   cd solar-radiation-data-insights
    ```
2. **Set up the virtual environment:
   ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
    ```
## ✅ Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn, plotly
- scikit-learn, scipy, jupyterlab
- Other dependencies listed in requirements.txt

## 📌 Usage

- Navigate to the notebooks/ folder for individual country analyses and also for comparison.
- Use scripts/ to preprocess raw data and reusable plot functions.
- Navigate to app to run the streamlit dashboard

## 📄 License
____________________________________________________________________________
This project is licensed under the MIT License. See LICENSE for more details.
_____________________________________________________________________________



