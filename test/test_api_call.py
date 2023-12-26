"""
This module contains the test cases for the api_call function
"""
import pytest
import requests
from source.api_call import ApiHandler
from test.mock_response import MockResponse

def mock_get(*args, **kwargs):
    """
    This function mocks the requests.get() function.
    """
    _ = args, kwargs
    return MockResponse()

def unsuccessful_mock_get(*args, **kwargs):
    """
    This function mocks the requests.get() function.
    """
    _ = args, kwargs
    resp = MockResponse()
    resp.ok = False
    return resp

def high_latency_mock_get(*args, **kwargs):
    """
    This function mocks the requests.get() function.
    """
    _ = args, kwargs
    resp = MockResponse()
    resp.elapsed_time = 0.55
    return resp

def test_api_call(monkeypatch):
    """
    This test case is used to test the api_call function
    """
    monkeypatch.setattr(requests,'get', mock_get)
    api_call = ApiHandler()
    status = api_call.api_call('https://www.fetch.com/', 'GET', None, None)
    assert status == 'UP'

def test_api_call_invalid_url(monkeypatch):
    """
    This test case is used to test the api_call function with an invalid url
    """
    monkeypatch.setattr(requests,'get', unsuccessful_mock_get)
    api_call = ApiHandler()
    status = api_call.api_call('https://www.google.com/invalid', 'GET', None, None)
    assert status == 'DOWN'

def test_api_call_high_latency(monkeypatch):
    """
    This test case is used to test the api_call function with high latency
    """
    monkeypatch.setattr(requests,'get', high_latency_mock_get)
    api_call = ApiHandler()
    status = api_call.api_call('https://www.google.com/', 'GET', None, None)
    assert status == 'DOWN'

def test_api_call_invalid_method():
    """
    This test case is used to test the api_call function with an invalid method
    """
    api_call = ApiHandler()
    with pytest.raises(SystemExit):
        api_call.api_call('https://www.google.com/', 'INVALID', None, None)