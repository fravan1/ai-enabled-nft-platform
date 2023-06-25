import requests
from flask import jsonify
import requests, json
import urllib.request
import qdrant_client
from Backend import Backend
from sentence_transformers import SentenceTransformer

# The backend only has API based access from the frontend and does not have any
# HTML pages to render. The routes are defined here.

# API route to query the asset from the opensea API
# The API is called with the asset contract address and the token id
# The API returns a JSON object with the asset details

# Azure Cognitive Services API endpoint and key
azure_endpoint = "https://waterlootest.cognitiveservices.azure.com/vision/v3.2/analyze"
api_key = "d5833954c09b4fe38ec2463ab4078218"
# Features to include in the analysis
features = "Adult,Brands,Categories,Color,Description,Faces,ImageType,Objects,Tags"

def upload_file(file):

    # Bearer token received during authentication
    bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGYyN2IxMDkxRjRiNDVFNzJERDg1RjBlRTY5RTIzMzcwOTgyQTkwRTAiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2ODc1OTQzNjA2MzIsIm5hbWUiOiJFVEhXYXRlcmxvbyJ9.fakf24JjopVQLKIuLOwq6BrV5HAGd1sPdacHe9OsZdw'

    # API endpoint URL
    url = 'https://api.web3.storage/upload'

    # Request headers with the Authorization header containing the bearer token
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Accept': 'application/json'
    }

    # Request payload (multipart/form-data)
    files = {
        'file': ('data.txt', open('data.txt', 'rb'), 'text/plain')
    }

    # Send the POST request
    response = requests.post(url, headers=headers, files=files)

    # Check the response
    if response.status_code == 200:
        print('Request succeeded!')
        # returning CID for further usage
        return response.json()['cid']
    else:
        print(f'Request failed with status code {response.status_code}')
        return None


@Backend.route('/')
def index():
    return jsonify({'message': 'Welcome to the backend'})

@Backend.route('/api/v1/get_asset/<contract_address>/<token_id>')
def get_asset(contract_address, token_id):
    # OpenSea API endpoint for a specific asset
    opensea_endpoint = f"https://api.opensea.io/api/v1/asset/{contract_address}/{token_id}"

    headers = {
        'Accept': 'application/json',
        'X-API-KEY': '02d7d6fbe51f446681317e33e5bd7468',
    }

    # Send GET request to the OpenSea API
    response = requests.get(opensea_endpoint, headers=headers)

    if response.status_code == 200:
        asset_data = response.json()

        # Extract the desired details from the asset data
        image_url = asset_data.get('image_url')

        primary_asset_contracts = asset_data.get('asset_contract', {})
        top_ownerships = asset_data.get('top_ownerships', [{}])[0]
        address = primary_asset_contracts.get('address')
        owner_address = top_ownerships.get('owner', {}).get('address')
        chain_identifier = primary_asset_contracts.get('chain_identifier')
        schema_name = primary_asset_contracts.get('schema_name')
        description = primary_asset_contracts.get('description')
        last_sale = asset_data.get('last_sale', {})

        image_metadata = {
            'image_url': image_url,
            'address': address,
            'owner_address': owner_address,
            'chain_identifier': chain_identifier,
            'schema_name': schema_name,
            'description': description,
            'last_sale': last_sale
        }

        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': api_key
        }

        # Request parameters
        params = {
            'visualFeatures': features,
            'language': 'en'
        }

        # download the image & call the convert_to_binary function
        image_data = urllib.request.urlopen(image_url).read()
        generated_data=requests.post(azure_endpoint, headers=headers, params=params, data=image_data).json()
        # cleaning the generated data to get the Categories,Description,Faces,ImageType,Objects,Tags
        # making a dictionary of the rich data cleaned from the generated data
        rich_data = {}
        rich_data['Categories'] = generated_data['categories'][0]['name']
        rich_data['Description'] = generated_data['description']['captions'][0]['text']
        rich_data['ImageType'] = generated_data['imageType']
        rich_data['Objects'] = generated_data['objects'][0]
        rich_data['Tags'] = generated_data['tags']
    else:
        print("Error:", response.status_code, response.text)

    # Adding the image_metadata & rich_data to a single JSON object
    image_metadata['rich_data'] = rich_data

    # Opening data.txt file in write mode & writing the image_metadata to the file
    with open('data.txt', 'w') as outfile:
        json.dump(image_metadata, outfile)

    # Calling the upload_file function to upload the data.txt file to IPFS
    image_metadata['cid'] = upload_file('data.txt')

    # Returning a Json object with Image URL, Address, Chain Identifier, Schema Name, Description, Last Sale, rich_data
    return jsonify(image_metadata)  


class Searcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # initializing the client
        self.qdrant_client = qdrant_client.QdrantClient(
            url="https://b8d36498-676b-465e-a42e-a7d679b977bd.us-east-1-0.aws.cloud.qdrant.io:6333",
            api_key="uB4HCvoYAYtoX0wr-FaBfsVSuGblAG4NlAz-wGPqWrG0WJBKZvB7Aw",
        )
    
    def search(self, text):
        # Convert text to vector
        model = SentenceTransformer('paraphrase-distilroberta-base-v1')
        embeddings = model.encode(text)

        # use vector to search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=embeddings,
            query_filter=None,
        )

        payloads = [hit.payload for hit in search_result]
        return payloads


# API Route to get search results from the Qdrant API. The API gets the Query Text as the input & returns a jsonified list of results
@Backend.route('/api/v1/search/<query_text>')
def search(query_text):
    # Function to create a Qdrant client
    client = qdrant_client.QdrantClient(
        url="https://b8d36498-676b-465e-a42e-a7d679b977bd.us-east-1-0.aws.cloud.qdrant.io:6333",
        api_key="uB4HCvoYAYtoX0wr-FaBfsVSuGblAG4NlAz-wGPqWrG0WJBKZvB7Aw",
    )

    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    embeddings = model.encode(query_text)

    # Creating a new instance of the Searcher class
    searcher = Searcher(collection_name="Noun")

    # Searching for the closest vectors to the word "cat"
    search_result = searcher.search(text=query_text)    

    return json.dumps(search_result, indent=4, sort_keys=True)
