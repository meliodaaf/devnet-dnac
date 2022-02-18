#!/usr/bin/python3

from dnacentersdk import api
import time

def main():
    
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!"
    )

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

    add_data = dnac.devices.add_device(**new_device_dict)

    time.sleep(10)
    task = add_data["response"]["taskId"]
    task_data = dnac.task.get_task_by_id(task)

    if not task_data["response"]["isError"]:
        print("New device successfully added.")
    else:
        print(f"Async task error seen: {task_data['progress']}")