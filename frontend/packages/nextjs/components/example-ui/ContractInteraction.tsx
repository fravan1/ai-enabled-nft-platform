import React, { useEffect, useState } from "react";
// Add this line to import Alchemy
import { CopyIcon } from "./assets/CopyIcon";
import { DiamondIcon } from "./assets/DiamondIcon";
import { HareIcon } from "./assets/HareIcon";
import { Alchemy, Network } from "alchemy-sdk";
import { ArrowSmallRightIcon, XMarkIcon } from "@heroicons/react/24/outline";

export const ContractInteraction = () => {
  const [visible, setVisible] = useState(true);
  const [newGreeting, setNewGreeting] = useState("");
  const [nfts, setNfts] = useState([]);

  useEffect(() => {
    const getNfts = async () => {
      const config = {
        apiKey: process.env.ALCHEMY_API_KEY,
        network: Network.ETH_MAINNET,
      };
      const alchemy = new Alchemy(config);
      const ownerNfts = await alchemy.nft.getNftsForOwner("ownerAddress");
      setNfts(ownerNfts.ownedNfts);
    };

    getNfts();
  }, []);

  const writeAsync = async () => {
    // Implement your write logic here
  };

  return (
    <div className="flex bg-base-300 relative pb-10">
      <DiamondIcon className="absolute top-24" />
      <CopyIcon className="absolute bottom-0 left-36" />
      <HareIcon className="absolute right-0 bottom-24" />
      <div className="flex flex-col w-full mx-5 sm:mx-8 2xl:mx-20">
        <div className="flex flex-col mt-6 px-7 py-8 bg-base-200 opacity-80 rounded-2xl shadow-lg border-2 border-primary">
          <span className="text-4xl sm:text-6xl text-black">NFT Name</span>
          <div className="mt-8 flex flex-col sm:flex-row items-start sm:items-center gap-2 sm:gap-5">
            <input
              type="text"
              placeholder="NFT Contract Address"
              className="input font-bai-jamjuree w-full px-5 bg-[url('/assets/gradient-bg.png')] bg-[length:100%_100%] border border-primary text-lg sm:text-2xl placeholder-white uppercase"
              onChange={e => setNewGreeting(e.target.value)}
            />
            <div className="flex rounded-full border border-primary p-1 flex-shrink-0">
              <div className="flex rounded-full border-2 border-primary p-1">
                <button
                  className={`btn btn-primary rounded-full capitalize font-normal font-white w-30 flex items-center gap-1 hover:gap-2 transition-all tracking-widest ${
                    isLoading ? "loading" : ""
                  }`}
                  onClick={writeAsync}
                >
                  {!isLoading && (
                    <>
                      Display <ArrowSmallRightIcon className="w-3 h-3 mt-0.5" />
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* <NFTDisplay /> */}
    </div>
  );
};
