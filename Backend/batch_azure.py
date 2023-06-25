import requests
import urllib.request
import csv

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

    # Save data to CSV file
    with open('metadata.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image URL', 'Address', 'Chain Identifier', 'Schema Name', 'Description', 'Last Sale', 'rich_data'])
        writer.writerow([image_url, address, chain_identifier, schema_name, description, last_sale, rich_data])

    print("Data saved to metadata.csv file.")

# going through all the assets in the collection & calling the get_asset() function for each asset
def get_all_assets():
    for i in range(1, 10):
        get_asset('0x495f947276749ce646f68ac8c248420045cb7b5e', str(i))


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
