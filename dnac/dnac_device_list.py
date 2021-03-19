#! /usr/bin/env python
from dnacentersdk import api

# Initiate session object
myDNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!", \
    base_url="https://sandboxdnac.cisco.com")

# Initiate Devices object
myDevices = myDNAC.devices.get_device_list()

# Print
for device in myDevices.response:
    print({device.hostname})