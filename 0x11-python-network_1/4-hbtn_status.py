#!/usr/bin/python3
"""fetches a url with the package request"""

if __name__ == "__main__":
    import urllib.requests

    response = urllib.requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
