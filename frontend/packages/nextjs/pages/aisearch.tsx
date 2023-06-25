// Importing default layout from the index.tsx file:
//
import { NextPage } from "next";
import { MetaHeader } from "~~/components/MetaHeader";
import AiSearch from "~~/components/aisearch";

const AISearch: NextPage = () => {
  return (
    <>
      <MetaHeader title="AI Fetch | Scaffold-ETH" description="AI Fetch" />
      <AISearch />
    </>
  );
};

export default AiSearch;
