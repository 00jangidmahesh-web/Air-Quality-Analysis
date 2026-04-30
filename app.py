import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Config Setup
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
st.title("🌍 Air Quality Analysis & Pollution Monitoring System")

# Data Loading & Cleaning Function
@st.cache_data 
def load_data():
    # Option 1: Agar file GitHub repo mein hi hai (Recommended for 1929 rows)
    file_path = "https://drive.google.com/file/d/1-S0nsOpV-ujkfdIIC74biEt3oYQEp4cN/view?usp=drive_link" 
    
    # Option 2: Agar Google Drive se lena hai, toh Drive ka 'Direct Download Link' yahan daalo
    # file_path = "https://drive.google.com/uc?id=TUMHARI_FILE_KA_ID"
    
    df = pd.read_csv(file_path)
    
    # --- Data Cleaning ---
    df.replace('NA', np.nan, inplace=True)
    pollutant_cols = ['so2', 'no2', 'rspm', 'spm', 'pm2_5']
    for col in pollutant_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    df.dropna(subset=['state', 'location'], inplace=True)
    return df

# Load data
df = load_data()

# --- Dashboard Layout ---
st.sidebar.header("Filter Data")
selected_state = st.sidebar.selectbox("Select State", sorted(df['state'].unique()))

filtered_df = df[df['state'] == selected_state]

# Key Metrics
st.subheader(f"Pollution Overview for {selected_state}")
col1, col2, col3 = st.columns(3)

avg_so2 = filtered_df['so2'].mean()
avg_no2 = filtered_df['no2'].mean()
avg_rspm = filtered_df['rspm'].mean()

col1.metric("Average SO2", f"{avg_so2:.2f}" if pd.notnull(avg_so2) else "N/A")
col2.metric("Average NO2", f"{avg_no2:.2f}" if pd.notnull(avg_no2) else "N/A")
col3.metric("Average RSPM", f"{avg_rspm:.2f}" if pd.notnull(avg_rspm) else "N/A")

st.markdown("---")

# Visualizations
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("SO2 vs NO2 Comparison by Location")
    loc_data = filtered_df.groupby('location')[['so2', 'no2']].mean().reset_index()
    fig1 = px.bar(loc_data, x='location', y=['so2', 'no2'], barmode='group')
    st.plotly_chart(fig1, use_container_width=True)

with col_chart2:
    st.subheader("Pollution Distribution by Area Type")
    if 'type' in filtered_df.columns:
        type_data = filtered_df.groupby('type')['no2'].mean().reset_index()
        fig2 = px.pie(type_data, names='type', values='no2', hole=0.4)
        st.plotly_chart(fig2, use_container_width=True)