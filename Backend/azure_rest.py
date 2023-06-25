import requests
import urllib.request


# Azure Cognitive Services API endpoint and key
endpoint = "https://waterlootest.cognitiveservices.azure.com/vision/v3.2/analyze"
api_key = "d5833954c09b4fe38ec2463ab4078218"
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
    breakpoint()
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
        # Storing the generated data in a text file
        with open('data.txt', 'w') as outfile:
            outfile.write(str(generated_data))
    else:
        print("Error:", response.status_code, response.text)


get_asset('0x629A673A8242c2AC4B7B8C5D8735fbeac21A6205', '1270989104761746854939651153331927477999454739203555626306833872706963209653')

# Uploading each new text file generated from the json dump of get_asset() to IPFS Storage
# using the base API : https://api.web3.storage/

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
        print(response.json())  # Access the response body
    else:
        print(f'Request failed with status code {response.status_code}')
        print(response.text)  # Access the error message if available


with open('data.txt', 'rb') as f:
    upload_file(f)
