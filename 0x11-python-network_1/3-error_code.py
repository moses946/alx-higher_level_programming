#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).

In addition, it handles HTTPError exceptions to print
the HTTP Status Code, if an error occurs.
"""
from urllib import request, error
import sys

url = sys.argv[1]

try:
    with request.urlopen(url) as resp:
        print(resp.read().decode('utf-8'))
except error.HTTPError as e:
    print(f"Error code: {e.code}")
