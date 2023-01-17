#!/usr/bin/python3
"""
module contains Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(email).encode('ascii')
    request = urllib.request.Request(url,data)
    with urllib.request.urlopen(request) as response:
        print(response.read())
