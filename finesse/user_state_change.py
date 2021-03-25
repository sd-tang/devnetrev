#! /usr/bin/env python
""" Finesse user state change with Finesse User API """

import requests

URL = "https://hq-uccx.abc.inc:8082/finesse/api/User/Agent001"
METHOD = "PUT"
PAYLOAD = (
    "<User>" +
    "   <state>READY</state>" +
    "</User>"
)
ENCODED = "bXl1c2VybmFtZTpteXBhc3N3b3Jk"
HEADERS = {
    "Authorization": "Basic {}".format(ENCODED),
    "Content-Type": "application/xml"
}

RESPONSE = requests.request(METHOD, url=URL, data=PAYLOAD, headers=HEADERS)
print(RESPONSE.text)
print(RESPONSE.status_code)