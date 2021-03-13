#! /usr/bin/env python
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Specify Cisco vManage IP, username, and password
vmanage_ip = "sandboxsdwan.cisco.com"
vmanage_port = "8443"
username = "devnetuser"
password = "Cisco123!"

# Construct base url string
base_url = "https://{}:{}/".format(vmanage_ip, vmanage_port)

# Login API resource and login credentials
login_action = "j_security_check"
login_data = {"j_username": username, "j_password": password}

# Combine base url and login action
login_url = base_url + login_action

# Establish a new session and connect it to Cisco vManage
mysession = requests.session()
login_response = mysession.post(url=login_url, data=login_data, verify=False)
print(login_response) # just to find out what the response is like

# Get the resource location from developer.cisco.com
networkdesign_resource = "/dataservice/networkdesign"

# Combine base url and resource location
networkdesign_url = base_url + networkdesign_resource

nd_response = mysession.get(url=networkdesign_url, verify=False)
nd_items = nd_response.content
print(nd_items)
# Not sure what is the expected output, need more research into this API call