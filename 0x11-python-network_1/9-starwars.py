#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    html = requests.get('https://swapi.co/api/people/', params={'search': q})
    html = html.json()
    try:
        print("Number of results: " + str(html['count']))
        for i in html['results']:
            print(i['name'])
    except ValueError:
        print("Not a valid JSON")
