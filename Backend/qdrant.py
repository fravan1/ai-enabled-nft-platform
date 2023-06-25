from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import json, csv
import numpy as np
from gensim.models import Word2Vec
from sentence_transformers import SentenceTransformer

# Function to create a Qdrant client
qdrant_client = QdrantClient(
    url="https://b8d36498-676b-465e-a42e-a7d679b977bd.us-east-1-0.aws.cloud.qdrant.io:6333", 
    api_key="uB4HCvoYAYtoX0wr-FaBfsVSuGblAG4NlAz-wGPqWrG0WJBKZvB7Aw",
)

# Loading the metadata.csv file and parsing row, by row, where each row deontes a token
with open('metadata.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    # print(data)

# Calling the create_collection function to create a collection named "test_collection" & store the data in it

# qdrant_client.recreate_collection(
#     collection_name="test_collection",
#     vectors_config=VectorParams(size=100, distance=Distance.COSINE),
# )

sentences = data[1][2:]
model = Word2Vec(sentences, vector_size=384, window=5, min_count=5, workers=4)
model.build_vocab(sentences)
model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)

# Defining the point containing the vector, the id as the contract address(from data), and payload as the entire row
point = PointStruct(
    id=1,
    vector=model.wv.vectors.tolist()[0],
    payload={
        "image_url": data[1][0],
        "address": data[1][1],
        "chain_identifier": data[1][2],
        "schema_name": data[1][3],
        "description": data[1][4],
        "last_sale": data[1][5],
        "rich_data": data[1][6]
    }
)

# adding the point to the collection using client.upsert
# qdrant_client.upsert(
#     collection_name="test_collection",
#     points=[point],
# )


# creating a new search Class
class Searcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # initializing the client
        self.qdrant_client = QdrantClient(
            url="https://b8d36498-676b-465e-a42e-a7d679b977bd.us-east-1-0.aws.cloud.qdrant.io:6333",
            api_key="uB4HCvoYAYtoX0wr-FaBfsVSuGblAG4NlAz-wGPqWrG0WJBKZvB7Aw",
        )
    
    def search(self, text):
        # Convert text to vector
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        embeddings = model.encode(query_text)

        # use vector to search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=embeddings,
            query_filter=None,
        )

        payloads = [hit.payload for hit in search_result]
        return payloads
    

# Creating a new instance of the Searcher class
searcher = Searcher(collection_name="test_collection")

# Searching for the closest vectors to the word "cat"
search_result = searcher.search(text=" ")

# Printing the results
print(json.dumps(search_result, indent=4, sort_keys=True))
