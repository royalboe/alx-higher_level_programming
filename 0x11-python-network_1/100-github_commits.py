#!/usr/bin/python3
"""  script that lists 10 commits (from the most recent to oldest)
     of the repository
"""
import requests
from sys import argv


def my_githubrails():
    """list 10 commits (from the most recent to oldest) of the repository"""
    url = "https://api.github.com/repos/{}/{}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    username = argv[2]
    repo = argv[1]
    full_url = url.format(username, repo)
    req = requests.get(full_url)
    if req.status_code >= 400:
        print("None")
    else:
        for i in req.json()[:10]:
            print("{}: {}".format(i.get('sha'),
                                  i.get('commit').get('author').get('name')))


if __name__ == "__main__":
    my_githubrails()
