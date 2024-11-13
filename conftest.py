import pytest

# add a marker for integration tests to avoid warning messages from pytest
def pytest_configure(config):
    config.addinivalue_line("markers", "integration: mark a test as an integration test.")

# Add API key as a command-line option to be used in tests by running pystest test_file.py --api_key=<key>
def pytest_addoption(parser):
    parser.addoption(
        "--api_key", action="store", default=None, help="API key for WeatherData"
    )

@pytest.fixture
def api_key(request):
    return request.config.getoption("--api_key")