import pandas as pd
import requests
from openpyxl import load_workbook

def get_publisher_by_title(paper_title):
    base_url = "https://api.crossref.org/works"
    query_params = {'query.title': paper_title, 'rows': 1}
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        items = data.get('message', {}).get('items', [])
        if items:
            return items[0].get('publisher', 'Publisher not found')
    except requests.RequestException:
        return "Error retrieving publisher"

def process_sheet(df):
    publishers = []
    for index, title in enumerate(df["['bib']title"], start=1):
        publisher = get_publisher_by_title(title)
        publishers.append(publisher)
        print(f"Processed {index}/{len(df)}: {publisher}")
    df['publisher'] = publishers
    return df

# Load the Excel file
file_path = '../data/raw/R_Tot_1137.xlsx'  # Replace with your actual file path

# Read all sheets into a dictionary of DataFrames
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

# Process each sheet
processed_sheets = {}
for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    processed_df = process_sheet(df)
    processed_sheets[sheet_name] = processed_df

# Save the processed DataFrames back to the Excel file, each sheet at a time
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    for sheet_name, df in processed_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("The Excel file has been updated with a 'publisher' column for all sheets.")
