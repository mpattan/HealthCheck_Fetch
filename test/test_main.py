"""
This file contains the tests for the __main__.py file.
"""
import pytest
import source.__main__
from source.file_parse import FileParser
from source.api_call import ApiHandler

def test_send_request(monkeypatch):
    """
    This test case is used to test the send_requests function
    """
    parse = FileParser()
    urls = parse.parse_yaml('test/mock_data/test_1.yaml')

    def mock_send_request(urls): # Mock the send_request function
        raise KeyboardInterrupt("Simulated KeyboardInterrupt")

    # Monkeypatch the function to use the mock version
    monkeypatch.setattr("source.api_call.ApiHandler.send_requests", mock_send_request)

    with pytest.raises(KeyboardInterrupt): # Check if the KeyboardInterrupt is raised
        # Call the function
        source.api_call.ApiHandler.send_requests(urls)
