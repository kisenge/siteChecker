import requests
import json
from dotenv import load_dotenv
import os


# Load the environment variables from .env file
load_dotenv()

# Now you can access the environment variable just like before
apiKey = os.environ.get('URLSCAN_API_KEY')
print(apiKey)


""" headers = {'API-Key':apiKey,'Content-Type':'application/json'}
data = {"url": 'https://developer.mozilla.org/en-US/observatory/analyze?host=blog.logrocket.com', "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
 """


headers = {'API-Key':apiKey,'Content-Type':'application/json'}
data = {"url": 'https://developer.mozilla.org/en-US/observatory/analyze?host=blog.logrocket.com', "visibility": "public"}
response = requests.get('https://urlscan.io/api/v1/result/$uuid/'+'9671c025-4c3c-48cc-9574-b43c61e0aa44''',headers=headers)
print(response)
print(response.json())


