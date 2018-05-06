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
    print ("================*.ITEM AND CONTAINER*==================\n")
    
    i = 1
    for container in containers:
      item = {}
      item['type'] = "Textbook"
      item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + container.parent.a["href"]
      item['source'] = "BC Campus"
      if (i % 2) != 0:
          print ("IF.....", i)
          item['title'] = container.parent.a.text
          item['author'] = container.nextSibling.findNextSibling(text=True)
      else:
          print ("ELSE.....", i)
          item['title'] = container.a.text
          print ("CHILD:-")
          print (container.a)

          print ("ALL CHILDS:-")
          print (container.find_all('a'))
          print ("container.nextSibling:-")
          print (container.nextSibling)
          print ("findNextSibling(text=True)")
          print (container.nextSibling.findNextSibling(text=True))
          item['author'] = container.nextSibling.findNextSibling(text=True)
     
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

    break

with open("./json/bc-modified.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)