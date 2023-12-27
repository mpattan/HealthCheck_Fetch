"""
This module contains the class ApiHandler which is used to make the API calls to a given endpoint
"""
import requests
import sys
from collections import defaultdict
import time


class ApiHandler:
    """
    This class contains the method api_call which is used to make the API calls
    """
    def __init__(self):
        pass

    @staticmethod
    def api_call(url, method, body, headers):
        """
        This method is used to make the API calls
        :param url: URL of the endpoint
        :param method: Method of the endpoint
        :param body: Body of the request
        :param headers: Headers for the endpoint
        :return: Status of the API
        """
        try:
            # Check if the method is supported
            if method == "GET":
                response = requests.get(url, headers = headers)
            elif method == "POST":
                response = requests.post(url, json = body, headers = headers)
            elif method == "PUT":
                response = requests.put(url, json = body, headers = headers)
            elif method == "DELETE":
                response = requests.delete(url)
            else:
                print("Method not supported")  # If the method is not supported, exit the program and display a message
                sys.exit(1)

            status = "UP"  # If the response is OK and the response time is less than 500ms, the status is UP
            if not response.ok or response.elapsed.total_seconds() * 1000 > 500:
                # If the response is not ok or the response time is more than 500ms, the status is DOWN
                status = "DOWN"
            return status  # Return the status

        except requests.exceptions.ConnectionError:  # If the connection is refused, return 404
            return 404

    def send_requests(self, urls):
        """
        This method is used to send the requests to the endpoints
        :param urls: List of tuples containing the urls, methods and bodies
        """
        up_count = defaultdict(int)  # Initialize the up_count dictionary
        total_calls = defaultdict(int)  # Initialize the total_calls dictionary
        try:
            # Run the health check every 15 seconds
            while True:
                for url, method, body, headers in urls:
                    domain = url.split("//")[1].split('/')[0]  # Get the domain of the API
                    status = self.api_call(url, method, body, headers)  # Get the status of the API
                    total_calls[domain] += 1  # Increment the total_calls

                    if status == "UP":
                        up_count[domain] += 1  # Increment the up_count if the status is UP

                for domain in up_count:  # Iterate through the domains
                    # Calculate the availability percentage
                    availability = (up_count[domain] / total_calls[domain]) * 100
                    # Print the availability percentage
                    print(f"{domain} has {availability:.0f}% availability percentage")
                time.sleep(15)

        except KeyboardInterrupt:  # If the user presses Ctrl+C, exit the program
            print("\nExiting health check")
