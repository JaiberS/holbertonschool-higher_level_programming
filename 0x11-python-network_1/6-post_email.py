#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    html = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(html.text)
