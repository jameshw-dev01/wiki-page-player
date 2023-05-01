import requests
from bs4 import BeautifulSoup, Tag
def get_internal_links(links: list[Tag]) ->list[Tag]:
    internal_links = []
    for link in links:
        link_text:str = link.get("href")
        in_paragraph = False
        for parent in link.parents:
            if parent is not None and parent.name == 'p':
                in_paragraph = True
        if (link_text is not None 
            and link_text.startswith("/wiki/")
            and ":" not in link_text and in_paragraph):
                internal_links.append(link)
    return internal_links

def parse_topics_from_links(internal_links:list[str]):
    topics = []
    for link in internal_links:
        link_text = link.get('href')[6:].replace("_", " ")
        topics.append(link_text)
    return topics
class WikiPage:
    def __init__(self, topic_link: str, exclude_links:list[str] = []):
        base_url = "https://en.wikipedia.org"
        response = requests.get(base_url+topic_link)
        if response.status_code != 200:
            raise ValueError()
        self.soup = BeautifulSoup(response.text, "html.parser")
        links = self.soup.find(id="bodyContent").find_all('a')
        self.internal_links = get_internal_links(links)
        self.internal_links = [link for link in self.internal_links 
                               if link.get('href') not in exclude_links]
        self.parsed_topics = parse_topics_from_links(self.internal_links)
    def get_title(self) -> str:
        title = self.soup.find('h1', {'id': 'firstHeading'}).get_text()
        if title is None:
            title = ""
        return title
    def get_intro(self) -> str:
        first_p = self.soup.find('p')
        if first_p is None or first_p.get_text("").strip() == "":
            first_p = first_p.find_next('p')
        if first_p is not None:
            return first_p.get_text("")
        return ""

    def get_link_context(self, link: Tag) -> str:
        link.string = "*" + link.string + '*'
        for parent in link.parents:
            if parent is not None and parent.name == 'p':
                return parent.get_text("")
        return ""