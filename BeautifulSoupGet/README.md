You do not need to remove any kind of duplicates. 

The only need is to update the code.

### WHERE THE PROBLEM WAS?

I know you want this because you're getting duplicated dictionaries.

This is because you're selecting containers as `h4` elements & f
or each book details, the specified page links https://open.bccampus.ca/find-open-textbooks/ 
and https://open.bccampus.ca/find-open-textbooks/?start=10
are having 2 `h4` elements.

That's why, instead of getting a list of 20 items(10 from each page) as containers list you're 
getting just double i.e. list of 40 items where each item is `h4` element. 

You may get different different values for each of these 40 items but the problem is while selecting parents.
As it gives the same element so the same text.

Let's clarify the problem by assuming the following dummy code.

    <li> <!-- 1st book -->
        <h4>
            <a> Text 1 </a>
        </h4>
        <h4>
            <a> Text 2 </a>
        </h4>
    </li>
    <li> <!-- 2nd book -->
        <h4>
            <a> Text 3 </a>
        </h4>
        <h4>
            <a> Text 4 </a>
        </h4>
    </li>
    ...
    ...
    <li> <!-- 20th book -->
        <h4>
            <a> Text 39 </a>
        </h4>
        <h4>
            <a> Text 40 </a>
        </h4>
    </li>

&raquo;&raquo; **containers = page_soup.find_all("h4");** will give the below list of `h4` elements.

    [
        <h4>
            <a> Text 1 </a>
        </h4>,
        <h4>
            <a> Text 2 </a>
        </h4>,
        <h4>
            <a> Text 3 </a>
        </h4>,
        <h4>
            <a> Text 4 </a>
        </h4>,
        ...
        ...
        ...
        <h4>
            <a> Text 39 </a>
        </h4>,
        <h4>
            <a> Text 40 </a>
        </h4>
    ]

&raquo;&raquo; In case of your code, 1st iteration of inner for loop will refer below element as **container** variable. 
 
    <h4>
        <a> Text 1 </a>
    </h4>

&raquo;&raquo; 2nd iteration will refer below element as **container** variable.

    <h4>
        <a> Text 1 </a>
    </h4>

&raquo;&raquo; In both the above (1st, 2nd) iterations of inner for loop, **container.parent;** will give the below element.

    <li> <!-- 1st book -->
        <h4>
            <a> Text 1 </a>
        </h4>
        <h4>
            <a> Text 2 </a>
        </h4>
    </li>

&raquo;&raquo; And **container.parent.a** will give the below element.

    <a> Text 1 </a>


&raquo;&raquo; Finally, **container.parent.a.text** gives the below text as our book title for first 2 books.
    
    Text 1

That's why we are getting duplicated dictionaries as our dynamic `title` & `author` are also same. 

Let's get rid of this problem 1 by 1.

### WEB PAGE DETAILS

1. We have links of 2 web pages.

2. Each web page is having details of 10 text books.

3. Each book details is having 2 `h4` elements.

4. So total, 2x10x2 = 40 `h4` elements.

### OUR GOAL:

1. Our goal is to only get an array/list of 20 dictionaries not 40.

2. So there's a need to iterate the containers list by 2 items i.e. 
by just skipping 1 item in each iteration.

### MODIFIED WORKING CODE:

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
            item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + containers[index].parent.a["href"]
            item['source'] = "BC Campus"
            item['title'] = containers[index].parent.a.text
            item['authors'] = containers[index].nextSibling.findNextSibling(text=True)

        data.append(item) # add the item to the list

    with open("./json/bc-modified-final.json", "w") as writeJSON:
      json.dump(data, writeJSON, ensure_ascii=False)

