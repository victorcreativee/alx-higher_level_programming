#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the GitHub API to display your id
Usage: ./10-my_github.py
  - You must use Basic Authentication
"""

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    print(response.json().get('id'))
else:
    print(None)
