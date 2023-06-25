import re

# Read the Noun_data text file & split the data into a list of strings using the delimiter '///'
with open('Noun_data.txt', 'r') as file:
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

# We can use regex to extract the Noun and the values associated with it
# The regex pattern is: r'Noun (\d+)\nBorn(.*)\n→\n\nHead\n\n(.*)\n\n\nGlasses\n\n(.*)\n\n\nAccessory\n\n(.*)\n\n\nBody\n\n(.*)\n\n\nBackground\n\n'
# The pattern is explained below:
# Noun (\d+) : Noun followed by a space and then a number, which is captured using the brackets
# \nBorn(.*)\n→\n\nHead\n\n(.*)\n\n\nGlasses\n\n(.*)\n\n\nAccessory\n\n(.*)\n\n\nBody\n\n(.*)\n\n\nBackground\n\n :

def extract_values(text):
    pattern = r'Noun (\d+)\nBorn(.*)\n→\n\nHead\n\n(.*)\n\n\nGlasses\n\n(.*)\n\n\nAccessory\n\n(.*)\n\n\nBody\n\n(.*)\n\n\nBackground\n\n'
    result = re.findall(pattern, text)
    return result

data = {}
# parsing through the list - text of strings, and extracting the values using the extract_values function
for i in range(2, len(text)-1):
    result = extract_values(text[i])
    # storing the reuslt in a dictionary with the key being the Noun number - from the result[0][0]
    data[result[0][0]] = result[0][1:]

print(data)
