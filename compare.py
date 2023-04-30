
import numpy as np
from helper import get_embeddings, load_key
from wiki_search import *

def get_closest_word(target, search_words):

    target_embedding = get_embeddings([target])[0]
    linked_embeddings = get_embeddings(search_words)
    result = similar_metric(target_embedding, linked_embeddings)
    best = np.argmax(result)
    return best, result[best]

def get_closest_but_different(target, search_words, current_word):
    target_words = set(target.split(" "))
    target_embedding = get_embeddings([target])[0]
    linked_embeddings = get_embeddings(search_words)
    current_embeddings = get_embeddings([current_word])[0]
    result1 = similar_metric(target_embedding, linked_embeddings)
    for i in range(result1.shape[0]):
        if "List of" in search_words[i]:
            result1[i] *= 1.1
    best = np.argmax(result1)
    return best, result1[best]

def similar_metric(x, M):
    dot_product = np.dot(x, M.T)
    norm_a = np.linalg.norm(x)
    norm_b = np.linalg.norm(M,axis=1)
    score = dot_product / (norm_a * norm_b)
    return score