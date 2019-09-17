#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()
    str0 = "https://api.github.com"
    str1 = str0 + "/repos/" + sys.argv[2] + "/" + sys.argv[1] + "/commits"
    html = requests.get(str1).json()
    j = 0
    for i in html:
        print(i['sha'] + ': ' + i['commit']['author']['name'])
        j += 1
        if j == 10:
            break
