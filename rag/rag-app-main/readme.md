Cloned from https://github.com/nileshhadalgi016/rag-app

pip install langchain-community pypdf

pip install -qU langchain-ollama

Local Python 3.11 virtualenv (recommended)

## rag-app

Small RAG demo that loads a PDF, chunks it, generates embeddings via Ollama, and stores them in a vector store.

Files
- `main.ipynb` — example notebook (load PDF, chunk, embed, store, query)
- `flow.tldr` — short notes

Prerequisites
- macOS with Python 3.11 installed (recommended). The repo originally used a `.venv` with Python 3.14 which is incompatible with `chromadb`.

Quick start (recommended — Python 3.11)

```bash
# create and activate a Python 3.11 venv in the project
python3.11 -m venv .venv311
source .venv311/bin/activate

# upgrade pip and install required packages
pip install -U pip setuptools wheel
pip install -qU chromadb langchain-community pypdf langchain-ollama
```

Run the notebook

```bash
# start Jupyter and open `main.ipynb`
jupyter lab    # or `jupyter notebook`
```

Notes
- The notebook uses a Chroma-backed vector store by default and persists data to `./chroma_langchain_db`.
- If you cannot use Python 3.11, you can switch to FAISS (works on newer Pythons) by installing `faiss-cpu` and updating the notebook to import `FAISS` from `langchain.vectorstores`.

If you want, I can:
- activate `.venv311` and run the notebook cells here, or
- update `main.ipynb` to use FAISS instead of Chroma so it works with your current `.venv`.

