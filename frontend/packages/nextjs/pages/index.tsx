import Link from "next/link";
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, SparklesIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";

const Home: NextPage = () => {
  return (
    <>
      <MetaHeader />
      {/* <div class="bg-blue-500 text-white flex items-center justify-center h-220 w-full">
      <h1 class="text-4xl font-bold absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">A Shoe</h1>
      <img src="cover-photo.jpg" alt="Cover Photo" class="h-full w-full object-cover opacity-30" />
    </div> */}

      <div className="bg-black-500 text-white flex items-center justify-center h-220 w-full">
        <img src="bgImg/bb1.avif" alt="Cover Photo" className="h-full w-full object-cover opacity-80" />
        {/* <h1 className="text-8xl font-bold absolute transform left-1/2 -translate-x-1/2 -translate-y-1/2">AI Feature</h1> */}
      </div>

      <div className="flex items-center flex-col flex-grow pt-10">
        <div className="px-5">
          <h1 className="text-center mb-8">
            <span className="block text-2xl mb-2">Welcome to</span>
            <span className="block text-4xl font-bold">NFT Searcher</span>
          </h1>
        </div>
        <div className="flex-grow bg-base-300 w-full mt-16 px-8 py-12">
          <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
            <div className="flex flex-col bg-base-100 px-2 py-2 text-center items-center max-w-xs rounded-2xl">
              <img src="bgImg/bg1.avif" alt="Image 1" className="w-full h-auto rounded-2xl" />
            </div>
            <div className="flex flex-col bg-base-100 px-2 py-2 text-center items-center max-w-xs rounded-2xl">
              <img src="bgImg/bg2.webp" alt="Image 1" className="w-full h-auto rounded-2xl" />
            </div>
            <div className="flex flex-col bg-base-100 px-2 py-2 text-center items-center max-w-xs rounded-2xl">
              <img src="bgImg/bg3.webp" alt="Image 2" className="w-full h-auto rounded-2xl" />
            </div>
            <div className="flex flex-col bg-base-100 px-2 py-2 text-center items-center max-w-xs rounded-2xl">
              <img src="bgImg/bg4.svg" alt="Image 3" className="w-full h-auto rounded-2xl" />
            </div>
          </div>
        </div>
        
       
        <div className="flex-grow bg-base-300 w-full mt-16 px-8 py-12">
          <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
            <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
              <BugAntIcon className="h-8 w-8 fill-secondary" />
              <p>
                {" "}
                <Link href="/aifetch" passHref className="link">
                  AI Feature
                </Link>
               
              </p>
            </div>
            <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
              <SparklesIcon className="h-8 w-8 fill-secondary" />
              <p>
                {" "}
                <Link href="/aisearch" passHref className="link">
                AI Search 
                </Link>{" "}
            
              </p>
            </div>
            
            <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
            <SparklesIcon className="h-8 w-8 fill-secondary" />
              <p>
                 <Link href="/ngtbundle" passHref className="link">NFT Bundling</Link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
