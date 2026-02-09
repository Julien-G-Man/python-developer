## My Python Tutorials

Collection of Python experiments, mini‑projects, and learning snippets I’ve written while practicing different areas of Python: core language features, data structures and algorithms, web frameworks, machine learning, computer vision, and modern LLM / RAG workflows.

This repo is meant to be a **playground** and **reference**: you can open any folder, run the script(s), and learn from small, focused examples.

### Repository layout

- **`data-structures/`**: Python fundamentals and classic data‑structure patterns.
  - Lists, tuples, sets, dictionaries, string methods, loops, file I/O, lambda functions, try/except, queues and stacks, insertion sort, merging and sorting utilities, and more.
- **`exercises/`**: Short coding challenges and practice problems.
  - Number games (even/odd, guessing, Fibonacci, palindromes, pass/fail), list and dict manipulation, random generators, simple simulations (dice, rock–paper–scissors), basic algorithms (frequency counts, filters), and more.
- **`oop/`**: Object‑oriented programming in Python.
  - Classes and objects, constructors and destructors, inheritance and polymorphism, encapsulation, access modifiers, static and class methods, and small domain examples like digital payments and banking.
- **`computer-vision/`**: Intro to computer vision with `opencv-python` and `face-recognition`.
  - Simple image operations (rotation, inversion), matrix operations, face detection and recognition using example images under `computer-vision/images/`.
- **`libraries/`**: How to use popular Python libraries.
  - `numpy`, `pandas`, `matplotlib.pyplot`, `seaborn`, `requests`, and `beautifulsoup4` examples for numerical computing, data analysis, plotting, HTTP calls, and HTML parsing.
- **`llm-apis/`**: Examples of calling AI / LLM related APIs.
  - Small scripts showing how to interact with services like OpenAI, AssemblyAI, Clarifai (and a Vercel API gateway), plus a note on counting tokens.
- **`frameworks/`**: Web framework examples.
  - **`fastapi-dir/`**: A tiny FastAPI app with a health‑check endpoint and a users endpoint (`/health`, `/users`) plus a `User` model in `models.py`.
  - **`django-projects/dictionary_project/`**: A Django project scaffold for a simple dictionary‑style app (`dictionary_app`) demonstrating views, models, and standard Django layout.
- **`machine-learning/`**
  - **`fastapi-ml-skeleton/`**: A small ML project skeleton.
    - `data/data.csv` – sample dataset.
    - `models/my_model.joblib` – pre‑trained model artifact.
    - `src/train.py` – training logic for creating the model.
    - `src/main.py` – FastAPI app exposing a `/predict` endpoint using Pydantic models.
    - `run.py` – helper script to launch Uvicorn (`main:app`).
- **`rag/`**
  - **`rag-app-main/`**: A tiny RAG demo cloned from `https://github.com/nileshhadalgi016/rag-app`.
    - `main.ipynb` – loads a PDF (e.g. `Think-And-Grow-Rich_2011-06.pdf`), chunks text, builds embeddings with LangChain + Ollama, stores in a vector store, and lets you query it.
    - `flow.tldr` – short notes about the RAG flow.
- **`leetcode/`**: A few problem‑style solutions (e.g. merging strings, making a string valid with minimal additions).
- **`random_trials/`**: Miscellaneous experiments and CLI toys.
  - Small utilities like calculators, password strength checker, factorials, recursion demos, GCD, inventory check, student management, substring/substring length logic, simple stats, and more.
- **`files/`**: Example CSV data sets (`finance_data.csv`, `wine_data.csv`) used by some scripts.
- **`rag-app-main/main.ipynb`**, sub‑READMEs, and other notebooks/scripts: additional, more focused demos inside individual subfolders (for example under `machine-learning/fastapi-ml-skeleton/` and `rag/rag-app-main/`).

### Getting started

- **Prerequisites**
  - Python **3.10+** installed.
  - Optional but recommended: a virtual environment tool (`venv`, `virtualenv`, `conda`, or similar).

