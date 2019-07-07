from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

urls = ['https://open.bccampus.ca/find-open-textbooks/', 
'https://open.bccampus.ca/find-open-textbooks/?start=10']

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
    print (containers,"\n", len(containers))
    print ("======================================*.ITEM AND CONTAINER*======================================\n")
    i = 1
    for container in containers:
       item = {}
       item['type'] = "Textbook"
       item['title'] = container.parent.a.text
       item['author'] = container.nextSibling.findNextSibling(text=True)
       item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + container.parent.a["href"]
       item['source'] = "BC Campus"

       data.append(item) # add the item to the list
       print (i, ".........................................................")
       print (item)
       print ("\n")
       print (container)
       print ("\n")
       print (container.parent)
       print ("\n")
       print (container.parent.a)
       print ("\n")
       print (container.parent.a.text)
       i += 1
       print (".............................................................\n")

with open("./json/bc-new.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)