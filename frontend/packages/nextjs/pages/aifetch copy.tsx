// Importing default layout from the index.tsx file:
//
import { NextPage } from "next";
import { MetaHeader } from "~~/components/MetaHeader";
import AiFetch from "~~/components/aifetch";

const AIFetch: NextPage = () => {
  return (
    <>
      <MetaHeader title="AI Fetch | Scaffold-ETH" description="AI Fetch" />
      <AiFetch />
    </>
  );
};

export default AIFetch;
