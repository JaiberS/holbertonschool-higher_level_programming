#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    p = 1
    parms = {'search': q, 'page': p}
    html = requests.get('https://swapi.co/api/people/', params=parms).json()
    try:
        cont = html['count']
        print("Number of results: " + str(cont))
        for i in range(cont):
            for j in html['results']:
                print(j['name'])
                for k in j['films']:
                    films = requests.get(k).json()
                    print('\t' + films['title'])
            p += 1
            parms = {'search': q, 'page': p}
            link = 'https://swapi.co/api/people/'
            html = requests.get(link, params=parms).json()
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        sys.exit()
