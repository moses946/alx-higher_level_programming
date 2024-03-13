#!/usr/bin/python3
"""
Module that sends http request
"""
import requests


resp = requests.get('https://alx-intranet.hbtn.io/status')
print(f"Body response:\n\t- type: {type(resp.text)}\n\t- content: {resp.text}")
