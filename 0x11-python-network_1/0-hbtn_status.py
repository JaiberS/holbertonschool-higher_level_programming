#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: " + str(type(html)))
        print("\t- content: " + str(html))
        print("\t- utf8 content: " + html.decode('utf-8'))
