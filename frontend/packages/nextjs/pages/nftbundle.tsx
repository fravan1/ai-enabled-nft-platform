// Importing default layout from the index.tsx file:
//
import { NextPage } from "next";
import { MetaHeader } from "~~/components/MetaHeader";
import NFTBUNDLE from "../components/nftbundle_component";

const NFTBundle: NextPage = () => {
  return (
    <>
      <MetaHeader title="AI Fetch | Scaffold-ETH" description="AI Fetch" />
      <NFTBUNDLE />
    </>
  );
};

export default NFTBundle;