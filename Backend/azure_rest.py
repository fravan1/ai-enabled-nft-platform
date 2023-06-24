import requests
import urllib.request
from base64 import b64encode
from PIL import Image
from io import BytesIO

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
        generated_data = process_image(image_data)
        print(generated_data)
    else:
        print("Error:", response.status_code, response.text)


get_asset('0x629A673A8242c2AC4B7B8C5D8735fbeac21A6205', '1270989104761746854939651153331927477999454739203555626306833872706963209653')

