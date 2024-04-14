import pandas as pd
from io import StringIO
import requests

url = "https://dimo.com/military-aircraft-parts/f-16-falcon/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print(html_content)
    # Wrap the HTML content in a StringIO object
    html_buffer = StringIO(html_content)
    spare_parts_tables = pd.read_html(html_buffer)
    
    # Create a Pandas Excel writer using 'xlsxwriter' as the engine
    excel_writer = pd.ExcelWriter('spare_parts.xlsx', engine='xlsxwriter')
    
    # Iterate through the list of DataFrames and save each to a separate sheet
    for idx, table in enumerate(spare_parts_tables):
        table.to_excel(excel_writer, sheet_name=f'Sheet{idx+1}', index=False)
    
    # Close the Pandas Excel writer to save the Excel file
    excel_writer._save()
    print("Excel file saved successfully.")
else:
    print("Failed to retrieve the webpage")
