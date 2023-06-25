import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = "https://nouns.wtf/explore"  # Replace with the URL of the webpage you want to parse
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.content, "html.parser")

token_dict = {}

relevant_dom = []

# Parse the HTML to find all the <p>, <span>, <strong>, and <h2> tags & store them in a list
for tag in soup.find_all(["p", "span", "strong", "h2"]):
    relevant_dom.append(tag)