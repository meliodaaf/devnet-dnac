import requests
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

username = "devnetuser"
password = "Cisco123!"

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, auth=(username, password))

print(response.text)