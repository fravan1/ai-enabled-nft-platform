from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import json, csv
import numpy as np
from gensim.models import Word2Vec

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
model = Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4)
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
qdrant_client.upsert(
    collection_name="test_collection",
    points=[point],
)


