import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# 1. Data Load Karo (apni file ka sahi naam yahan daalna)
print("Data load ho raha hai...")
df = pd.read_csv('data.csv')

# 2. Data Cleaning
# Tumhare data mein 'NA' text likha tha, usko actual Null values (NaN) mein convert karte hain
df.replace('NA', np.nan, inplace=True)

# Pollutants ko numbers (float) mein convert karna
pollutant_cols = ['so2', 'no2', 'rspm', 'spm', 'pm2_5']
for col in pollutant_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Date column ko theek karna
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Missing values ko handle karna (Ya toh drop karo, ya fill karo. Abhi ke liye aage badhte hain)
df.dropna(subset=['state', 'location'], inplace=True)

print("Data clean ho gaya! MySQL mein push kar rahe hain...")

# 3. MySQL se Connect Karo
# Format: mysql+pymysql://username:password@localhost/database_name
# 'YOUR_PASSWORD' ki jagah apna actual MySQL password daalna
db_connection_str = "mysql+pymysql://root:YOUR_PASSWORD@localhost/air_quality_db"
engine = create_engine(db_connection_str)

# 4. Clean Data ko MySQL Table mein save karna
# 'pollution_records' tumhari nayi table ka naam hoga MySQL mein
df.to_sql(name='pollution_records', con=engine, if_exists='replace', index=False)

print("Success! Data MySQL database mein save ho gaya hai.")