import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { ethers } from "ethers";
import { useScaffoldContract } from "~~/hooks/scaffold-eth";

const CONTRACT_ABI = useScaffoldContract("YourContract");
const CONTRACT_ADDRESS = useScaffoldContract("YourContract");

const DisplayNft = () => {
  const router = useRouter();
  const [contract, setContract] = useState(null);

  useEffect(() => {
    if (typeof window.ethereum !== "undefined") {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

      setContract(contract);
    } else {
      console.log("Metamask is not detected");
    }
  }, []);

  const mintNFT = async () => {
    if (!contract) return;

    const price = ethers.utils.parseEther("0.1"); // to convert eth to wei
    const transaction = await contract.createToken("https://cdn-icons-png.flaticon.com/512/747/747958.png", {
      value: price,
    });

    await transaction.wait(); // to wait until transaction is confirmed

    console.log("NFT minted!");
  };

  return (
    <div>
      <button onClick={mintNFT}>Mint NFT</button>
    </div>
  );
};

export default DisplayNft;
