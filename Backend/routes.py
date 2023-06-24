import requests
from base64 import b64encode
from flask import render_template, redirect, url_for, flash, jsonify
from Backend import Backend



# The backend only has API based access from the frontend and does not have any
# HTML pages to render. The routes are defined here.

# API route to query the asset from the opensea API
# The API is called with the asset contract address and the token id
# The API returns a JSON object with the asset details

@Backend.route('/api/v1/get_asset/<contract_address>/<token_id>')
def get_asset(contract_address, token_id):
    url = 'https://api.opensea.io/api/v1/asset/' + contract_address + '/' + token_id + '/'

    headers = {
        'Accept': 'application/json',
        'X-API-KEY': '02d7d6fbe51f446681317e33e5bd7468',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        asset = data.get('asset', {})
        return jsonify(asset)
    else:
        return jsonify({'error': 'Error occurred'}), 400
