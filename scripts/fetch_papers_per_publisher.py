import pandas as pd
import os

# Define file paths
file_path = r'C:\Users\alaar\OneDrive - uniroma1.it\Desktop\Sapienza\FP SLR\QueryResults\venuePapers_721\sum\687_exclude_non_english.xlsx'
output_path = r'C:\Temp\papers_per_publisher.csv'  # Using a simpler path to avoid permission issues

# Ensure the Excel file exists before proceeding
if not os.path.exists(file_path):
    print(f"Error: The file at {file_path} was not found.")
    exit()

# Read the Excel file with error handling
try:
    df = pd.read_excel(file_path, engine='openpyxl')
    print("File loaded successfully.")
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Display available columns for debugging
print("Available columns:", df.columns.tolist())

# Check if 'publisher' column exists in the dataset
if 'publisher' not in df.columns:
    print("Error: 'publisher' column not found in the dataset.")
    exit()

# Count the number of papers per publisher
publisher_counts = df['publisher'].value_counts()

# Display the results for verification
print("\nNumber of papers per publisher:")
print(publisher_counts)

# Debugging output before saving
print("\nAttempting to save the following data to file:")
print(publisher_counts)
print(f"Saving file to: {output_path}")

# Ensure the output directory exists
output_directory = os.path.dirname(output_path)
if not os.path.exists(output_directory):
    print(f"Error: The output directory {output_directory} does not exist. Creating it now...")
    os.makedirs(output_directory)

# Try saving to CSV with error handling and different methods
try:
    # Standard saving method
    publisher_counts.to_csv(output_path, index=True, header=['Count'])
    print(f"Results saved successfully to {output_path}")

    # Verify the file was saved correctly
    if os.path.exists(output_path):
        print(f"File was successfully saved at: {output_path}")
    else:
        print("Error: File was not saved despite no errors.")
except PermissionError:
    print(f"Error: Permission denied when trying to save to {output_path}. Ensure the file is closed.")
except Exception as e:
    print(f"Error saving file: {e}")

# Attempt writing a test file to verify permissions
test_file_path = os.path.join(output_directory, 'test_write.txt')
try:
    with open(test_file_path, 'w') as f:
        f.write("Test file writing successful.\n")
    print(f"Successfully wrote a test file to {test_file_path}")
    os.remove(test_file_path)  # Clean up after test
except Exception as e:
    print(f"Error writing test file: {e}")

# Alternative saving method using to_string if issues persist
try:
    with open(output_path.replace('.csv', '_alternative.txt'), 'w') as f:
        publisher_counts.to_string(f)
    print(f"Alternative results saved to {output_path.replace('.csv', '_alternative.txt')}")
except Exception as e:
    print(f"Alternative saving method failed: {e}")
