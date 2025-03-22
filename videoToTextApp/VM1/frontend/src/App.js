import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [video, setVideo] = useState(null);
    const [result, setResult] = useState("");
    const [progress, setProgress] = useState(false);

    const uploadVideo = async () => {
        const formData = new FormData();
        formData.append("video", video);
        setProgress(true);
        const res = await axios.post("http://localhost:5000/upload", formData);
        setResult(res.data.transcription);
        setProgress(false);
    };

    return (
        <div>
            <h2>Video to Text</h2>
            <input type="file" onChange={(e) => setVideo(e.target.files[0])} />
            <button onClick={uploadVideo}>Upload</button>
            {progress && <p>Processing...</p>}
            <pre>{result}</pre>
        </div>
    );
}

export default App;