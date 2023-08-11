'use client'

import {useRouter} from 'next/router';
import {useState, useEffect} from 'react';
import ShiftGraph from "@pages/components/ShiftGraph";
import {fetchShiftGraphData} from "@/services/api";
import {DataPoint} from "@/types";

function MonthGraphDetails() {
    const [graphData, setGraphData] = useState<DataPoint[]>([]);
    const [selectedDay, setSelectedDay] = useState<string>('1');
    const router = useRouter();
    const {year, month} = router.query;

    useEffect(() => {
        if (year && month && selectedDay) {
            fetchShiftGraphData(year, month, selectedDay)
                .then(response => {
                    setGraphData(response);
                });
        }
    }, [year, month, selectedDay]);

    if (!router.isReady) return null;

    return (
        <div>
            <h1>Graph for Year: {year} - Month: {month}</h1>
            <label>
                Select Day:
                <select value={selectedDay} onChange={(e) => setSelectedDay(e.target.value)}>
                    {Array.from({length: 31}, (_, i) => i + 1).map(day => (
                        <option key={day} value={day}>{day}</option>
                    ))}
                </select>
            </label>
            <ShiftGraph data={graphData}/>
        </div>
    );
}

export default MonthGraphDetails;
