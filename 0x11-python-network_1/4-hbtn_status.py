#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""
import requests


resp = requests.get('https://alx-intranet.hbtn.io/status')
print(f"Body response:\n\t- type: {type(resp.text)}\n\t- content: {resp.text}")
