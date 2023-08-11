'use client'

import {useState, useEffect} from 'react';
import Link from 'next/link';
import {fetchImportGroupedData} from "@/services/api";
import {DataItem} from "@/types";


function ImportsList() {
    const [data, setData] = useState<DataItem[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchImportGroupedData()
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <div className="text-xl font-semibold text-center mt-10">Loading...</div>;
    if (error) return <div
        className="text-xl font-semibold text-center mt-10 text-red-600">Error: {error}</div>;


    return (
        <div className="bg-white dark:bg-gray-800 shadow-lg rounded-lg px-3 py-5 max-w-md mx-auto mt-10">
            <h1 className="text-2xl font-semibold mb-6 text-center">Imports Grouped by Month</h1>
            <ul>
                {data.map((item) => (
                    <li key={`${item.year}-${item.month}`}
                        className="border-b border-gray-200 dark:border-gray-600 py-2">
                        <span>Year: {item.year} - Month: {item.month} - Total: {item.total_records}</span>
                        <span> | </span>
                        <Link href="/shift/[year]/[month]/table" as={`/shift/${item.year}/${item.month}/table`}>
                            <button className="bg-blue-500 hover:bg-black text-white font-bold py-1 px-1 mx-1 rounded">
                                Table View
                            </button>
                        </Link>
                        <Link href="/shift/[year]/[month]/graph" as={`/shift/${item.year}/${item.month}/graph`}>
                            <button className="bg-blue-500 hover:bg-black text-white font-bold py-1 px-1 mx-1 rounded">
                                Graph View
                            </button>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );

}

export default ImportsList;
