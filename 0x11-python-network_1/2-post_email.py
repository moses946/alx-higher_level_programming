#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""
from urllib import parse, request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = parse.urlencode({'email': email}).encode('ascii')

with request.urlopen(url, data) as resp:
    print(f"Your email is: {resp.read().decode('utf-8')}")
