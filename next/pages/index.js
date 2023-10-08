import Head from "next/head";
import { useState } from "react";
import styles from "./index.module.css";

export default function Home() {
  const [result, setResult] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);

  // Function to handle file input change
  function handleFileInputChange(event) {
    setSelectedFile(event.target.files[0]);
  }

  async function onSubmit(event) {
    event.preventDefault();

    try {
      // Check if a file has been selected
      if (!selectedFile) {
        throw new Error("Please select a PDF file.");
      }

      // You can add additional form data here if needed
      const formData = new FormData();

      formData.append("file", selectedFile);

      // Make an API request to send the form data
      const response = await fetch("/api/upload", {
        method: "POST", // Change to your API endpoint and HTTP method
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      // Handle a successful response here, if needed
      // For example, you can display a success message to the user
      setResult("File uploaded successfully");

    } catch (error) {
      // Handle errors here
      console.error(error);
      alert(error.message);
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>OpenAI Morgan</title>
        <link rel="icon" href="/favicon.png" />
      </Head>
      <div className={styles.topbar}>
        <img className={styles.logo} src="/morgan.png" alt="Logo" />
      </div>

      <div className={styles.infoBox}>
        <div className={styles.scrollBox}>
          <div className={styles.title}>CASES</div>
          <ul className={styles.caseList}>
            <li className={styles.case}>Case Number 1</li>
            <li className={styles.case}>Case Number 2</li>
            <li className={styles.case}>Case Number 3</li>
            <li className={styles.case}>Case Number 4</li>
            <li className={styles.case}>Case Number 5</li>
            {/* Your case list items */}
          </ul>
        </div>

        {/* Wrap your elements in a form element */}
       
          <textarea
            className={styles.userInput}
            type="text"
            placeholder="Send A Message"
            name="userinput"
          />
          <form onSubmit={onSubmit}>
          <div className={styles.uploadSection}>
            {/* Add a label or button to trigger the file input */}
            <label className={styles.uploadButton}>
              Upload PDF
              <input
                type="file"
                accept=".pdf"
                onChange={handleFileInputChange}
                style={{ display: "none" }}
              />
            </label>
            {selectedFile && (
              <p className={styles.p}>Selected File: {selectedFile.name}</p>
            )}
            {result && <p className={styles.p}>Uploaded File: {result}</p>}
            <button type="submit">Submit</button>
          </div>
        </form>
      </div>
    </div>
  );
}
