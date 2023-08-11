import {ShiftTableProps} from "@/types";

export default function ShiftTable({ data }: ShiftTableProps) {
    return (
        <div>
            <h1 className="text-2xl font-semibold mb-4 text-center text-gray-900 dark:text-white">Shift Data</h1>
            <table className="min-w-full divide-y divide-gray-300 dark:divide-gray-600">
                <thead className="bg-gray-200 dark:bg-gray-700">
                <tr>
                    {['Employer ID', 'Employer Name', 'Start Shift', 'End Shift', 'Start Lunch', 'End Lunch'].map(header => (
                        <th key={header}
                            className="px-4 py-2 text-left text-xs font-medium text-gray-600 dark:text-gray-300 uppercase tracking-wider">{header}</th>
                    ))}
                </tr>
                </thead>
                <tbody className="bg-white dark:bg-gray-800">
                {data && data.length > 0 ? data.map((item) => (
                    <tr key={item.id} className="text-gray-900 dark:text-gray-200">
                        <td className="px-4 py-2">{item.employer_id}</td>
                        <td className="px-4 py-2">{item.employer.name || "N/A"}</td>
                        <td className="px-4 py-2">{item.start_shift}</td>
                        <td className="px-4 py-2">{item.end_shift}</td>
                        <td className="px-4 py-2">{item.start_lunch}</td>
                        <td className="px-4 py-2">{item.end_lunch}</td>
                    </tr>
                )) : null}
                </tbody>
            </table>
        </div>
    );
}