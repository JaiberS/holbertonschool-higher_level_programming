#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()
    q = (sys.argv[1], sys.argv[2])
    html = requests.get('https://api.github.com/user', auth=q).json()
    if 'id' in html:
        try:
            print(str(html['id']))
        except ValueError:
            print("Not a valid JSON")
    else:
        print("None")
