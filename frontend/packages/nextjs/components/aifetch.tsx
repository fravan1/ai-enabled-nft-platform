import React, { useState } from "react";

const AiFetch = () => {
  const [char_address, setchar_address] = useState("");
  const [token_id, settoken_id] = useState("");
  const [aiData, setAiData] = useState("");
  const [tableData, setTableData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

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
      const data = await res.json();
      setAiData(JSON.stringify(data, null, 2));
      setTableData(jsonToTable(data));
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
        <button type="submit" className="btn btn-secondary btn-sm normal-case font-thin bg-base-300" disabled={loading}>
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
            className="w-full max-w-7xl pb-1 px-6 lg:px-10 flex-wrap text-black textarea-large"
          />
        </div>
      )}
      {tableData && (
        <div className="flex flex-col gap-y-6 lg:gap-y-8">
          <label htmlFor="aiData">AI data table</label>
          <div dangerouslySetInnerHTML={{ __html: tableData.outerHTML }} />
        </div>
      )}
      {error && <p className="text-red-500">{error}</p>}
    </div>
  );
};

export default AiFetch;
