import React, {useState, useEffect} from "react";
import {uploadFiles} from "@/services/api";

const FileUpload: React.FC = () => {
    const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
    const [progress, setProgress] = useState<number>(0);
    const [message, setMessage] = useState<string>("");
    const [fileInfos, setFileInfos] = useState<string[]>([]);

    const selectFiles = (event: React.ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files as FileList;
        setSelectedFiles(Array.from(files));
        setProgress(0);
    };

    const upload = async () => {
        setProgress(0);

        if (!selectedFiles.length) return;

        try {
            const responses = await Promise.all(selectedFiles.map(file => uploadFiles([file])));
            setMessage("Files uploaded successfully!");
            setFileInfos(prevFiles => [...prevFiles, ...responses.map(res => res.filename)]);
        } catch (error) {
            setMessage(`Failed to upload files: ${(error as Error).message}`);
        }

        setSelectedFiles([]);
    };

    return (
        <div className="space-y-4">
            <div className="flex space-x-4 items-center">
                <div className="flex space-x-4 items-center">
                    <input
                        type="file"
                        accept=".csv, .xls, .xlsx"
                        onChange={selectFiles}
                        multiple
                        className="px-2 py-1 border rounded"
                    />
                    <button
                        className="px-4 py-2 bg-blue-500 text-white rounded disabled:opacity-50"
                        disabled={!selectedFiles.length}
                        onClick={upload}
                    >
                        Upload
                    </button>
                </div>
            </div>

            {progress > 0 && (
                <div className="relative pt-1">
                    <div className="flex mb-2 items-center justify-between">
                        <div>
              <span
                  className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blue-600 bg-blue-200">
                {progress}%
              </span>
                        </div>
                    </div>
                    <div className="overflow-hidden h-2 mb-4 text-xs flex rounded bg-blue-200">
                        <div
                            style={{width: progress + "%"}}
                            className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500"
                        ></div>
                    </div>
                </div>
            )}

            {message && (
                <div className="alert mt-3 p-4 bg-gray-200 text-gray-700 rounded">
                    {message}
                </div>
            )}

            {fileInfos.length > 0 && (
                <div className="mt-3 p-4 border rounded space-y-4">
                    <div className="font-semibold">List of Uploaded Files</div>
                    <ul>
                        {fileInfos.map((filename, index) => (
                            <li key={index} className="text-blue-500 hover:underline">
                                {filename}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default FileUpload;