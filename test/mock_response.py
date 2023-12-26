"""
This module contains the MockResponse class for mocking requests.get() response
"""

class MockResponse:
    """
    MockResponse class for mocking requests.get() response
    """
    def __init__(self, elapsed_time=0.1):
        self.elapsed_time = elapsed_time
        self.ok = True
    
    @property
    def elapsed(self):
        """
        This function returns the elapsed time of the mock response
        """
        class Elapsed:
            def __init__(self, seconds):
                self._seconds = seconds

            def total_seconds(self):
                return self._seconds

        return Elapsed(self.elapsed_time)