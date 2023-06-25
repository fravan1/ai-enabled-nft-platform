import React, { useEffect, useState } from "react";
import { Alchemy, Network } from "alchemy-sdk";

const NftDisplay = () => {
  const [nftList, setNftList] = useState([]);

  useEffect(() => {
    const fetchNFTs = async () => {
      const settings = {
        apiKey: "YOUR_ALCHEMY_API_KEY",
        network: Network.ETH_MAINNET,
      };

      const alchemy = new Alchemy(settings);
      const owner = "vitalik.eth";
      const fetchedNFTs = await alchemy.nft.getNftsForOwner(owner);
      setNftList(fetchedNFTs["ownedNfts"]);
    };

    fetchNFTs();
  }, []);

  return (
    <div>
      {nftList.map((nft, index) => (
        <div key={index}>
          <h3>{nft.title}</h3>
          {/* Add other relevant fields here */}
        </div>
      ))}
    </div>
  );
};

export default NftDisplay;
