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
    
    for index in range(0, len(containers), 2):
      item = {}
      
      # Store book's information as per given the web page (all 5 are dynamic)
      item['title'] = containers[index].parent.a.text
      item["catagories"] = [a_tag.text for a_tag in containers[index + 1].find_all('a')]
      item['authors'] = [author.strip() for author in containers[index].nextSibling.findNextSibling(text=True).strip().split(",")]
      print (index, containers[index].parent.find_all("strong")[1].findNextSibling(text=True))
      item['date'] =  "" #containers[index].find("strong")[1].findNextSibling(text=True)
      item["description"] = containers[index].parent.p.text.strip()

      # Store extra information (1st is dynamic, last 2 are static)
      item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + containers[index].parent.a["href"]
      item['source'] = "BC Campus"
      item['type'] = "Textbook"
      
     
      
      
      data.append(item) # add the item to the list

with open("./json/bc-modified-final-my-own-version.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)