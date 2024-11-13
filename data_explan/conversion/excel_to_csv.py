import pandas as pd
import os

def excel_to_csv(excel_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the Excel file
    xls = pd.ExcelFile(excel_file)

    # Iterate through each sheet and save as CSV
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        csv_file_path = os.path.join(output_folder, f"{sheet_name}.csv")
        df.to_csv(csv_file_path, index=False)
        print(f"Converted '{sheet_name}' to '{csv_file_path}'")

if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()

    # Specify the Excel file name and output folder name
    excel_file_name = 'RTS_Data_Area.xlsx'  # Change this to your Excel file name
    output_folder_name = 'rts_data_zonal'  # Change this to your desired output folder name

    # Construct full paths
    excel_file_path = os.path.join(cwd, excel_file_name)
    output_folder_path = os.path.join(cwd, output_folder_name)

    excel_to_csv(excel_file_path, output_folder_path)