#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers.get("X-Request-Id"))
