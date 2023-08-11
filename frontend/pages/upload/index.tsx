// pages/upload.tsx

import ClientFileUpload from "@/pages/components/ClientFileUpload";

export default function UploadPage() {

    return (
        <div className="relative flex place-items-center">
            <h1>Upload Files</h1>
            <ClientFileUpload/>
        </div>
    );
}
