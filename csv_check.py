import pandas as pd
import os

# Assuming BASE_SYNTHEA_INPUT_DIRECTORY points to the directory containing the CSV files
BASE_SYNTHEA_INPUT_DIRECTORY = Your Generated Synthea Directory
encounters_file = csv file under the directory

# Construct the full path to encounters.csv
encounters_path = os.path.join(BASE_SYNTHEA_INPUT_DIRECTORY, encounters_file)

# Read the first few rows of encounters.csv
try:
    df_encounters = pd.read_csv(encounters_path)
    print(df_encounters.head())  # Print the first few rows
    print(df_encounters.info())  # Print column info and data types
except Exception as e:
    print(f"Error reading {encounters_file}: {e}")
