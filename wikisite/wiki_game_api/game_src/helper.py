
import openai
import numpy as np
import json
import os

def load_key():
    openai.api_key = os.environ["OPENAI_API_KEY"]

def get_embeddings(queries: list[str]) -> list[list[float]]:
    output = []
    load_key()
    response = openai.Embedding.create(model="text-embedding-ada-002", 
                                        input=queries[:2000])
    for data in response["data"]:
        output.append(np.array(data["embedding"]))
    return np.stack(output)

def get_embeddings_parallel(queries: list[str]) -> list[list[float]]:
    filename = "data/example_requests_to_parallel_process.jsonl"
    n_requests = 10_000
    jobs = [{"model": "text-embedding-ada-002", "input": str(x) + "\n"} for x in range(n_requests)]
    with open(filename, "w") as f:
        for job in jobs:
            json_string = json.dumps(job)
            f.write(json_string + "\n")