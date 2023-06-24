// Importing default layout from the index.tsx file:
//
import { NextPage } from "next";
import { MetaHeader } from "~~/components/MetaHeader";
import { ContractUI } from "~~/components/scaffold-eth";

const AIFetch: NextPage = () => {
    return (
        <>
        <MetaHeader
            title="AI Fetch | Scaffold-ETH"
            description="AI Fetch"
        />
        <div className="flex flex-col gap-y-6 lg:gap-y-8 py-8 lg:py-12 justify-center items-center">
            <ContractUI
            contractName="AIFetch"
            className=""
            />
        </div>
        </>
    );
    }

export default AIFetch;