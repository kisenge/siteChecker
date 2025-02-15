from utils.tableCrawler import crawlMozillaResultsTable
from utils.mozillaAPI import callMozillaApi


#mozillaTestResults=crawlMozillaResultsTable('https://www.postman.com/downloads/postman-agent/')

mozillaApiResults= callMozillaApi('https://www.postman.com/downloads/postman-agent/')
print(mozillaApiResults)