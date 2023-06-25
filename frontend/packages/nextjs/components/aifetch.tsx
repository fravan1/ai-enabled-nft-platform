import React, { useState } from "react";
import Link from "next/link";
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, SparklesIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";

const AiFetch = () => {
  const [char_address, setchar_address] = useState("");
  const [token_id, settoken_id] = useState("");
  const [aiData, setAiData] = useState("");
  const [tableData, setTableData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [desc, setDesc] = useState("");
  const [owner, setOwner] = useState("");

  const jsonToTable = (data, className = "json-table") => {
    let table = document.createElement("table");
    table.className = `table-auto border-collapse w-full ${className}`;

    for (let key in data) {
      let row = document.createElement("tr");

      let keyCell = document.createElement("td");
      keyCell.appendChild(document.createTextNode(key));
      keyCell.className = "border border-black-300 px-4 py-2 text-black-600 font-bold";
      row.appendChild(keyCell);

      let valueCell = document.createElement("td");
      valueCell.className = "border border-black-300 px-4 py-2 text-black-600";
      if (typeof data[key] === "object" && data[key] !== null) {
        valueCell.appendChild(jsonToTable(data[key], "json-table-inner"));
      } else {
        valueCell.appendChild(document.createTextNode(data[key]));
      }
      row.appendChild(valueCell);

      table.appendChild(row);
    }

    return table;
  };
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch("/api/ai_query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ char_address, token_id }),
      });
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      console.log(data);
      setAiData(JSON.stringify(data, null, 2));
      setTableData(jsonToTable(data));
      setImageUrl(data.data.image_url); // Set image url
      setDesc(data.data.rich_data.Description); // Set rich_data.Description
      setOwner(data.data.owner_address);
      console.log(owner);
      // Set rich_data.Description
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <h1 className="text-6xl mx-auto font-bold mt-10">
        <span className="text-blue-600">AI</span> Search
      </h1>
      <div className="flex-grow  w-full mt-16 px-8 py-12">
        <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
          <form onSubmit={handleSubmit} className="flex flex-col gap-y-6 lg:gap-y-8">
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
              <label htmlFor="char_address">Char address</label>
              <input
                id="char_address"
                type="text"
                placeholder="Enter char address"
                value={char_address}
                onChange={e => setchar_address(e.target.value)}
                className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap text-black"
              />
            </div>
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
              <label htmlFor="token_id">Token ID</label>
              <input
                id="token_id"
                type="text"
                placeholder="Enter token ID"
                value={token_id}
                onChange={e => settoken_id(e.target.value)}
                className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap text-black"
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
          <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
            <SparklesIcon className="h-8 w-8 fill-secondary" />
            <p>
              {" "}
              <Link href={`https://xmtp.pages.dev/dm/${owner}`} passHref target="blank" className="link">
                Chat w/ {owner.slice(0, 6)}...{owner.slice(-6, -1)}
              </Link>{" "}
            </p>
          </div>
        </div>
      </div>

      <div className="flex-grow bg-base-300 w-full mt-16 px-8 py-12">
        <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
          <div className="flex flex-col bg-base-100 px-2 py-2 text-center items-center max-w-xs rounded-2xl">
            <img src={imageUrl} alt="Image 1" className="w-full h-auto rounded-2xl" />
            <br />
            <h2>{desc}</h2>
          </div>
        </div>
        <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
          {tableData && (
            <div className="flex flex-col gap-y-6 lg:gap-y-8">
              <br />
              <br />
              <div dangerouslySetInnerHTML={{ __html: tableData.outerHTML }} />
            </div>
          )}
          {error && <p className="text-red-500">{error}</p>}
        </div>
              
      </div>
    </>
  );
};

export default AiFetch;
