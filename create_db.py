import pandas as pd
import sqlite3

# Read the CSV file
df = pd.read_csv('/home/vignesh/Documents/medcal-hunt-august-2024/app/telangana_results_cleaned_2024.csv')

# Create a new SQLite database
conn = sqlite3.connect('telangana_neet_candidates.db')

# Save DataFrame to the SQLite database
df.to_sql('neet_candidates', conn, if_exists='replace', index=False)

conn.close()
