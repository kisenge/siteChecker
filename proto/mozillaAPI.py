import requests
import time

# Define the base URL and the website to scan
mozilla_api = 'https://observatory-api.mdn.mozilla.net/api/v2/scan'
website = 'https://blog.logrocket.com'

# post request
response = requests.post(f'{mozilla_api}?host={website}')
print('Scan response:', response.json())


