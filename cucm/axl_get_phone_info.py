""" Using CiscoAXL SDK to retrieve phone info """
from ciscoaxl import axl

URL = "10.1.50.1"
USER = "devnetuser"
PASSWORD = "cisco123"
VERSION = "12.0"

# initiate an object from the axl Class
myUCM = axl(username=USER, password=PASSWORD, cucm=URL, cucm_version=VERSION)
print(myUCM)

# use method get_phones
for phone in myUCM.get_phones():
    print(phone.name) # attribute "name"

# use method get_users
for user in myUCM.get_users():
    print(user.firstName) # attribute "firstName"