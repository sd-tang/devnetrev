#! /usr/bin/env python
from ucsmsdk.ucshandle import UcsHandle 

# Define handle's params; UCSM IP address, username, password
myHandle = UcsHandle("10.1.100.101", "devnetuser", "Cisco123!")

# Initiate connection
myHandle.login()

# Retrieve all the compute blades
myBlades = myHandle.query_classid("ComputeBlade")

# Table-formatted print
print("{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}".format(
    "Distinguished Name",
    "Serial",
    "Admin State",
    "Model",
    "Total Memory"
))
print("-"*70)

# Extract DN, serial number, admin state, model, total memory
# for each blade
for Blade in myBlades:
    print("{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}".format(
        Blade.dn,
        Blade.serial,
        Blade.admin_state,
        Blade.model,
        Blade.total_memory
    ))

# Remember to close the connection
myHandle.logout()