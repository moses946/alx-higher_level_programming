#!/usr/bin/python3
"""
Module that fetches a url
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    html = resp.read()
    resp_type = type(html)
    content = html.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(resp_type, html, content))
