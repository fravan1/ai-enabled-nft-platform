import { config } from "hardhat";
import { ethers, Wallet } from "ethers";

async function main() {
  const privateKey = process.env.DEPLOYER_PRIVATE_KEY;

  if (!privateKey) {
    console.log("🚫️ You don't have a deployer account. Run `yarn generate` first");
    return;
  }

  // Get account from private key.
  const wallet = new Wallet(privateKey);
  const nftAddress = wallet.address;



  const tokenboundClient = new TokenboundClient({ signer, chainId: 1 });
 
  const tokenBoundAccount = tokenboundClient.getAccount({
    tokenContract: nftAddress,
    tokenId: 129343,
  });
 
console.log(tokenBoundAccount); //0

  // Balance on each network
  const availableNetworks = config.networks;
  for (const networkName in availableNetworks) {
    try {
      const network = availableNetworks[networkName];
      if (!("url" in network)) continue;
      const provider = new ethers.providers.JsonRpcProvider(network.url);
      const tokenBoundAccount = tokenboundClient.getAccount({
      tokenContract: nftAddress,
      tokenId: 129343,
    });
 
      console.log(tokenBoundAccount);
     
      
    } catch (e) {
      console.log("Can't connect to network", networkName);
    }
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
