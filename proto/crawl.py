from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


# Path to your ChromeDriver (download it if you haven't already)
chrome_driver_path = r"C:\Users\kisen\Projects\siteChecker\proto\chromedriver.exe"

# Initialize Selenium WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
url = 'https://developer.mozilla.org/en-US/observatory/analyze?host=blog.logrocket.com'  # Replace with the actual URL you are scraping
driver.get(url)

# Wait for the page to load and for JavaScript to render the table
time.sleep(5)  # Adjust the time as needed for the page to fully load

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Close the WebDriver (you no longer need it once you have the page source)
driver.quit()

# Find the table with class "tests"
table = soup.find('table', {'class': 'tests'})

if table:
    # Extract rows from the <tbody>
    tbody = table.find('tbody')
    rows = tbody.find_all('tr') if tbody else []
    
    # Iterate over each row and extract the data
    for row in rows:
        cols = row.find_all('td')  # Find each column (td)
        col_data = [col.get_text(strip=True) for col in cols]  # Extract text data
        print('\t'.join(col_data))  # Print columns separated by tabs
else:
    print("Table with class 'tests' not found.")
