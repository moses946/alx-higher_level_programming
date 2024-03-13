#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
with `requests` module.
"""
import sys
import requests


url = sys.argv[1]
resp = requests.get(url)
if resp.status_code >= 400:
    print(f"Error code: {resp.status_code}")
else:
    print(resp.text)
