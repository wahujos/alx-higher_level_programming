#!/usr/bin/python3
""" importing the relevant modules"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    auth = (username, token)
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            }
    res = requests.get('https://api.github.com/user',
                       auth=auth, headers=headers)
    if res.status_code == 200:
        user_data = res.json()
        if user_data.get('id') is None:
            print("None")
        else:
            print(f'{user_data[id]}')
    else:
        print(f"Error {res.status_code} {res.text}")
