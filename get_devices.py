import requests
import json
from get_token import data

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/"

headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': data
}

response = requests.request("GET", url, headers=headers)

print(response.text)
