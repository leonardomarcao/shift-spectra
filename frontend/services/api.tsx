const BASE_URL = 'http://localhost:8000/api/v1';

export const uploadFiles = async (files: File[]) => {
    const formData = new FormData();
    files.forEach((file, index) => {
        formData.append(`files`, file);
    });

    const response = await fetch(`${BASE_URL}/shift/upload`, {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    return response.json();
};

export const fetchImportGroupedData = async () => {
    const response = await fetch(`${BASE_URL}/shift/grouped-by-month`);
    return response.json();
}

export const fetchShiftsForMonth = async (year: string | string[], month: string | string[]) => {
    const response = await fetch(`${BASE_URL}/shift/by-month/${year}/${month}`);
    if (!response.ok) {
        throw new Error('Failed to fetch shift data');
    }
    return response.json();
}

export const fetchShiftGraphData = async (year: string | string[], month: string | string[], day: string | string[]) => {
    const response = await fetch(`${BASE_URL}/shift/graph/${year}/${month}/${day}`);

    if (!response.ok) {
        throw new Error('Failed to fetch shift graph data');
    }

    return response.json();
}
