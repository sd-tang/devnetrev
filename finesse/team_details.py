#! /usr/bin/env python
""" Get Finesse Team Details """

import requests

URL = "https://hq-uccx.abc.inc:8445/finesse/api/Team/2"
METHOD = "GET"
ENCODED = "bXl1c2VybmFtZTpteXBhc3N3b3Jk"
HEADERS = {
    "Authorization": "Basic {}".format(ENCODED),
    "Cache-Control": "no-cache"
}

RESPONSE = requests.request(METHOD, url=URL, headers=HEADERS)
print(RESPONSE.text)