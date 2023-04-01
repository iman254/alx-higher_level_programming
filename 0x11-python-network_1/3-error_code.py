#!/usr/bin/python3
"""takes in url sends request to url and displays body (in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode(utf-8))

    except HTTPError as error:
        print(f"error code: {error.status}")
