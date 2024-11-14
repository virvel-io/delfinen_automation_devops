# test_integration_weather_data.py
# runt test by: pytest -rs test_integration_weather_data --api-key <key>

import pytest
from get_weather import WeatherData

lat = 59.3293
lon = 18.0686

# Test if the API key is invalid
def test_invalid_api_key(api_key):
    if not api_key:
        pytest.skip("API key not provided")

    get_weather = WeatherData(lat, lon, api_key)
    status_code = get_weather.get_status_code()  
    if status_code == 200:
        pytest.skip("API key is valid, skipping invalid API key test")
    else:
        assert status_code == 401, f"Expected 401, but got {status_code}"  

# Test if the API request is successful
@pytest.mark.integration
def test_request_success(api_key):
    if not api_key:
        pytest.skip("API key not provided")

    get_weather = WeatherData(lat, lon, api_key)
    status_code = get_weather.get_status_code()
    
    # Check for successful status code
    assert status_code == 200, f"Expected 200, but got {status_code}"

def test_weather_api_invalid_params(api_key):
    """Test the /weather endpoint with invalid parameters to check error handling."""
    if not api_key:
        pytest.skip("API key not provided")
    lat = 1000 # Invalid latitude
    lon = 1000 # Invalid longitude

    get_weather = WeatherData(lat, lon, api_key)
    status_code = get_weather.get_status_code()
   
    # Check for 400 Bad Request status code
    assert status_code == 400, f"Expected 400, but got {status_code}"
    

# Get current temperature from the API
@pytest.mark.integration
def test_get_current_temp_integration(api_key):
    if not api_key:
        pytest.skip("API key not provided")
 
    get_weather = WeatherData(lat, lon, api_key)
    current_temp = get_weather.get_current_temp()

    # Check that we get a valid float temperature (or None if the request fails)
    assert isinstance(current_temp, (float, type(None)))

@pytest.mark.integration
def test_get_temp_next_24h_integration(api_key):
    
    if not api_key:
        pytest.skip("API key not provided")

    get_weather = WeatherData(lat, lon, api_key)
    temp_24h = get_weather.get_temp_next_24h()

    # Check if the result is a list of temperature data (or None if the request fails)
    if temp_24h is not None:
        assert isinstance(temp_24h, list)
        assert len(temp_24h) <= 24
    else:
        assert temp_24h is None