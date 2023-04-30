import requests
from bs4 import BeautifulSoup
def get_internal_links(links):
    internal_links = []
    for link in links:
        link_text:str = link.get("href")
        if (link_text is not None 
            and link_text.startswith("/wiki/")
            and ":" not in link_text):
                internal_links.append(link)
    return internal_links
def search_topic(topic):
    base_url = "https://en.wikipedia.org"
    response = requests.get(base_url+topic)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find(id="bodyContent").find_all('a')
    internal_links = get_internal_links(links)
    return internal_links

def parse_topics_from_links(internal_links:list[str]):
    topics = []
    for link in internal_links:
        link_text = link.get('href')[6:].replace("_", " ")
        topics.append(link_text)
    return topics
