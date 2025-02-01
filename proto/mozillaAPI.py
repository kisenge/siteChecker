import requests
import time
import json

# Define the base URL and the website to scan
mozilla_api = 'https://observatory-api.mdn.mozilla.net/api/v2/scan'
website = 'https://www.shopify.com/'

#Isolate domain from url
website = website.split('://')[1]
domain = website.split('/')[0]

# post request
response = requests.post(f'{mozilla_api}?host={domain}')
print('Scan response:', response.json())

response=response.json()
extractMozilla= {key: response[key] for key in ("scanned_at","grade","score")}


with open("jsonMozilla.json", "w") as json_file:
    json.dump(extractMozilla,json_file,indent=4)



