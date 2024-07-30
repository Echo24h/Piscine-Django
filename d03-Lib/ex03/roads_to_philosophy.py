import sys
import requests
from bs4 import BeautifulSoup


# Usage example:
# python3 roads_to_philosophy.py "Albert Einstein"


class WikipediaScraper:

    def __init__(self) -> None:
        self.visited_pages = []
        self.road_to_philosophy_start = ""


    def road_to_philosophy(self, path : str) -> None:

        URL = f"https://en.wikipedia.org/wiki/{path.replace(' ', '_').replace('/wiki/', '')}"

        try:
            response = requests.get(URL)
            response.raise_for_status()
        except requests.RequestException as e:
            self.visited_pages = []
            self.road_to_philosophy_start = ""
            print(f"Error fetching the URL {URL} :\n{e}")
            sys.exit(1)

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1", id="firstHeading").text
        print(title)

        if self.road_to_philosophy_start == "":
            self.road_to_philosophy_start = title

        if title == "Philosophy":
            print(f"{len(self.visited_pages)} roads from {self.road_to_philosophy_start} to philosophy!")
            self.visited_pages = []
            self.road_to_philosophy_start = ""
            sys.exit(0)
        
        if title in self.visited_pages: 
            self.visited_pages = []
            self.road_to_philosophy_start = ""
            print("It leads to an infinite loop!")
            sys.exit(1)

        self.visited_pages.append(title)

        content = soup.find("div", id="mw-content-text")

        links = content.select("p > a")
        for link in links:
            if link.get('href') is not None and link['href'].startswith('/wiki/')\
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                return self.road_to_philosophy(link["href"])

        self.visited_pages = []
        self.road_to_philosophy_start = ""
        print("It leads to a dead end !.")
        return 


def main():
    if len(sys.argv) != 2:
        print("Usage: python roads_to_philosophy.py <search_string>")
        sys.exit(1)
    
    scraper = WikipediaScraper()
    scraper.road_to_philosophy(sys.argv[1].replace(' ', '_'))


if __name__ == "__main__":
    main()