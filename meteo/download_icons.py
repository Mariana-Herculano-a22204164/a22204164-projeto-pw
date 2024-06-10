import os
import requests
from zipfile import ZipFile

icons_url = 'https://api.ipma.pt/open-data/forecast/meteorology/icons_ipma_weather.zip'
icons_zip_path = 'weather-icons.zip'
icons_extract_path = 'static/meteo/'

print(os.curdir)
response = requests.get(icons_url)
with open(icons_zip_path, 'wb') as file:
    file.write(response.content)

with ZipFile(icons_zip_path, 'r') as zip_ref:
    zip_ref.extractall(icons_extract_path)

os.remove(icons_zip_path)
