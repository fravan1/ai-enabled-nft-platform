// Component to render the form with two input fields, namely Char_address and token_id,
// and a button to fetch the data from the /api/ai_query endpoint
// and display the json response in a textarea
import React, { useState } from "react";

const AiFetch = () => {
    const [charAddress, setCharAddress] = useState("");
    const [tokenId, setTokenId] = useState("");
    const [aiData, setAiData] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);
        try {
        const res = await fetch("/api/ai_query", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({ charAddress, tokenId }),
        });
        const data = await res.json();
        setAiData(JSON.stringify(data, null, 2));
        } catch (error) {
        setError(error.message);
        } finally {
        setLoading(false);
        }
    };
    
    return (
        <div className="flex flex-col gap-y-6 lg:gap-y-8 py-8 lg:py-12 justify-center items-center">
        <form onSubmit={handleSubmit} className="flex flex-col gap-y-6 lg:gap-y-8">
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
            <label htmlFor="charAddress">Char address</label>
            <input
                id="charAddress"
                type="text"
                placeholder="Enter char address"
                value={charAddress}
                onChange={e => setCharAddress(e.target.value)}
                className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap"
            />
            </div>
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
            <label htmlFor="tokenId">Token ID</label>
            <input
                id="tokenId"
                type="text"
                placeholder="Enter token ID"
                value={tokenId}
                onChange={e => setTokenId(e.target.value)}
                className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap"
            />
            </div>
            <button
            type="submit"
            className="btn btn-secondary btn-sm normal-case font-thin bg-base-300"
            disabled={loading}
            >
            {loading ? "Loading..." : "Fetch AI data"}
            </button>
        </form>
        {aiData && (
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
            <label htmlFor="aiData">AI data</label>
            <textarea
                id="aiData"
                value={aiData}
                readOnly
                className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap"
            />
            </div>
        )}
        {error && <p className="text-red-500">{error}</p>}

        </div>
    );
    }

export default AiFetch;

