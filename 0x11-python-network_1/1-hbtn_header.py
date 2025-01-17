#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers.get("X-Request-Id"))
