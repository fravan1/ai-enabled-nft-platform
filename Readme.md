# Readme File: How to Work with the Code

## Introduction

This readme file provides instructions on how to work with the code for the Discovia platform. The platform takes NFTs, which are images on ERC-721 queried with the graph substream, and parses them through computer vision technology to identify image-specific attributes. It then creates an index table for each NFT, which is stored on the IPFS chain. This gives a richer database of each NFT that will provide premium search results.

## Installation

To get started with the code, follow these installation steps:

1. Clone the repository and install dependencies:

```
git clone https://github.com/Rutvikrj26/ETHWaterloo.git
cd ETHWaterloo
yarn install
```

2. Run a local network in the first terminal:

```
yarn chain
```

This command starts a local Ethereum network using Hardhat. The network runs on your local machine and can be used for testing and development. You can customize the network configuration in `hardhat.config.ts`.

3. Deploy the test contract in the second terminal:

```
yarn deploy
```

This command deploys a test smart contract to the local network. The contract is located in `packages/hardhat/contracts` and can be modified to suit your needs. The `yarn deploy` command uses the deploy script located in `packages/hardhat/deploy` to deploy the contract to the network. You can also customize the deploy script.

4. Start the NextJS app in the third terminal:

```
yarn start
```

Visit your app at `http://localhost:3000`. You can interact with your smart contract using the contract component or the example UI in the frontend. You can tweak the app config in `packages/nextjs/scaffold.config.ts`.


To run the servers for the backend and get the website running on the browser, follow these steps:

1. Backend Server:
   - Open a terminal and navigate to the backend directory of the code.
   - Type the following command to start the backend server:
     ```
     python run_Backend.py
     ```

2. Frontend Server:
   - Open a new terminal and navigate to the frontend directory of the code.
   - Install the required dependencies by running the following command:
     ```
     yarn install
     ```
   - Once the dependencies are installed, start the frontend server by running the command:
     ```
     yarn start
     ```

3. Accessing the Website:
   - Open a web browser and visit `http://localhost:3000`.
   - The website should be live and accessible at this URL.

Note: Make sure both the backend and frontend servers are running simultaneously. The backend server can be started using the `python run_Backend.py` command, while the frontend server can be started using `yarn start`.
