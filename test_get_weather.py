# test_weather_data.py
import unittest
from unittest.mock import patch, Mock
from get_weather import WeatherData
from datetime import timedelta, datetime as dt
from random import uniform

class TestWeatherData(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.lat = 40.7128
        self.lon = -74.0060
        self.api_key = 'fake_api_key'
        self.get_weather = WeatherData(self.lat, self.lon, self.api_key)

    @patch('get_weather.requests.get')
    def test_get_current_temp_success(self, mock_get):
        # Mock response for a successful request
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current': {'temp': 20}
        }
        mock_get.return_value = mock_response

        # Assert that the temperature returned is correct
        self.assertEqual(self.get_weather.get_current_temp(), 20)

    @patch('get_weather.requests.get')
    def test_get_current_temp_failure(self, mock_get):
        # Mock response for a failed request
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Assert that None is returned when request fails
        self.assertIsNone(self.get_weather.get_current_temp())

    @patch('get_weather.requests.get')
    def test_get_temp_next_24h_success(self, mock_get):
        # Mock response for a successful request
        mock_response = Mock()
        mock_response.status_code = 200
        timestamp_this_hour = dt.now().replace(minute=0, second=0, microsecond=0).timestamp()
        mock_response.json.return_value ={'hourly': [{'dt': timestamp_this_hour + 3600*i, 'temp': 10+uniform(-7.2, 8.9)} for i in range(25)]}
        mock_get.return_value = mock_response

        # Check if the method returns a list with expected time and temperature values
        next_24h = self.get_weather.get_temp_next_24h()
        self.assertIsInstance(next_24h, list)
        self.assertEqual(len(next_24h), 24)
        self.assertIsInstance(next_24h[0][0], dt)
        self.assertEqual(next_24h[0][0], next_24h[1][0] - timedelta(hours=1))
        self.assertIsInstance(next_24h[0][1], float)
        self.assertGreaterEqual(next_24h[0][1], -100) # Assuming temperature is in Celsius and over -100
        self.assertLessEqual(next_24h[0][1], 80) # Assuming temperature is in Celsius and below 80

    @patch('get_weather.requests.get')
    def test_get_temp_next_24h_failure(self, mock_get):
        # Mock response for a failed request
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Assert that None is returned when request fails
        self.assertIsNone(self.get_weather.get_temp_next_24h())

if __name__ == '__main__':
    unittest.main()