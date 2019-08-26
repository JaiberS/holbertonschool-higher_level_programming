#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))
