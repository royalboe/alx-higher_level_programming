#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


def fetch():
    """ fetches https://alx-intranet.hbtn.io/status """
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    s = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(s.format(type(the_page), the_page, the_page.decode('utf-8')))


if __name__ == "__main__":
    fetch()
