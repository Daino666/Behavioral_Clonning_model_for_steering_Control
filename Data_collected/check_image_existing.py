import os
import pandas as pd

# === CONFIG ===
csv_file = "driving_log.csv"        # path to your CSV
folder_path = "IMG"   # path to the folder with files
name_column = "/home/daino/Desktop/Self-Driving-Car-with-AI/Data_collected/IMG/center_2025_02_15_13_16_16_633.jpg"          # column in the CSV that contains the names
output_file = "filtered.csv"  # output CSV after filtering

# Load CSV
df = pd.read_csv(csv_file)

# Check if each name exists in folder
existing_names = set(os.listdir(folder_path))  # all files/folders in directory

# Keep only rows where name exists
filtered_df = df[df[name_column].isin(existing_names)]

# Save result
filtered_df.to_csv(output_file, index=False)

print(f"Filtering complete! Saved to {output_file}")
