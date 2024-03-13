#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the
letter as a parameter and with `requests` module.
"""
import sys
import requests

if sys.argv[1]:
    letter = sys.argv[1]
else:
    letter = ''
resp = requests.post("http://0.0.0.0:5000/search_user", data={'q':letter})
js = resp.json()

if js:
    if len(js) > 0:
        print(f"[{js.id}] {js.name}")
    else:
        print('No result')
else:
    print("Not a valid JSON")
