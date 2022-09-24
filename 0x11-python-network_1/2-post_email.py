#!/usr/bin/python3
"""  script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


def post_email():
    """sends a POST request to the passed URL with the email as a parameter"""
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
    print(the_page)


if __name__ == "__main__":
    post_email()
