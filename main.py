from compare import get_closest_word, get_closest_but_different
from wiki_search import parse_topics_from_links, search_topic
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
    current_word = current[6:].replace("_", " ")
    tried_links = {current}
    while current_word != end_word and num_steps < 30:
        scraped_links = search_topic(current)
        internal_links = []
        for link in scraped_links:
            if link.get('href') == end:
                print(end)
                return
            if link.get('href') not in tried_links:
                internal_links.append(link)
        linked_topics = parse_topics_from_links(internal_links)
        best_index, distance = get_closest_but_different(end_word, linked_topics, current_word)
        current = internal_links[best_index].get("href")
        current_word = current[6:].replace("_", " ")
        tried_links.add(current)
        print(current_word,  distance)
        num_steps += 1

wiki_game("/wiki/Fire", "/wiki/Biology")