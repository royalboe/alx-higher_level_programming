#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests


def fetch_r():
    """ fetches https://alx-intranet.hbtn.io/status """
    req = requests.get('https://alx-intranet.hbtn.io/status')
    s = "Body response:\n\t- type: {}\n\t- content: {}"
    print(s.format(type(req.text), req.text))


if __name__ == "__main__":
    fetch_r()
