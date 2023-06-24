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
    url = 'https://api.opensea.io/api/v1/asset/' + contract_address + '/' + token_id + '/'

    headers = {
        'Accept': 'application/json',
        'X-API-KEY': '02d7d6fbe51f446681317e33e5bd7468',
    }

    # Send the REST request to get the Asset's Image URL
    response = requests.get(url, headers=headers)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        image_url = data['image_url']
        # download the image & call the convert_to_binary function
        image_data = urllib.request.urlopen(image_url).read()
        return process_image(image_data)
    else:
        return("Error:", response.status_code, response.text)

