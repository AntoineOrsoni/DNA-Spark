"""
This script retrieves an authentication token from APIC-EM and prints out it's value
It is standalone, there is no dependency.
"""

import requests   # We use Python "requests" module to do HTTP GET query
import json       # Import JSON encoder and decode module

requests.packages.urllib3.disable_warnings() # Disable warnings

# APIC-EM IP, modify these parameters if you are using your own APIC-EM
apicem_ip = "devnetapi.cisco.com/sandbox/apic_em"
username = "devnetuser"
password = "Cisco123!"
version = "v1"
sparkToken = "ODVjODQ0ZDItZjI3ZC00ZTc5LWI2MTYtMzU3YWNhY2Y5ZDllMGUwMTIwODEtYTRj"
sparkRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vMTgyMDQxMDAtZTcwMS0xMWU3LTg4MjUtOTc2MWUwNDRiODJm"

# JSONhttps://sandboxapic.cisco.com/ input
r_json = {
    "username": username,
    "password": password
}

# POST ticket API URL
post_url = "https://"+apicem_ip+"/api/"+version+"/ticket"

# GET url
get_url = "https://"+apicem_ip+"/api/"+version+"/interface"

# All APIC-EM REST API request and response content type is JSON.
headers = {'content-type': 'application/json'}



# Make request and get response - "resp" is the response of this request
resp = requests.post(post_url, json.dumps(r_json), headers=headers,verify=False)
print ("Request Status: ",resp.status_code)

# Get the json-encoded content from response
response_json = resp.json()
print ("\nRaw response from POST ticket request:\n",resp.text)
# Not that easy to read the raw response, so try the formatted print out

# Pretty print the raw response
print ("\nPretty print response:\n",json.dumps(response_json,indent=4))

# ----------------------------------------
# Spark work
# ----------------------------------------


# serviceTicket = service ticket returned by the APIC
serviceTicket = response_json["response"]["serviceTicket"]


# ----------------------------------------
# Get device state
# ----------------------------------------

get_headers = {"x-auth-token": serviceTicket}

getDeviceInfo = requests.get(get_url, params=get_headers)

print("\n \n Device information : \n", json.dumps(getDeviceInfo.json(),indent=4))



# JSON : build the message

sparkMessage = str(serviceTicket) + " \n **desole sylvain pour le spam**"

spark_json = {
	"roomId" : sparkRoomID,
  	"text" : sparkMessage
}


# POST the message on the room
spark_post_url = "https://api.ciscospark.com/v1/messages"
spark_headers = {
	"Authorization" : "Bearer " + sparkToken,
	"Content-Type" : "application/json"
}

spark_resp = requests.post(spark_post_url, json.dumps(spark_json), headers=spark_headers, verify=False)
print("Spark status ", spark_resp.status_code)

spark_response_json = spark_resp.json()
print("\nPretty response from Spark : \n", json.dumps(spark_response_json,indent=4))