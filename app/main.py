import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- Title
st.title("☀️ Solar Data Dashboard")

# --- Load Data
@st.cache_data
def load_data():
    benin = pd.read_csv('data/benin_clean.csv', parse_dates=['Timestamp'])
    sierraleone = pd.read_csv('data/sierraleone_clean.csv', parse_dates=['Timestamp'])
    togo = pd.read_csv('data/togo_clean.csv', parse_dates=['Timestamp'])

    benin['Country'] = 'Benin'
    sierraleone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    return pd.concat([benin, sierraleone, togo], ignore_index=True)

df = load_data()

# --- Sidebar: Country Selection
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

# --- Filtered Data
filtered_df = df[df['Country'].isin(selected_countries)]

# --- Select Metric Type
metric = st.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# --- Boxplot
st.subheader(f"📦 Boxplot of {metric} by Country")
fig, ax = plt.subplots()
sns.boxplot(x="Country", y=metric, data=filtered_df, ax=ax, palette="Set2")
st.pyplot(fig)

# --- Top Countries Table
st.subheader(f"🌍 Top Countries by Average {metric}")
top_countries = (
    filtered_df.groupby('Country')[metric]
    .mean()
    .reset_index()
    .sort_values(by=metric, ascending=False)
)
st.dataframe(top_countries)

# --- Bar Chart
st.subheader(f"📊 Average {metric} by Country")
fig2, ax2 = plt.subplots()
sns.barplot(x='Country', y=metric, data=top_countries, palette="pastel", ax=ax2)
ax2.set_ylabel(f"Average {metric}")
ax2.set_title(f"Average {metric} per Country")
st.pyplot(fig2)
