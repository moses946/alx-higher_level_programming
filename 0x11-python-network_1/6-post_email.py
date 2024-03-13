#!/usr/bin/python3
"""
Script that sends a post request
"""
import sys
import requests


url = sys.argv[1]
data = {"email" : sys.argv[2]}

resp = requests.post(url, data=data)
print(f"Your email is: {resp.text}")
