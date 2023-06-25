import requests
from flask import jsonify
import re
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from time import sleep
from sklearn.decomposition import PCA
import numpy as np

# Azure Cognitive Services API endpoint and key
endpoint = "https://waterlootest.cognitiveservices.azure.com/vision/v3.2/analyze"
api_key = "e7b18d719c324918a038199c4d9564eb"
# Features to include in the analysis
features = "Brands,Categories,Color,Description,Objects,Tags"

# Function to create a Qdrant client
qdrant_client = QdrantClient(
    url="https://b8d36498-676b-465e-a42e-a7d679b977bd.us-east-1-0.aws.cloud.qdrant.io:6333", 
    api_key="uB4HCvoYAYtoX0wr-FaBfsVSuGblAG4NlAz-wGPqWrG0WJBKZvB7Aw",
)

def process_image(image_url):
    # Prepare the headers
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key
    }

    # Request parameters
    params = {
        'visualFeatures': features,
        'language': 'en'
    }

    # Request body
    body = {
        'url': image_url
    }

    # Send the REST request
    response = requests.post(endpoint, headers=headers, params=params, json=body)

    # Handle the response
    if response.status_code == 200:
        return response.json()
    else:
        return "Error:", response.status_code, response.text

def extract_values(text):
    pattern = r'Noun (\d+)\nBorn(.*)\n→\n\nHead\n\n(.*)\n\n\nGlasses\n\n(.*)\n\n\nAccessory\n\n(.*)\n\n\nBody\n\n(.*)\n\n\nBackground\n\n'
    result = re.findall(pattern, text)
    return result[0]


def process_file(file_path):
# Read the Noun_data text file & split the data into a list of strings using the delimiter '///'
    base_url = 'https://noun.pics/'

    with open(file_path, 'r') as file:
        text = file.read()
        text = text.split('///')

    # from text[2] pnwards, the data is in the format:
    # '\nNoun 755\nBornJune 23, 2023\n→\n\nHead\n\nCheese\n\n\nGlasses\n\nSquare black\n\n\nAccessory\n\nTee yo\n\n\nBody\n\nBluegrey\n\n\nBackground\n\n'
    # We need to extract the Noun, 755  in this case, and the values associated with it, which are: 
    # Born : June 23, 2023
    # Head : Cheese
    # Glasses : Square black
    # Accessory : Tee yo
    # Body : Bluegrey

    final_list = []

    # parsing through the list - text of strings, and extracting the values using the extract_values function
    for i in range(2, len(text)-1):

        print("Processing Noun:", extract_values(text[i])[0])

        metadata = extract_values(text[i])
        # fetching the image url from the data dictionary
        image_url = base_url + metadata[0] + '.png'
        # Storing the other parameters in the image_metadata dictionary with the key being the Noun number - from the result[0][0]
        image_metadata = {}
        image_metadata['Noun'] = metadata[0]
        image_metadata['Born'] = metadata[1]
        image_metadata['Head'] = metadata[2]
        image_metadata['Glasses'] = metadata[3]
        image_metadata['Accessory'] = metadata[4]
        image_metadata['Body'] = metadata[5]
        generated_data = process_image(image_url)
        sleep(3)
        # cleaning the generated data to get the Categories,Description,Faces,ImageType,Objects,Tags
        # making a dictionary of the rich data cleaned from the generated data
        rich_data = {}
        rich_data['Categories'] = generated_data['categories'][0]['name']
        rich_data['Description'] = generated_data['description']['captions'][0]['text']
        rich_data['Tags'] = generated_data['tags']

        # merging the image_metadata and rich_data dictionaries
        merged_data = {**image_metadata, **rich_data}

        print("Appending Noun:", merged_data['Noun'] + " to the final list")

        final_list.append(merged_data)
        
    return final_list


def upload_data(data):

    print("Uploading data to Qdrant")

    points = []
    # Iterationg through the data list, converting each item to point and uploading it to the collection
    for i in range(len(data)):

        print("Converting Noun:", data[i]['Noun'] + " to a point")

        # Extract relevant text values from the JSON
        text_values = [
            data[i]['Noun'],
            data[i]['Born'],
            data[i]['Head'],
            data[i]['Glasses'],
            data[i]['Accessory'],
            data[i]['Body'],
            data[i]['Categories'],
            data[i]['Description']
        ]

        tags = [tag['name'] for tag in data[i]['Tags']]

        # Concatenate the text values and tags
        encoded_text = ' '.join(text_values + tags)

        # Vectorizing the data using the SentenceTransformer
        model = SentenceTransformer('paraphrase-distilroberta-base-v1')
        embeddings = model.encode([encoded_text])

        point = PointStruct(
            id=int(data[i]['Noun']),
            vector=embeddings.tolist()[0],
            payload=data[i]
        )

        points.append(point)
    
    print("Uploading points to Qdrant")

    # uploading the points to the Noun collection through the client.upsert function
    qdrant_client.upsert(
        collection_name="Noun",
        points=points,
    )

    print("Data uploaded to Qdrant")

upload_data(process_file('Noun_data.txt'))
