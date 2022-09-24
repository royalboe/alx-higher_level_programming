#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""
import requests
from sys import argv


def error_rcode():
    """ sends a request to the URL and displays the body of the response """
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(response.text)


if __name__ == "__main__":
    error_rcode()
