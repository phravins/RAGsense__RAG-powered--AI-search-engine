# RAGsense: RAG powered AI Search Engine

![RAGsense Logo](logo.jpg)

RAGsense is a RAG powered AI search engine that allows you to ask questions about the content of any web page you are currently visiting. It combines a Chrome Extension with a  Python backend powered by Retrieval-Augmented Generation (RAG).
Built with 100 % open-source stack: **LangChain**, **RAG**, **Hugging-Face** embeddings + small LLM, **FAISS** vector store, and a tiny **Manifest-V3 Chrome extension*

## 🚀 Features

-   **Local Intelligence**: Uses `google/flan-t5-small` and `sentence-transformers` running entirely on your CPU. No data leaves your machine (unless you deploy the backend).
-   **Instant Answers**: Ask questions about the current tab's content and get immediate, context-aware answers.
-   **RAG Pipeline**: Built with [LangChain](https://www.langchain.com/) and [FAISS](https://github.com/facebookresearch/faiss) for efficient document retrieval and answering.
-   **Chrome Extension**: Seamless integration with your browsing experience.


## 📋 Prerequisites

-   Python 3.10 or higher
-   Google Chrome (or Chromium-based browser)

## 📦 Installation

### 1. Backend Setup

The backend handles the scraping, embedding, and question-answering.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd RAGsense
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Start the server:**
    ```bash
    python backend/main.py
    ```
    The server will start at `http://0.0.0.0:8000`.

### 2. Chrome Extension Setup

The extension allows you to interact with the backend from your browser.

1.  **Configure the Backend URL:**
    -  Open `chrome-extension/popup.js`.
    -  Find the line:
        ```javascript
        const BACKEND = "https://ai-search-engine-abc123-4567.app.github.dev";
        ```
    -   Change it to your local server URL (or deployed URL):
        ```javascript
        const BACKEND = "http://localhost:8000";
        ```

2.  **Load the Extension:**
    -   Open Chrome and navigate to `chrome://extensions`.
    -   Enable **Developer mode** (toggle in the top right).
    -   Click **Load unpacked**.
    -   Select the `chrome-extension` folder from this project.

## 💡 Usage

1.  Ensure the backend server is running (`python backend/main.py`).
2.  Open any web page in Chrome (e.g., a news article or documentation).
3.  Click the **RAGsense** extension icon in the toolbar.
4.  Type your question in the input box (e.g., "What is the main summary of this article?").
5.  Click **Ask**.
6.  The AI will read the page content and provide an answer based on the text.

## 📁 Project Structure

```
RAGsense/
├── backend/
│   ├── main.py           # FastAPI application entry point
│   ├── rag_chain.py      # RAG logic (Embeddings, LLM, Vector Store)
│   └── requirements.txt  # Python dependencies
└── chrome-extension/
    ├── manifest.json     # Extension configuration
    ├── popup.html        # Extension UI
    ├── popup.js          # Extension logic
    ├── content.js        # Content script
    └── icons/            # Extension icons
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

AUTHOR: [Phravins](https://github.com/phravins)

RAGsense - MIT licenced
