#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


def json_api():
    """ sends a POST request to the passed URL with a letter as a parameter """
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        values = {'q': ""}
    else:
        values = {'q': argv[1]}
    r = requests.post(url, data=values)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    json_api()
