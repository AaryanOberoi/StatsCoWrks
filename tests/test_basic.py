import requests

app_url = 'http://127.0.0.1:5000'


def setup_function():
    print('Setup')


def teardown_function():
    print('Teardown')


def test_basic():
    requests.get(app_url)
