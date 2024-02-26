#!/usr/bin/python3
"""
Module that displays Header info from http response.
"""
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as resp:
    headers = resp.headers
    print(headers.get('X-Request-Id'))