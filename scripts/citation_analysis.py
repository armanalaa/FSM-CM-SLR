import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
source_file_path = r'../data/processed/R1_687.xlsx'
export_folder_path = r'../results/'

# Load the data
df = pd.read_excel(source_file_path, engine='openpyxl')

# Normalize the number of citations with a small constant to avoid division by zero
current_year = 2024
small_constant = 1
df["['bib']pub_year"] = pd.to_numeric(df["['bib']pub_year"], errors='coerce')  # Convert to numeric, coercing errors
df = df.dropna(subset=["['bib']pub_year"])  # Drop rows where publication year is NaN

df['normalized_citations'] = df['num_citations'] / (current_year - df["['bib']pub_year"] + small_constant)

# # Assuming df is your DataFrame and 'normalized_citations' is calculated as before
sorted_df = df.sort_values(by='normalized_citations', ascending=False)

# Calculate percentile values for normalized citations
P80_value = sorted_df['normalized_citations'].quantile(0.80)

# Filter rows for each percentile threshold
top_20_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P80_value)]

# Export the filtered data to separate Excel files with the number of rows in the filename
top_20_percent_df.to_excel(f'{export_folder_path}\\top_20_percent_{top_20_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')


print("Data exported successfully.")

# Plot the distribution of normalized citations
plt.figure(figsize=(10, 6))
plt.hist(sorted_df['normalized_citations'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)

# Add vertical lines for the 80th percentile values
plt.axvline(P80_value, color='r', linestyle='--', label='80th percentile')


# Add labels and title
plt.xlabel('Normalized Citations')
plt.ylabel('Paper Frequency')
plt.legend()

# Show the plot
plt.show()