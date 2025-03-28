

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import time
import json
import asyncio
from pyppeteer import launch


def crawlMozillaResultsTable(siteUrl):

    
   

    chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

     # Create the asyncio event loop
    loop = asyncio.get_event_loop()

    try:
        browser = loop.run_until_complete(launch(executablePath=chromePath, headless=True))

        #Launch the browser
        #browser = loop.run_until_complete(launch(headless=True))

        #Create a new page
        page = loop.run_until_complete(browser.newPage())

        #Isolate domain from url
        website = siteUrl.split('://')[1]
        domain = website.split('/')[0]


        #Navigate to the page and wait for it to load
        loop.run_until_complete(page.goto('https://developer.mozilla.org/en-US/observatory/analyze?host='+domain, {'waitUntil': 'networkidle0'}))

        pageSource = loop.run_until_complete(page.content())
        print(pageSource)

        loop.run_until_complete(browser.close())


    except Exception as e:
        # Catch any exception and print the error message
        print(f"Error occurred: {e}")
        jsonData={'message':'Error crawling Mozilla Observe result table'}
        return jsonData

    
    # Path to your ChromeDriver (download it if you haven't already)
    chrome_driver_path = r"C:\Users\kisen\Projects\siteChecker\src\utils\chromedriver.exe"

    
    '''
    options= Options()
    options.headless= True

    # Initialize Selenium WebDriver
    #service = Service(chrome_driver_path)
    #driver = webdriver.Chrome(service=service,options=options)
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    #Isolate domain from url
    website = siteUrl.split('://')[1]
    domain = website.split('/')[0]

    # Open the webpage
    url = 'https://developer.mozilla.org/en-US/observatory/analyze?host='+domain  # Replace with the actual URL you are scraping
    driver.get(url)

    # Wait for the page to load and for JavaScript to render the table
    #time.sleep(10)  # Adjust the time as needed for the page to fully load
    driver.implicitly_wait(10)
    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    tableData=[]

    # Close the WebDriver 
    driver.quit()
    '''

    # Find the table with class "tests"
    soup = BeautifulSoup(pageSource,'html.parser')
    tableData=[]
    table = soup.find('table', {'class': 'tests'})

  


    if table is not None:
        rows = table.find_all('tr')
        headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]
        #print(headers)

        # Extract rows from the <tbody>
        tbody = table.find('tbody')
        rows = tbody.find_all('tr') if tbody else []

        

        # `I`terate over each row and extract the data
        for row in rows:
            cols = row.find_all('td')  # Find each column (td)
            colData = [col.get_text(strip=True) for col in cols]  # Extract text data
            #print('\t'.join(colData))  # Print columns separated by tabs

            rowDict= dict(zip(headers,colData))
            tableData.append(rowDict)


        with open('MozillaObserveFull.json', 'w') as json_file:
            json.dump(tableData, json_file, indent=4)   


        #Clean pass/fail in json
        with open('MozillaObserveFull.json', 'r') as json_file:
            jsonData = json.load(json_file)


        for entry in jsonData:
            if "Passed" in entry['Score']:
                entry['Score']="Passed"

            if "Failed" in entry['Score']:
                entry['Score']="Failed"

            else:
                entry['Score']="Not Applicable"


    
    else:
        
        jsonData={'message':'Error crawling Mozilla Observe result table'}
        #print(jsonData)
    

    
    

    #To write to json file
    """ with open('MozillaObserveFull.json', 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)  """

    return jsonData  
    