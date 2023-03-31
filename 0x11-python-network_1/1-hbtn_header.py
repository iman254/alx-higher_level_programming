#!/usr/bin/python3
"""a script that takes in a url and displays the value of x-request-id variable found in header response"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as file:
        print(dict(response.headers).get("X-request-Id")) 
