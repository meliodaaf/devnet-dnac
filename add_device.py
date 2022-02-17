#!/usr/bin/python3

import json
import requests
from get_token import get_token


def main():
    
    token = get_token()
    add_device(token)

def add_device(token):

    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/"

    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
    }

    new_device_dict = {
        "ipAddress": ["192.168.100.100"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "clarence",
        "password": "P@ssword",
        "computeDevice": "null",
        "enablePassword": "cisco123"
    }

    response = requests.get(url, headers=headers, json=new_device_dict)
    print(response.status_code)

if __name__ == '__main__':
	main()