import requests
import json
from dotenv import load_dotenv
import os
import time

# Load the environment variables from .env file
load_dotenv()

# Access api key
apiKey = os.environ.get('URLSCAN_API_KEY')
print(apiKey)


#query URL Scan API
headers = {'API-Key':apiKey,'Content-Type':'application/json'}
data = {"url": 'https://www.shopify.com/', "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
scanJson=response.json()


##get id for Result Api from Scan json respone
queryId= scanJson['uuid']

time.sleep(15)

#query to get results
headers = {'API-Key':apiKey,'Content-Type':'application/json'}
data = {"url": 'https://developer.mozilla.org/en-US/observatory/analyze?host=blog.logrocket.com'}
response = requests.get('https://urlscan.io/api/v1/result/'+queryId)
print(response)
print(response.json())
resultsJson= response.json()



#extract location data
locationDict= []
for entry in resultsJson['meta']['processors']['geoip']['data']:
    location={
        'ip': entry['ip'],
        'country': entry['geoip']['country_name'],
        'll':entry['geoip']['ll']
    }
    locationDict.append(location)
print(locationDict)



#extract security info
tlsDict= []
for entry in resultsJson['stats']['tlsStats']:
    tls={
        'protocols':entry['protocols'],
        'urlscan_securityState':entry['securityState']
    }
    tlsDict.append(tls)



protocolKeysList=[]
cleanKeys=[]
for protocols in tlsDict[0]['protocols']:
    cleanKey= protocols.replace("  ","")
    cleanKeys.append(cleanKey)
    
tlsDict[0]['protocols']=cleanKeys
print(tlsDict)


#extract malicious info
maliciousDict= []
print(resultsJson['verdicts']['overall'])
malicious={
        'urlscan_score':resultsJson['verdicts']['overall']['score'],
        'urlscan_malicious':resultsJson['verdicts']['overall']['malicious'],
        'urlscan_hasVerdict':resultsJson['verdicts']['overall']['hasVerdicts']
    }
maliciousDict.append(malicious)    
print(maliciousDict)




#create a new json to compile other json 
with open("urlScanResults.json",'w') as json_file:
    #json.dump(locationDict, json_file, indent=4)
    #json.dump(tlsDict, json_file, indent=4)
    #json.dump(maliciousDict, json_file, indent=4)
    combineDict= {**locationDict[0],**tlsDict[0],**maliciousDict[0]}
    json.dump(combineDict, json_file, indent=4)


with open("MozillaObserveFull.json",'r') as json_file:
    mozillaObserve= json.load(json_file)
    
with open("jsonMozilla.json",'r') as json_file:
    mozilla= json.load(json_file)

with open("urlScanResults.json",'r') as json_file:
    finalJson=json.load(json_file)   


finalJson['time']=mozilla["scanned_at"]
finalJson['mozilla_grade']=mozilla["grade"]
finalJson['mozilla_score']=mozilla["score"]
finalJson["mozilla_test_results"]=mozillaObserve

# Step 3: Write the updated JSON back to the file
with open("jsonAPI.json", "w") as file:
    json.dump(finalJson, file, indent=4)
