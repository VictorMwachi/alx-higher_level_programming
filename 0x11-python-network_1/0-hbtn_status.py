#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print(f"\t- type: -{html}")
    print(f"\t- content: {type(html)}")
    print(f'\t- utf8 content: {html.decode("utf-8", "replace")}')
