import React, { useState } from "react";
import Link from "next/link";
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, SparklesIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";

const NFTBUNDLE: NextPage = () => {
    const [char_address, setchar_address] = useState("");
    const [loading, setLoading] = useState(false);
    
    const [likeCount, setLikeCount] = useState(0);
    const [superLikeCount, setSuperLikeCount] = useState(0);
    const [countFund, setCountFund] = useState(0);
    const [dislikeCount, setDislikeCount] = useState(0);
    
    const handleLikeClick = () => {
        setLikeCount(likeCount + 1);
        handleCountFund(0);
    };
    const handleSuperLikeCount = () => {
        setSuperLikeCount(superLikeCount + 1);
        handleCountFund(0.001);
    };
    const handleDislikeClick = () => {
        setDislikeCount(dislikeCount + 1);
        handleCountFund(0);
    };
    const handleCountFund = (amt: number) => {
        setCountFund(countFund + amt);
        // Math.round(countFund * 10000000) / 10000000
    };


    return (
        <>
        <div className="mt-4 mx-auto">
                    <form className="flex">
                        <input type="text" name="address" placeholder="Char address" className="block w-64 appearance-none focus:outline-none bg-transparent border-b-2 border-blue-500" />
                        <button type="submit" className="ml-2 bg-blue-500 text-white px-4 py-2 rounded">Find</button>
                    </form>
                </div>
        <div className="grid grid-cols-4 mt-8 ">
          
                <div className="col-start-2 max-w-md mx-10 bg-white shadow-md rounded-lg overflow-hidden">
                    <div className="p-4">
                        {/* <!-- Image --> */}
                        <img src="bgImg/bg8.avif" alt="Image" className="w-full mb-4"/>

                        {/* <!-- Like/Dislike buttons --> */}
                        <div className="flex items-center justify-between mb-4 space-x-4">
                            
                            <button className="text-black py-2 px-3 rounded" onClick={handleLikeClick}>
                                <img src="like.png" alt="Like" className="max-w-[30px] max-h-[30px]"/>
                                <span>{likeCount}</span>
                            </button>
                            
                            <button className="text-black py-2 px-3 rounded" onClick={handleSuperLikeCount}>
                                <img src="super.png" alt="Super Like" className="max-w-[30px] max-h-[30px]"/>     
                                <span>{superLikeCount}</span>    
                            </button>
                            <button className="text-black py-2 px-3 rounded" onClick={handleDislikeClick}>
                                <img src="dislike.png" alt="Dislike" className="max-w-[30px] max-h-[30px]"/>
                                <span>{dislikeCount}</span>
                            </button>
                        </div>

                        
                        {/* <!-- Share button --> */}
                        <button className="bg-blue-500 text-white px-4 py-2 rounded mb-4">Share</button>

                        {/* <!-- Comment section --> */}
                        <textarea className="w-full h-20 p-2 border border-gray-300 text-black rounded mb-4" placeholder="Write a comment"></textarea>

                        {/* <!-- Post comment button --> */}
                        <button className="bg-blue-500 text-white px-4 py-2 rounded">Post Comment</button>
                    </div>
                </div>
                <div className="max-w-md mx-auto">
                    <div className="max-w-md mx-auto  bg-white shadow-md rounded-lg overflow-hidden">        
                        <div className="flex items-center justify-between mb-1 mt-2 space-x-4">
                            
                            <button className="text-black py-2 px-3 rounded" >
                                <img src="like.png" alt="Like" className="max-w-[30px] max-h-[30px]"/>
                                <span>{likeCount}</span>
                            </button>
                            
                            <button className="text-black py-2 px-3 rounded" >
                                <img src="super.png" alt="Super Like" className="max-w-[30px] max-h-[30px]"/>     
                                <span>{superLikeCount}</span>    
                            </button>
                            <button className="text-black py-2 px-3 rounded" >
                                <img src="dislike.png" alt="Dislike" className="max-w-[30px] max-h-[30px]"/>
                                <span>{dislikeCount}</span>
                            </button>
                        </div>                    
                    </div>
                    <br/>
                    <br/>
                   
                    <div className="max-w-md mx-auto h-20 bg-white shadow-md rounded-lg overflow-hidden">        
                        <table>
                            <tr>
                                <th className="text-black">Final Cost: </th>
                                <td></td>
                                <td className="text-black">{countFund.toFixed(3)} ETH</td>
                            </tr>
                            <tr >
                                <td><button className="bg-blue-500 text-white px-4 py-2 w-20 rounded ml-2 mt-2 mb-4">Buy</button></td>
                                <td></td>
                                <td><button className="bg-blue-500 text-white px-4 py-2 w-20 rounded ml-20 mt-2 mb-4 mr-3">Claim</button></td>   
                            </tr>
                            
                        </table>
                    </div>
                </div>     
            </div>
        </>
    );
  };


export default NFTBUNDLE;