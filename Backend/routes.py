import requests
from flask import jsonify
import requests
import urllib.request

from Backend import Backend

# The backend only has API based access from the frontend and does not have any
# HTML pages to render. The routes are defined here.

# API route to query the asset from the opensea API
# The API is called with the asset contract address and the token id
# The API returns a JSON object with the asset details

# Azure Cognitive Services API endpoint and key
endpoint = "https://waterlootest.cognitiveservices.azure.com/vision/v3.2/analyze"
api_key = "e7b18d719c324918a038199c4d9564eb"
# Features to include in the analysis
features = "Adult,Brands,Categories,Color,Description,Faces,ImageType,Objects,Tags"

def process_image(data):
    # Prepare the headers
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key
    }

    # Request parameters
    params = {
        'visualFeatures': features,
        'language': 'en'
    }

    # Send the REST request
    response = requests.post(endpoint, headers=headers, params=params, data=data)

    # Handle the response
    if response.status_code == 200:
        return(response.json())
    else:
        return("Error:", response.status_code, response.text)

@Backend.route('/')
def index():
    return jsonify({'message': 'Welcome to the backend'})

@Backend.route('/api/v1/get_asset/<contract_address>/<token_id>')
def get_asset(contract_address, token_id):
    # OpenSea API endpoint for a specific asset
    endpoint = f"https://api.opensea.io/api/v1/asset/{contract_address}/{token_id}"

    headers = {
        'Accept': 'application/json',
        'X-API-KEY': '02d7d6fbe51f446681317e33e5bd7468',
    }

    # Send GET request to the OpenSea API
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        asset_data = response.json()

        # Extract the desired details from the asset data
        image_url = asset_data.get('image_url')

        primary_asset_contracts = asset_data.get('asset_contract', {})
        address = primary_asset_contracts.get('address')
        chain_identifier = primary_asset_contracts.get('chain_identifier')
        schema_name = primary_asset_contracts.get('schema_name')
        description = primary_asset_contracts.get('description')

        last_sale = asset_data.get('last_sale', {})

    else:
        print("Failed to fetch OpenSea asset:", response.status_code)

    # Handle the response
    if response.status_code == 200:
        # download the image & call the convert_to_binary function
        image_data = urllib.request.urlopen(image_url).read()
        generated_data = process_image(image_data)
        # cleaning the generated data to get the Categories,Description,Faces,ImageType,Objects,Tags
        # making a dictionary of the rich data cleaned from the generated data
        rich_data = {}
        rich_data['Categories'] = generated_data['categories'][0]['name']
        rich_data['Description'] = generated_data['description']['captions'][0]['text']
        rich_data['ImageType'] = generated_data['imageType']
        rich_data['Objects'] = generated_data['objects'][0].keys()
        rich_data['Tags'] = generated_data['tags']
    else:
        print("Error:", response.status_code, response.text)


    # Returning a Json object with Image URL, Address, Chain Identifier, Schema Name, Description, Last Sale, rich_data
    return jsonify({
        'image_url': image_url,
        'address': address,
        'chain_identifier': chain_identifier,
        'schema_name': schema_name,
        'description': description,
        'last_sale': last_sale,
        'rich_data': rich_data
    })

    # Save data to CSV file
    # with open('metadata.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Image URL', 'Address', 'Chain Identifier', 'Schema Name', 'Description', 'Last Sale', 'rich_data'])
    #     writer.writerow([image_url, address, chain_identifier, schema_name, description, last_sale, rich_data])

    # print("Data saved to metadata.csv file.")

