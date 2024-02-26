#!/usr/bin/python3
"""
Module that sends http requests and handles errors.
"""
from urllib import request, error
import sys

url = sys.argv[1]

try:
    with request.urlopen(url) as resp:
        print(resp.read().decode('utf-8'))
except error.HTTPError as e:
    print(f"Error code: {e.code}")
