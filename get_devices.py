import json
import requests
from get_token import data

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/"

headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': data
}

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)["response"]

for item in data:
	hostname = item["hostname"]
	mac = item["macAddress"]
	sn = item["serialNumber"]
	series = item["series"]
	role = item["role"]
	type = item["softwareType"]

	output = hostname, mac, sn, series, role, type

	print(output)