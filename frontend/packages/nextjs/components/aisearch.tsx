import { useState } from "react";
import axios from "axios";

const AiSearch = () => {
  const [keyword, setKeyword] = useState("");
  const [data, setData] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`https://api.yourwebsite.com/search?keyword=${keyword}`);
      setData(response.data);
    } catch (error) {
      console.error("Error occurred:", error);
    }
  };

  return (
    <div className="p-8">
      <div className="mb-6 flex">
        <input
          type="text"
          placeholder="Search"
          value={keyword}
          onChange={e => setKeyword(e.target.value)}
          className="w-full p-2 border-2 border-gray-300 rounded-md text-black mr-2"
        />
        <button onClick={handleSearch} className="px-4 py-2 bg-blue-500 text-white rounded-md">
          Search
        </button>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {data.length > 0
          ? data.map((item, index) => (
              <a href="#" key={index}>
                <div className="p-4 border-2 border-gray-200 rounded-md">
                  {/* Render your card data here. For example: */}
                  <h2 className="text-xl font-bold">{item.title}</h2>
                  <p className="mt-2">{item.description}</p>
                </div>
              </a>
            ))
          : [...Array(9)].map((_, index) => (
              <a href="#" key={index}>
                <div className="p-4 border-2 border-gray-200 rounded-md">
                  {/* Render your card data here. For example: */}
                  <h2 className="text-xl font-bold">Card {index + 1}</h2>
                  <p className="mt-2">This is a dummy card.</p>
                </div>
              </a>
            ))}
      </div>
    </div>
  );
};

export default AiSearch;
