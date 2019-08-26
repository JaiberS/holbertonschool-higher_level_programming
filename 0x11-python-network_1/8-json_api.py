#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys
import pdb


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    html = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if len(html.json()) == 0:
            print("No result")
            sys.exit()
        str0 = "[" + str(html.json()['id']) + "]"
        print(str0 + " " + html.json()['name'])
    except ValueError:
        print("Not a valid JSON")
