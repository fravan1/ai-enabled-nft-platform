// Frontend form to submit a search query to the backend:
// recieves a list of 10 json objects to be displayed in a grod format.
import React, { useState } from "react";
import Link from "next/link";
import type { NextPage } from "next";
import { MetaHeader } from "~~/components/MetaHeader";

const AiSearch = () => {
  const [search_query, setSearchQuery] = useState("");
  const [aiData, setAiData] = useState([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch("/api/ai_search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ search_query }),
      });
      const data = await res.json();
      console.log(data);
      setAiData(Array.isArray(data) ? data : [data]);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <MetaHeader title="AI Search" />
      <div className="flex flex-col items-center justify-center min-h-screen py-2">
        <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
          <div className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
            <h1 className="text-6xl font-bold">
              <span className="text-blue-600">AI</span> Search
            </h1>
            <p className="mt-3 text-2xl">Search for a token by its attributes.</p>
            <form
              className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center"
              onSubmit={handleSubmit}
            >
              <input
                className="border border-black-300 rounded-md px-4 py-2 m-2 w-1/2"
                type="text"
                name="search_query"
                placeholder="Search Query"
                value={search_query}
                onChange={e => setSearchQuery(e.target.value)}
              />
              <button className="border border-black-300 rounded-md px-4 py-2 m-2 w-1/2" type="submit">
                Search
              </button>
            </form>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}
            {aiData.length > 0 && (
              <div className="grid grid-cols-3 gap-4">
                {aiData.map((item, index) => (
                  <div key={index} className="p-4 border-2 border-gray-200 rounded-md">
                    <h2 className="text-xl font-bold">Item {index + 1}</h2>
                    <p className="mt-2">Description: {item.Description}</p>
                    <p className="mt-2">Born: {item.Born}</p>
                    <p className="mt-2">Body: {item.Body}</p>
                    <p className="mt-2">Head: {item.Head}</p>
                    <p className="mt-2">Glasses: {item.Glasses}</p>
                    <p className="mt-2">Accessory: {item.Accessory}</p>
                    <p className="mt-2">Noun: {item.Noun}</p>
                    <p className="mt-2">Categories: {item.Categories}</p>
                    {item.Tags &&
                      item.Tags.map((tag, i) => (
                        <p key={i} className="mt-2">
                          Tag: {tag.name} - Confidence: {tag.confidence}
                        </p>
                      ))}
                  </div>
                ))}
              </div>
            )}
          </div>
        </main>
      </div>
    </>
  );
};

export default AiSearch;
