#!/usr/bin/python3

import time
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

    response = requests.post(url, headers=headers, json=new_device_dict)


    if response.ok:

        print(f"Request accepted: status code {response.status_code}")
        time.sleep(10)

        task = response.json()["response"]["taskId"]
        task_resp = requests.get(
            f"https://sandboxdnac.cisco.com/dna/intent/api/v1/task/{task}",
            headers=headers
        )

    else:
        print(f"Device addition failed with code {response.status_code}")
        print(f"Failure body: {response.text}")


if __name__ == '__main__':
	main()