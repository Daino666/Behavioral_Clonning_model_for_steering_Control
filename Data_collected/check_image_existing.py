import os
import pandas as pd

# === CONFIG ===
csv_file = "driving_log.csv"     # path to your CSV
folder_path = "IMG"              # path to the folder with images
output_file = "filtered.csv"     # output CSV after filtering

# Load CSV
df = pd.read_csv(csv_file)

# Get all filenames in folder
existing_names = set(os.listdir(folder_path))

# Function to check if row has at least one valid image
def row_has_match(row):
    for col in row[:3]:  # check first 3 columns (center, left, right)
        filename = os.path.basename(str(col))  # take only the file name (not full path)
        if filename in existing_names:
            return True
    return False

# Filter rows
filtered_df = df[df.apply(row_has_match, axis=1)]

# Save result
filtered_df.to_csv(output_file, index=False)

print(f"Filtering complete! Saved to {output_file}")

