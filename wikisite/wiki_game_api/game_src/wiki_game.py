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

def wiki_game(start: str, end: str):
    num_steps = 0
    current = start
    end_word = end[6:].replace("_", " ")
    game_data: dict[str, list[str]] = {}
    game_data["searched_links"] = []
    game_data["intros"] = []
    game_data["link_contexts"] = []
    game_data["titles"] = []
    while current != end and num_steps < 30:
        wiki_page = wiki_search.WikiPage(current, game_data["searched_links"])
        best_index, _ = compare.get_closest_word(end_word, wiki_page.parsed_topics)
        print(current)
        game_data["titles"].append(wiki_page.get_title())
        game_data["searched_links"].append(current)
        game_data["intros"].append(wiki_page.get_intro())
        game_data["link_contexts"].append(wiki_page.get_link_context(wiki_page.internal_links[best_index]))
        current = wiki_page.internal_links[best_index].get("href")
        num_steps += 1
    game_data["searched_links"].append(current)
    return game_data

if __name__ == "__main__":
    print(wiki_game("/wiki/Leo_Tolstoy", "/wiki/Dolphin"))