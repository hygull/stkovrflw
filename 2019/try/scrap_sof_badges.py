import requests
from bs4 import BeautifulSoup 

class ScrapStackOverflowBadge(object):
    def __init__(self, url, *args, **kwargs):
        super(ScrapStackOverflowBadge, self).__init__(*args, **kwargs)

        self.url = url
        

    def get_soup(self, html_text=False):
        response = {}

        try:
            res = requests.get(self.url)
            response["status_code"] = res.status_code

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                response["soup"] = soup

                if html_text is True:
                    response["html_text"] = res.text
            else:
                response["message"] = "Partially successful work, but something bad happened"
        except Exception as error:
            response["status_code"] = 600 # Custom status code (indication of an exception)
            response["message"] = str(error)

        return soup


if __name__ == "__main__":
    url = "https://stackoverflow.com/help/badges"
    scrap = ScrapStackOverflowBadge(url)
    print("Processing ", scrap.url)

    response = scrap.get_soup(html_text=True)
    print(soup)
