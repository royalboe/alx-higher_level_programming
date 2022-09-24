#!/usr/bin/python3
"""  script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import requests
from sys import argv


def my_github():
    """sends a POST request to the passed URL with a letter as a parameter"""
    url = "https://api.github.com/user"
    values = (argv[1], argv[2])
    req = requests.get(url, auth=values)
    if req.status_code >= 400:
        print("None")
    else:
        print(req.json().get('id'))


if __name__ == "__main__":
    my_github()
