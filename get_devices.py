#!/usr/bin/python3

import json
import requests
from get_token import get_token


def main():
    
    token = get_token()
    get_devices(token)


def get_devices(token):
    	
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/"

    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
    }

    response = requests.request("GET", url, headers=headers)

    data = json.dumps(response.json()["response"], indent=2)
    
    if response.ok:
        for device in response.json()["response"]:
            id = device["id"]
            ip =device["managementIpAddress"]
            print(f"ID: {id} IP: {ip}")
    else:
        print(f"Device collection failed with status code {response.status_code}")
        print(f"Failure body: {response.text}")



if __name__ == '__main__':
	main()