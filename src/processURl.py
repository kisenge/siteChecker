from utils.tableCrawler import crawlMozillaResultsTable
from utils.mozillaAPI import callMozillaApi
from utils.urlscanChecker import callUrlScanApi


#def processData(url):

#scan Mozilla results table
mozillaTestResults=crawlMozillaResultsTable('https://www.postman.com/downloads/postman-agent/')

#call Mozilla Api
mozillaApiResults= callMozillaApi('https://www.postman.com/downloads/postman-agent/')

#call urlscan Api
urlScanApiResults= callUrlScanApi('https://www.postman.com/downloads/postman-agent/')


combinedDict= {**mozillaTestResults,**mozillaApiResults,**urlScanApiResults}
print(combinedDict)





'''

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

'''

#return mozillaApiResults