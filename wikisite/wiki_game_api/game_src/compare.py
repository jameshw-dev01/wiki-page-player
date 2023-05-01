import numpy as np
from wiki_game_api.game_src import helper

def get_closest_word(target, search_words):

    target_embedding = helper.get_embeddings([target])[0]
    linked_embeddings = helper.get_embeddings(search_words)
    result = similar_metric(target_embedding, linked_embeddings)
    #for i in range(result.shape[0]):
    #    if "List of" in search_words[i]:
    #        result[i] *= 1.1
    best = np.argmax(result)
    return best, result[best]

def similar_metric(x, M):
    dot_product = np.dot(x, M.T)
    norm_a = np.linalg.norm(x)
    norm_b = np.linalg.norm(M,axis=1)
    score = dot_product / (norm_a * norm_b)
    return score