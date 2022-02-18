#!/usr/bin/python3

from dnacentersdk import api
import json

def main():
    
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!"
    )

    devices = dnac.devices.get_device_list()
    # print(json.dumps(devices, indent=2))

    for device in devices["response"]:
        device_id = device["id"]
        device_ip = device["managementIpAddress"]
        print(f"ID: {device_id} IP: {device_ip}")


if __name__ == '__main__':
	main()