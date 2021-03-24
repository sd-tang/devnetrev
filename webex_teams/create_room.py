#! /usr/bin/env python
""" Create a Webex Teams room using Rooms API """

import json
import requests
import pprint

PAT = "" # Personal Access Token from developer.webex.com
URL = "https://webexapis.cisco.com/v1/rooms"
METHOD = "POST"
PAYLOAD = {
    "title": "Room 1 Title for DEVASC Team"
}
HEADERS = {
    "Authorization": "Bearer {}".format(PAT)
    "Content-Type": "appplication/json"
}

RESPONSE = requests.request(METHOD, url=URL, \
    data=json.dumps(PAYLOAD), headers=HEADERS)

pprint.pprint(json.loads(RESPONSE.text))