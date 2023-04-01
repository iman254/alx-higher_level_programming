#!/usr/bin/python3
"""script that takes in a url and requests to the url
and displays the value of x-request-id"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as file:
        header = file.getheader("X-Request-Id")
        print(header)
