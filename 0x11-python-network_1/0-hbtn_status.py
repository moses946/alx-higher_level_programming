#!/usr/bin/python3
"""
Module that fetches a url
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    html = resp.read()
    resp_type = type(html)
    content = html.decode('utf-8')
    print(f"Body response:\n\t- type: {resp_type}\n\t- content: {html}\n\t- utf8 content: {content}")
    