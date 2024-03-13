#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the value of the `X-Request-Id`
variable found in the header of the response.
"""
import requests
import sys


url = sys.argv[1]
resp = requests.get(url)
print(resp.headers.get('X-Request-Id'))
