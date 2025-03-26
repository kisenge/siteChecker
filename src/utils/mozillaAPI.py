import requests
import time
import json

def callMozillaApi(siteUrl):
    # Define the Api url
    mozilla_api = 'https://observatory-api.mdn.mozilla.net/api/v2/scan'
    

    #Isolate domain from url
    website = siteUrl.split('://')[1]
    domain = website.split('/')[0]

    # post request
    response = requests.post(f'{mozilla_api}?host={domain}')
    #eprint('Scan response:', response.status_code)


    if response.status_code==200:
        response=response.json()
        #print(response)
        extractMozilla= {key: response[key] for key in ("scanned_at","grade","score")}

        # To write to file
        """ with open("jsonMozilla.json", "w") as json_file:
        json.dump(extractMozilla,json_file,indent=4) """


    else:
        extractMozilla={"message":"Error calling Mozilla Api."}


    return extractMozilla







