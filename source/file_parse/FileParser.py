"""
This module is responsible for parsing the YAML file and returning a list of tuples
"""
import yaml
import sys


class FileParser:
    """
    This class contains the method parse_yaml which is used to parse the YAML file
    """

    def __init__(self):
        """
        This method is used to initialize the URLs list
        """
        self.urls = []

    def parse_yaml(self, path):
        """
        This method is used to parse the YAML file
        :param path: Path of the YAML file
        :return: List of tuples containing the URLs, methods and bodies
        """

        endpoints = self.read_file(path)  # Load the yaml file

        if endpoints is None:  # Checking if the given YAML file is empty
            print('Empty YAML file with no endpoints \n')
            self.exit_program()

        for endpoint in endpoints:  # Iterate through the endpoints
            # Check if the method is specified, if not, the default method is GET
            method = endpoint.get('method') if 'method' in endpoint else 'GET'
            body = None  # Initialize the body to None

            if method == 'POST' or method == "PUT":
                # If the method is POST or PUT, check if the body is specified
                body = endpoint.get('body') if 'body' in endpoint else None

            headers = endpoint.get('headers') if 'headers' in endpoint else None
            name = endpoint.get('name')
            url = endpoint.get('url')

            # Checking if name or url parameters are empty
            valid_url_name = self.check_name_url(name, url)

            if valid_url_name:
                self.urls.append((url, method, body, headers))  # Append the url, method and body

        if not self.check_len(self.urls):
            self.exit_program()

        return self.urls  # Return the list of tuples

    @staticmethod
    def exit_program():
        """
        This method is used to exit the program
        """
        print('Exiting the program \n')
        sys.exit(1)

    @staticmethod
    def check_name_url(name, url):
        """
        This method is used to check for name and url parameter of every endpoint in the YAML file.
        :param name: name of the endpoint
        :param url: url of the endpoint
        :return: True if name and url are valid, False if either of them are not given for an endpoint
        """
        if name is None and url is None:
            print('\n Name and URL missing for one or more endpoints in the given YAML file. \n')
            return False
        elif url is None:
            print('\n URL missing for ' + name + ' endpoint in the given YAML file. \n')
            return False
        elif name is None:
            print('\n Name missing for ' + url + ' endpoint in the given YAML file. \n')
            return False

        return True

    @staticmethod
    def check_len(urls):
        """
        This method is used to check for number of valid endpoints in the YAML file
        :param urls: List of tuples containing the valid endpoints
        :return: True if there is at least one valid endpoint, False if there are no valid endpoints
        """
        if len(urls) == 0:
            print('No valid endpoints given in the YAML file. \n')
            return False

        return True

    def read_file(self, path):
        """
        This method is used to read a file in the given path
        :param path: the path containing the file to be read
        :return: True if there is a file in the given path, False if there is no file in the given path
        """
        try:
            with open(path, 'r') as f:  # Open the yaml file
                endpoints = yaml.load(f, Loader = yaml.FullLoader)  # Load the yaml file
                return endpoints

        except FileNotFoundError:  # If the file is not found, exit the program
            print('File not found')
            self.exit_program()

        except yaml.YAMLError as e:  # If there is an error in the yaml file, exit the program
            print(e)
            self.exit_program()
