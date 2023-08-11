export interface DataPoint {
  time: string;
  count: number;
}

export interface ShiftGraphProps {
  data: DataPoint[];
}

export type DataItem = {
    year: number;
    month: number;
    total_records: number;
};

export interface ShiftTableProps {
    data: any[];
}