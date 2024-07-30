import requests
import dewiki
import sys

# Usage example: 
# python request_wikipedia.py "Chocolatine"


def query_wikipedia(search_string):
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": False,
        "titles": search_string,
        "redirects": 1,  # Follow redirects
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()


def get_first_page_content(json_response):
    pages = json_response["query"]["pages"]
    page_id = next(iter(pages))
    page_content = pages[page_id].get("extract", "No content found.")
    
    return page_content


def write_to_file(content, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <search_string>")
        return

    json_response = query_wikipedia(sys.argv[1])
    page_content = get_first_page_content(json_response)
    if not page_content or page_content == "No content found.":
        print("No content found or the page may be a redirect without content.")
        return
    plain_text_content = dewiki.from_string(page_content)
    write_to_file(plain_text_content, sys.argv[1].lower().replace(" ", "_") + ".txt")


if __name__ == "__main__":
    main()