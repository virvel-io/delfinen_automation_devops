import os
from dotenv import load_dotenv
import requests
import openpyxl
from datetime import datetime
import json
import streamlit as st

# Ladda in .env-filen
load_dotenv()

# Hämta API-nyckeln från .env-filen
api_key = os.getenv("API_KEY")

# Ange koordinater för platsen
latitude = 59.30996
longitude = 18.0215

# Ange URL för OpenWeatherMap:s API för platsprognos
api_url  = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,daily,alerts&appid={api_key}&units=metric"
# Gör API-anropet
response = requests.get(api_url)

# Kontrollera att begäran lyckades
if response.status_code == 200:
    # Tolka rådata som JSON
    data = json.loads(response.content)

    # Visualisera data med Streamlit
    st.title("Väderdata från OpenWeatherMap")
    st.json(data)
else:
    st.error(f'Error: {response.status_code}')