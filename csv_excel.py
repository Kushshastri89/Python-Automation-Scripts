import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill
def convert_csv_to_excel(csv_file, excel_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False, engine='openpyxl')
        print(f"✅ Successfully converted '{csv_file}' to '{excel_file}'")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")

if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ").strip()
    excel_file = input("Enter the desired Excel filename (e.g., output.xlsx): ").strip()
    convert_csv_to_excel(csv_file, excel_file)
