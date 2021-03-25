#! /usr/bin/env python
""" Finesse - Initiate a dialog between two numbers """

import requests

URL = "https://hq-uccx.abc.inc:8082/finesse/api/User/Agent001/Dialogs"
METHOD = "POST"
PAYLOAD = (
    "<Dialog>" +
    "   <requestedAction>MAKE_CALL</requestedAction>" +
    "   <fromAddress>1001</fromAddress>" +
    "   <toAddress>1002</toAddress>" +
    "<Dialog>"
)
ENCODED = "bXl1c2VybmFtZTpteXBhc3N3b3Jk"
HEADERS = {
    "Authorization": "Basic {}".format(ENCODED),
    "Content-Type": "application/xml",
    "Cache-Control": "no-cache"
}

RESPONSE = requests.request(METHOD, url=URL, data=PAYLOAD, headers=HEADERS)
print(RESPONSE.text)
print(RESPONSE.status_code)