#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.error as error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            response.read().decode('utf-8')
    except error.HTTPError as error:
        print("Error code:", error.code)
