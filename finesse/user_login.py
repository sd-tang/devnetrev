#! /usr/bin/env python
""" Finesse user login with Finesse User API 
Utilizes XML data type """

import requests
import base64

URL = "https://hq-uccx.abc.inc:8082/finesse/api/User/Agent001"
METHOD = "PUT"
PAYLOAD = (
    "<User>" +
    "   <state>Login</state>" +
    "   <extension>1001</extension>" +
    "</User>"
)
ENCODED = base64.b64encode("myusername:mypassword".encode("UTF-8"))
HEADERS = {
    "Authorization": "Basic {}".format(ENCODED),
    "Content-Type": "application/xml"
}

RESPONSE = requests.request(METHOD, url=URL, data=PAYLOAD, headers=HEADERS)
print(RESPONSE.text)
print(RESPONSE.status_code)