- **Clone and set up**

```bash
git clone <your-fork-or-this-repo-url>
cd "My Python Tutorials"

# (optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# or Command Prompt
.venv\Scripts\activate.bat

# install dependencies used across the projects
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note**: Some folders (like `rag/rag-app-main/` or `machine-learning/fastapi-ml-skeleton/`) may have their own extra dependencies or specific version recommendations. Check their local `README.md` files or script comments if something fails to import.

### Running selected projects

- **Python basics, data structures, OOP, and exercises**
  - Most scripts in `data-structures/`, `oop/`, `exercises/`, and `random_trials/` can be run directly:

```bash
python path/to/script.py
# example
python exercises/number_guessing.py
python oop/classes_and_objects.py
python data-structures/Insertion\ Sort.py
```

- **FastAPI ML skeleton (`machine-learning/fastapi-ml-skeleton/`)**
  - From the repo root:

```bash
cd machine-learning/fastapi-ml-skeleton

# install local requirements if needed
pip install -r requirements.txt

# optional: (re)train or update the model
python src/train.py

# run the FastAPI app
python run.py
```

  - Once running, open `http://localhost:8000/docs` in your browser to explore the `/predict` endpoint via the automatically generated Swagger UI.

- **Simple FastAPI example (`frameworks/fastapi-dir/`)**
  - Inspect `frameworks/fastapi-dir/main.py` for a minimal app with `/health` and `/users` endpoints.
  - A typical way to run a FastAPI app is via Uvicorn:

```bash
uvicorn main:app --reload
```

  - Depending on how your Python path is configured, you may run this from inside `frameworks/fastapi-dir/` or via your IDE’s run/debug configuration.

- **Django dictionary project (`frameworks/django-projects/dictionary_project/`)**

```bash
cd frameworks/django-projects/dictionary_project
python manage.py migrate
python manage.py runserver
```

  - Then browse to `http://127.0.0.1:8000/` to see the project.

- **RAG demo (`rag/rag-app-main/`)**

  - This folder contains a Jupyter notebook `main.ipynb` that:
    - Loads `Think-And-Grow-Rich_2011-06.pdf`.
    - Chunks the text, generates embeddings (via LangChain + Ollama), and stores them in a vector store (e.g. Chroma).
    - Lets you query the document in a retrieval‑augmented‑generation style.

  - High‑level steps:

```bash
cd rag/rag-app-main

# create and activate a virtual environment (Python 3.11 recommended)
python -m venv .venv
.venv\Scripts\Activate.ps1  # on Windows PowerShell

pip install --upgrade pip
pip install chromadb langchain-community pypdf langchain-ollama

# start Jupyter
jupyter lab  # or: jupyter notebook
```

  - Open `main.ipynb` from Jupyter and run through the cells.

### LLM / external API examples

- The scripts under `llm-apis/` show how to:
  - Call **OpenAI** models via the `openai` Python client.
  - Use **AssemblyAI** for speech‑to‑text or related audio tasks.
  - Talk to **Clarifai** and a **Vercel**-hosted API gateway.
- For these examples you will typically need API keys set as environment variables or in a `.env` file (see script comments for the expected variable names). **Do not commit your keys** to version control.

### How to use this repo for learning

- **Pick a topic folder** that matches what you want to learn (e.g. `data-structures/`, `oop/`, `computer-vision/`, `libraries/`, `llm-apis/`, `machine-learning/`).
- **Open scripts in your editor**, read through them, and run them from the terminal.
- **Experiment**:
  - Change input values and edge cases.
  - Add new functions or classes.
  - Refactor scripts into modules or packages as you grow more comfortable.
- **Use it as a cookbook**: when you need a quick reminder on how to do something (read CSVs with `pandas`, make a quick plot, build a small API endpoint, or call an AI service), search this repository for a nearby example and adapt it.

Over time this repo can evolve into a personal **Python cookbook + playground** where you keep adding new experiments, notes, and mini‑projects as you learn more.
