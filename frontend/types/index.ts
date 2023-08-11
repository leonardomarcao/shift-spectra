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
    records: number;
    import_data: string;
    import_time: string;
    import_file: string;
};

export interface ShiftTableProps {
    data: any[];
}