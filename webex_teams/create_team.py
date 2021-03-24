#! /usr/bin/env python
""" Create Webex Teams team using Teams API """

import json
import requests

PAT = "" # Get Personal Access Token from developer.webex.com
URL = "https://webexapis.cisco.com/v1/teams"
METHOD = "POST"
PAYLOAD = {
    "name": "DEVASC Team"
}
HEADERS = {
    "Authorization": "Bearer {}".format(PAT),
    "Content-Type": "application/json"
}

RESPONSE = requests.request(METHOD, url=URL, \
    data=json.dumps(PAYLOAD), headers=HEADERS)
print(RESPONSE.text)