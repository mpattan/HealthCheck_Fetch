"""
This module is the entry point for the health checker application
"""
import argparse
from source.file_parse import FileParser
from source.api_call import ApiHandler


def main():
    """
    This method is the entry point for the health checker application
    """
    parsed_args = argparse.ArgumentParser(description=
                                          """
                                          Health Check - 
                                          Provides the availability percentage of
                                          the HTTP endpoints
                                          """,
                                          usage = "%(prog)s [options] path",
                                          epilog=
                                          """
                                          Example: %(prog)s input.yaml,
                                          %(prog)s /Users/{user}/Code/HealthCheck_Fetch/input2.yaml
                                          """)  # Initialize the parser
    parsed_args.add_argument("path", metavar="path", type=str,
                             help="Enter path to yaml file")  # Add the path argument
    args = parsed_args.parse_args()  # FileParser the arguments
    parse = FileParser()  # Initialize the FileParser class
    api_handler = ApiHandler()
    urls = parse.parse_yaml(args.path)  # FileParser the yaml file
    api_handler.send_requests(urls)  # Send the requests to the endpoints


if __name__ == '__main__':
    main()  # Call the main method
