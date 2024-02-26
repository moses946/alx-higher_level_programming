#!/usr/bin/python3
"""
Module that prints header of a http response
"""
import requests
import sys


url = sys.argv[1]
resp = requests.get(url)
print(resp.headers.get('X-Request-Id'))
