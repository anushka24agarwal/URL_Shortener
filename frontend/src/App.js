import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url, setUrl] = useState("");
  const [shortened, setShortened] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setShortened("");

    if (!url.trim()) {
      setError("Please enter a valid URL.");
      return;
    }

    try {
      const res = await axios.post("/shorten", { url });
      setShortened(`http://127.0.0.1:8000/${res.data.short_code}`);
    } catch (err) {
      setError("Failed to shorten URL. Try again.");
    }
  };

  return (
    <div className="container">
      <h1>🔗 URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter a long URL (e.g. https://google.com)"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button type="submit">Shorten</button>
      </form>

      {error && <p className="error">{error}</p>}

      {shortened && (
        <div className="result">
          <p>✅ Short URL:</p>
          <a href={shortened} target="_blank" rel="noreferrer">
            {shortened}
          </a>
        </div>
      )}
    </div>
  );
}

export default App;
