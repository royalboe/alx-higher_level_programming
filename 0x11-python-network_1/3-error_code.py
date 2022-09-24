#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv


def error_code():
    """ sends a request to the URL and displays the body of the response """
    url = argv[1]
    try:
        with urlopen(url) as response:
            the_page = response.read()
        print(the_page.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    error_code()
