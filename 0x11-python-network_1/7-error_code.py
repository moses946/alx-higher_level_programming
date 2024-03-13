#!/usr/bin/python3
"""
Module that displays body of a url
"""
import sys
import requests


url = sys.argv[1]
resp = requests.get(url)
if resp.status_code >= 400:
    print(f"Error code: {resp.status_code}")
else:
    print(resp.text)
