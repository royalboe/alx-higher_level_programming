#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
from sys import argv


def request_id():
    """ displays the value of the X-Request-Id variable """
    with urllib.request.urlopen(argv[1]) as response:
        the_page = response.info()
    print(the_page['X-Request-Id'])


if __name__ == "__main__":
    request_id()
