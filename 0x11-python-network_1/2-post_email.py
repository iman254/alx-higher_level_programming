#!/usr/bin/python3
"""script that takes in an email and a url and
sends a post request to the passed url with the email
 as parameter and displays body in decoded utf-8
"""

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    header = parse.urlencode(email).encode()
    with request.urlopen(request.Request(url, header)) as response:
        print(response.read().decode("utf-8"))
