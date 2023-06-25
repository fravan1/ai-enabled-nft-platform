# Fetching Live on-chain events using Substream API

import requests, json
from substreams import Substream

# Create a new Substream instance
substream = Substream()

# Create a new stream
stream = substream.create_stream()

# Setting up  the stream files
sb = Substream("substreams-uniswap-v2-v0.1.0.spkg")
print(sb.output_modules)