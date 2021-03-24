#! /usr/bin/env python
""" Add new member to a room using Memberships API """

import json
import requests
import pprint

PAT = "" # Personal Access Token from developer.webex.com
URL = "https://webexapis.cisco.com/v1/memberships"
METHOD = "POST"
PAYLOAD = {
    "roomId": "", # list room to find ID
    "personEmail": "chris@example.com",
    "personDisplayName": "Christopher Tang",
    "isModerator": "true"
}
HEADERS = {
    "Authorization": "Basic {}".format(PAT),
    "Content-Type": "application/json"
}

RESPONSE = requests.request(METHOD, url=URL, data=json.dumps(PAYLOAD),\
     headers=HEADERS)

pprint.pprint(json.loads(RESPONSE.text))