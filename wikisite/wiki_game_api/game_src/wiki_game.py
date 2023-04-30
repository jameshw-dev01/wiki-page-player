from wiki_game_api.game_src import compare
from wiki_game_api.game_src import wiki_search
def filter_words(search_words, exclude):
    filtered_words = []
    for words in search_words:
        discard = False
        for test_word in exclude:
            if test_word in words:
                discard = True
        if not discard:
            filtered_words.append(words)

def wiki_game(start, end):
    num_steps = 0
    current = start
    end_word = end[6:].replace("_", " ")
    tried_links = [current]
    while current != end and num_steps < 30:
        scraped_links = wiki_search.search_topic(current)
        internal_links = []
        for link in scraped_links:
            if link.get('href') == end:
                tried_links.append(end)
                return tried_links
            if link.get('href') not in tried_links:
                internal_links.append(link)
        linked_topics = wiki_search.parse_topics_from_links(internal_links)
        best_index, _ = compare.get_closest_word(end_word, linked_topics)
        current = internal_links[best_index].get("href")
        tried_links.append(current)
        num_steps += 1
    
    return tried_links

if __name__ == "__main__":
    print(wiki_game("/wiki/Fire", "/wiki/Biology"))