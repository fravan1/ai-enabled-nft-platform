from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import json, csv
import numpy as np

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

qdrant_client.recreate_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)

# Tokenizing the data and adding it to the collection using client.upsert


print(point)

breakpoint()

# adding the point to the collection using client.upsert
qdrant_client.upsert(
    collection_name="test_collection",
    points=[point],
)

# viewing the recently added data in the collection
qdrant_client.describe_collection(collection_name="test_collection")
