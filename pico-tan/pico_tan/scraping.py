"""
scraping.py bundles together all of pico-tans abilities that involve scraping the web
"""
import requests
import urllib
from beautifulscraper import BeautifulScraper
import re

def urban_dict(term):
    scraper = BeautifulScraper()

    url = "https://www.urbandictionary.com/define.php?term=%s" % (term)

    page = scraper.go(url)
    def_div = page.find("div",{'class' : 'meaning'})

    definition = ""
    #for loop strips html tags, also removes carriage return
    if(def_div is not None):
        for container in def_div:
            t = str(container)
            t = re.sub('<.*?>' , ' ', t)
            t = t.rstrip()
            definition += t

        print("\n" + re.sub('\+', ' ',term) + ": \n" + definition + "\n")
    else:
        print("term not found(check case)")

if __name__ == "__main__":
    pass
