'use client'

import { useRouter } from 'next/router';
import { useState, useEffect } from 'react';
import ShiftTable from "@/pages/components/ShiftTable";
import { fetchShiftsForMonth } from "@/services/api";

function MonthTableDetails() {
    const [data, setData] = useState([]);
    const router = useRouter();
    const { year, month } = router.query;

    useEffect(() => {
        if (year && month) {
            fetchShiftsForMonth(year, month)
                .then(response => {
                    setData(response);
                });
        }
    }, [year, month]);

    if (!router.isReady) return null;

    return (
        <div>
            <h1>Details for Year: {year} - Month: {month}</h1>
            <ShiftTable data={data} />
        </div>
    );
}

export default MonthTableDetails;
