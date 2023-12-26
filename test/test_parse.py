"""
Test cases for FileParser.py
"""
import pytest
from source.file_parse import FileParser


def test_parse():
    """
    This test case is used to test the parse function
    """
    parse = FileParser()
    urls = parse.parse_yaml('test/mock_data/test_1.yaml')
    assert urls == [('https://www.google.com/', 'GET', None, None), ('https://www.yahoo.com/', 'GET', None, None)]


def test_parse_empty_method():
    """
    This test case is used to test the parse function with an empty method
    """
    parse = FileParser()
    urls = parse.parse_yaml('test/mock_data/test_2.yaml')
    body = '{"foo": "bar"}'
    headers = {'content-type': 'application/json', 'user-agent': 'fetch-synthetic-monitor'}
    assert urls == [('https://fetch.com/', 'POST', body, headers), ("https://fetch.com/careers", "PUT", body, headers),
                    ("https://fetch.com/rewards", "GET", None, headers)]


def test_invalid_path():
    """
    This test case is used to test the parse function with an invalid path
    """
    parse = FileParser()
    with pytest.raises(SystemExit):  # Check if the SystemExit is raised
        parse.parse_yaml('test/mock_data/test_3.yaml')


def test_check_name_url():
    name = None
    url = None
    parse = FileParser()
    assert parse.check_name_url(name, url) == False

def test_check_len():
    urls = []
    parse = FileParser()
    assert parse.check_len(urls) == False
