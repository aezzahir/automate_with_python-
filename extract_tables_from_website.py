import pandas as pd
from io import StringIO
import requests

url = "https://dimo.com/military-aircraft-parts/f-16-falcon/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    # Wrap the HTML content in a StringIO object
    html_buffer = StringIO(html_content)
    spare_parts_table = pd.read_html(html_buffer)
    print(spare_parts_table)
else:
    print("Failed to retrieve the webpage")
