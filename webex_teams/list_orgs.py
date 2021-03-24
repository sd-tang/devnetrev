#! /usr/bin/env python
""" List all the organizations """

import json
import requests

PAT = "" # get Personal Access Token from developer.webex.com
URL = "https://webexapis.cisco.com/v1/organizations"
HEADERS = {
    "Authorization": "Bearer {}".format(PAT)
}

RESPONSE = requests.get(url=URL, headers=HEADERS)
print(RESPONSE.text)