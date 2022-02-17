#!/usr/bin/python3

import requests
import json


def main():
	token = get_token()
	print(token)

def get_token():
	
	# Authentication URL to get the Token that will be used for API calls.
	url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

	# Basic authentication
	auth = ("devnetuser", "Cisco123!")
	headers = {'Content-Type': 'application/json'}

	response = requests.post(url, headers=headers, auth=auth)

	response.raise_for_status()
	Token = json.loads(response.text)["Token"]

	return Token

if __name__ == '__main__':
	main()
