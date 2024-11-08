import streamlit as st

def layout():
    """create the layout for the web application"""

    st.title("Delfinen - Termometer")
    st.write("Denna webbapplikation visar temperaturdata från Delfinens temperaturmätare (skoajar bara, vi hämtar data från OpenWeatherMap).")

    st.markdown("## Temperatur")
    st.write("Skriv in lattidud och longitud för att se temperaturen på vald plats.")

    lat = st.number_input("Latitude", value=59.3293)
    lon = st.number_input("Longitude", value=18.0686)

    # PROVIDE FUNCTION THAT WILL GET DATA FROM THE API FOR THE GIVEN LATITUDE AND LONGITUDE
    # AND RETURN THE TEMPERATURE

if __name__ == "__main__":
    layout()

