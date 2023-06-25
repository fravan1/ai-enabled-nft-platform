import { useState } from "react";
import ERC721ABI from "../assets/ERC721_ABI.json";
import { ethers } from "ethers";

const provider = new ethers.providers.JsonRpcProvider(process.env.NEXT_PUBLIC_RPC_URL);

const DisplayNft = () => {
  const [nftAddress, setNftAddress] = useState("");
  const [nftData, setNftData] = useState(null);

  const fetchNftData = async () => {
    try {
      const nftContract = new ethers.Contract(nftAddress, ERC721ABI, provider);
      const name = await nftContract.name();
      const symbol = await nftContract.symbol();
      const totalSupply = await nftContract.totalSupply();
      const tokenId = 1694393;
      const tokenURI = await nftContract.tokenURI(tokenId);

      setNftData({ symbol, totalSupply, tokenURI });
      fetchMetadata(tokenURI);
    } catch (error) {
      console.error("Error fetching NFT data:", error);
    }
  };

  const fetchMetadata = async tokenURI => {
    try {
      const response = await fetch(tokenURI);
      const metadata = await response.json();
      console.log("Fetched metadata:", metadata); // Add this line
      setNftData(prevState => ({ ...prevState, metadata }));
    } catch (error) {
      console.error("Error fetching metadata:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={nftAddress}
        onChange={e => setNftAddress(e.target.value)}
        placeholder="Enter NFT address"
      />
      <button onClick={fetchNftData}>Fetch NFT</button>
      {nftData && (
        <div>
          <h3>
            {nftData.name} ({nftData.symbol})
          </h3>
          <p>Total Supply: {nftData.totalSupply.toString()}</p>
          {nftData.metadata && (
            <div>
              <h4>{nftData.metadata.title}</h4>
              <img src={nftData.metadata.imageUrl} alt={nftData.metadata.title} width="300" />
              <p>{nftData.metadata.info}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default DisplayNft;
