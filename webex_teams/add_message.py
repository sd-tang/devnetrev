#! /usr/bin/env python
""" Send a new message to a room using Messages API """

import json
import requests
import pprint

PAT = "" #Personal Access Token from developer.webex.com
URL = "https://webexapis.cisco.com/v1/messages"
METHOD = "POST"
PAYLOAD = {
    "roomId": "", # List room to find ID
    "text": "Hi there, welcome to our room"
}
HEADERS = {
    "Authorization": "Basic {}".format(PAT),
    "Content-Type": "application/json"
}

RESPONSE = requests.request(METHOD, url=URL, data=json.dumps(PAYLOAD),\
     headers=HEADERS)

pprint.pprint(json.loads(RESPONSE.text))