### OUTPUT:

    [
        {
            "type": "Textbook",
            "title": "Vital Sign Measurement Across the Lifespan - 1st Canadian edition",
            "authors": " Jennifer L. Lapum, Margaret Verkuyl, Wendy Garcia, Oona St-Amant, Andy Tan, Ryerson University",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=feacda80-4fc1-40a5-b713-d6be6a73abe4&contributor=&keyword=&subject=",
            "source": "BC Campus"
        },
        {
            "type": "Textbook",
            "title": "Exploring Movie Construction and Production",
            "authors": " John Reich, SUNY Genesee Community College",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=19892992-ae43-48c4-a832-59faa1d7108b&contributor=&keyword=&subject=",
            "source": "BC Campus"
        },
        {
            "type": "Textbook",
            "title": "Project Management",
            "authors": " Adrienne Watt",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=8678fbae-6724-454c-a796-3c6667d826be&contributor=&keyword=&subject=",
            "source": "BC Campus"
        },
        ...
        ...
        ...
        {
            "type": "Textbook",
            "title": "Naming the Unnamable: An Approach to Poetry for New Generations",
            "authors": " Michelle Bonczek Evory. Western Michigan University",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=8880b4d1-7f62-42fc-a912-3015f216f195&contributor=&keyword=&subject=",
            "source": "BC Campus"
        }
    ]

Finally, I tried to modify your code and added more details `description`, `date` & `categories` to dictionary object.

> Python version: 3.6
>
> Dependency: pip install beautifulsoup4

## MODIFIED WORKING CODE (ENHANCED VERSION):

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

            # Store book's information as per given the web page (all 5 are dynamic)
            item['title'] = containers[index].parent.a.text
            item["catagories"] = [a_tag.text for a_tag in containers[index + 1].find_all('a')]
            item['authors'] = containers[index].nextSibling.findNextSibling(text=True).strip()
            item['date'] = containers[index].parent.find_all("strong")[1].findNextSibling(text=True).strip()
            item["description"] = containers[index].parent.p.text.strip()

            # Store extra information (1st is dynamic, last 2 are static)
            item['link'] = "https://open.bccampus.ca/find-open-textbooks/" + containers[index].parent.a["href"]
            item['source'] = "BC Campus"
            item['type'] = "Textbook"

            data.append(item) # add the item to the list

    with open("./json/bc-modified-final-my-own-version.json", "w") as writeJSON:
        json.dump(data, writeJSON, ensure_ascii=False)

## OUTPUT (ENHANCED VERSION):

    [
        {
            "title": "Vital Sign Measurement Across the Lifespan - 1st Canadian edition",
            "catagories": [
                "Ancillary Resources"
            ],
            "authors": "Jennifer L. Lapum, Margaret Verkuyl, Wendy Garcia, Oona St-Amant, Andy Tan, Ryerson University",
            "date": "May 3, 2018",
            "description": "Description: The purpose of this textbook is to help learners develop best practices in vital sign measurement. Using a multi-media approach, it will provide opportunities to read about, observe, practice, and test vital sign measurement.",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=feacda80-4fc1-40a5-b713-d6be6a73abe4&contributor=&keyword=&subject=",
            "source": "BC Campus",
            "type": "Textbook"
        },
        {
            "title": "Exploring Movie Construction and Production",
            "catagories": [
                "Adopted"
            ],
            "authors": "John Reich, SUNY Genesee Community College",
            "date": "May 2, 2018",
            "description": "Description: Exploring Movie Construction and Production contains eight chapters of the major areas of film construction and production. The discussion covers theme, genre, narrative structure, character portrayal, story, plot, directing style, cinematography, and editing. Important terminology is defined and types of analysis are discussed and demonstrated. An extended example of how a movie description reflects the setting, narrative structure, or directing style is used throughout the book to illustrate ...[more]",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=19892992-ae43-48c4-a832-59faa1d7108b&contributor=&keyword=&subject=",
            "source": "BC Campus",
            "type": "Textbook"
        },
        ...
        ...
        ...
        {
            "title": "Naming the Unnamable: An Approach to Poetry for New Generations",
            "catagories": [],
            "authors": "Michelle Bonczek Evory. Western Michigan University",
            "date": "Apr 27, 2018",
            "description": "Description: Informed by a writing philosophy that values both spontaneity and discipline, Michelle Bonczek Evory’s Naming the Unnameable: An Approach to Poetry for New Generations  offers practical advice and strategies for developing a writing process that is centered on play and supported by an understanding of America’s rich literary traditions. With consideration to the psychology of invention, Bonczek Evory provides students with exercises aimed to make writing in its early stages a form of play that ...[more]",
            "link": "https://open.bccampus.ca/find-open-textbooks/?uuid=8880b4d1-7f62-42fc-a912-3015f216f195&contributor=&keyword=&subject=",
            "source": "BC Campus",
            "type": "Textbook"
        }
    ]

That's it. Thanks.