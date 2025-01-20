import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
source_file_path = r'687_exclude_non_english.xlsx'
export_folder_path = r'./687_exclude_non_english'

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
P90_value = sorted_df['normalized_citations'].quantile(0.90)
P80_value = sorted_df['normalized_citations'].quantile(0.80)
P70_value = sorted_df['normalized_citations'].quantile(0.70)
P60_value = sorted_df['normalized_citations'].quantile(0.60)
P50_value = sorted_df['normalized_citations'].quantile(0.50)
P40_value = sorted_df['normalized_citations'].quantile(0.40)
P30_value = sorted_df['normalized_citations'].quantile(0.30)
P20_value = sorted_df['normalized_citations'].quantile(0.20)
P10_value = sorted_df['normalized_citations'].quantile(0.1)


# Filter rows for each percentile threshold
top_10_percent_df = sorted_df[sorted_df['normalized_citations'] >= P90_value]
top_20_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P80_value)]
top_30_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P70_value)]
top_40_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P60_value)]
top_50_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P50_value)]
top_60_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P40_value)]
top_70_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P30_value)]
top_80_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P20_value)]
top_90_percent_df = sorted_df[(sorted_df['normalized_citations'] >= P10_value)]


# Export the filtered data to separate Excel files with the number of rows in the filename
top_10_percent_df.to_excel(f'{export_folder_path}\\top_10_percent_papers_{top_10_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_20_percent_df.to_excel(f'{export_folder_path}\\top_20_percent_papers_{top_20_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_30_percent_df.to_excel(f'{export_folder_path}\\top_30_percent_papers_{top_30_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_40_percent_df.to_excel(f'{export_folder_path}\\top_40_percent_papers_{top_40_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_50_percent_df.to_excel(f'{export_folder_path}\\top_50_percent_papers_{top_50_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_60_percent_df.to_excel(f'{export_folder_path}\\top_60_percent_papers_{top_60_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_70_percent_df.to_excel(f'{export_folder_path}\\top_70_percent_papers_{top_70_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_80_percent_df.to_excel(f'{export_folder_path}\\top_80_percent_papers_{top_80_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')
top_90_percent_df.to_excel(f'{export_folder_path}\\top_90_percent_papers_{top_90_percent_df.shape[0]}_rows.xlsx', index=False, engine='openpyxl')


print("Data exported successfully.")

# Plot the distribution of normalized citations
plt.figure(figsize=(10, 6))
plt.hist(sorted_df['normalized_citations'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)

# Add vertical lines for the 90th, 80th, and 70th percentile values
# plt.axvline(P90_value, color='r', linestyle='--', label='90th percentile')
plt.axvline(P80_value, color='r', linestyle='--', label='80th percentile')
# plt.axvline(P70_value, color='b', linestyle='--', label='70th percentile')


# Add labels and title
plt.xlabel('Normalized Citations')
plt.ylabel('Paper Frequency')
# plt.title('Distribution of Normalized Citations with Percentile Thresholds')
plt.legend()

# Show the plot
plt.show()