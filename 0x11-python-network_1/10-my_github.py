#!/usr/bin/python3
"""Takes my Github credentials (username and password)
and uses the Github API to display my Github id.
"""
import requests
import sys


url = "https://api.github.com/" + sys.argv[1]
password = "Bearer " + sys.argv[2]

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": password,
    "X-GitHub-Api-Version": "2022-11-28"
}
resp = requests.get(url, headers=headers)
print(resp)
print(resp.json().get("id"))
