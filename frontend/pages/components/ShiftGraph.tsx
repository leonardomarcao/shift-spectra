import React from 'react';
import {BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid} from 'recharts';
import {ShiftGraphProps} from "@/types";


const ShiftGraph: React.FC<ShiftGraphProps> = ({data}) => {
    return (
        <BarChart
            width={800}
            height={500}
            data={data}
            margin={{top: 20, right: 30, left: 20, bottom: 5}}
        >
            <CartesianGrid strokeDasharray="3 3"/>
            <XAxis dataKey="time"/>
            <YAxis/>
            <Tooltip/>
            <Bar dataKey="count" fill="#8884d8"/>
        </BarChart>
    );
};

export default ShiftGraph;
