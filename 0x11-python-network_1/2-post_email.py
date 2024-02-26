#!/usr/bin/python3
"""
Python script that sends a post request
"""
from urllib import parse, request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = parse.urlencode({'email': email}).encode('ascii')

with request.urlopen(url, data) as resp:
    print(f"Your email is: {resp.read().decode('utf-8')}")
