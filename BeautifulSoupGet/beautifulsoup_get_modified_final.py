from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

urls = [
    'https://open.bccampus.ca/find-open-textbooks/', 
    'https://open.bccampus.ca/find-open-textbooks/?start=10'
]

data = []

#opening up connection and grabbing page
for url in urls:
    uClient = urlopen(url)
    page_html = uClient.read()
    uClient.close()

    #html parsing
    page_soup = soup(page_html, "html.parser")

    #grabs info for each textbook
    containers = page_soup.find_all("h4")
    
    for index in range(0, len(containers), 2):
        item = {}
        item['type'] = "Textbook"
        item['title'] = containers[index].parent.a.text
        item['authors'] = containers[index].nextSibling.findNextSibling(text=True)
        item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + containers[index].parent.a["href"]
        item['source'] = "BC Campus"

        data.append(item) # add the item to the list

with open("./json/bc-modified-final.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)