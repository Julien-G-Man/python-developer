## Yo Python Devs 🐍

Collection of Python experiments, mini‑projects, and learning snippets I’ve written while practicing different areas of Python: core language features, data structures and algorithms, web frameworks, machine learning, computer vision, and modern LLM / RAG workflows.

This repo is meant to be a **playground** and **reference**: you can open any folder, run the script(s), and learn from small, focused examples.
A lof of what you'll see here will be code I wrote during my early days of learning Python, so you'll definitely see variations cos I've been putting everything here since I began learning   Python till date, including my first helloworld("print") :)

### 📁 Project structure

```text
python-practice/
├── README.md                         # This file – repo overview & guide
├── requirements.txt                  # Shared Python dependencies
├── .gitignore                        # Git ignore rules
├── data-structures/                  # Python fundamentals & data-structure patterns
│   ├── Insertion Sort.py
│   ├── queues_and_stacks.py
│   ├── Dictionaries.py
│   └── ...                           # lists, tuples, sets, I/O, lambdas, try/except, etc.
├── exercises/                        # Short coding challenges & practice problems
│   ├── number_guessing.py
│   ├── fibonacci_numbers.py
│   ├── rock_paper_scissors.py
│   └── ...                           # list/dict practice, filters, random utilities, etc.
├── oop/                              # Object-oriented programming examples
│   ├── classes_and_objects.py
│   ├── inheritance.py
│   ├── polymorphism.py
│   └── ...                           # constructors, destructors, encapsulation, payments, etc.
├── computer-vision/                  # OpenCV & face-recognition demos
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── image_inversion.py
│   ├── image_rotation.py
│   └── images/                       # sample images used by the scripts
├── libraries/                        # Popular Python library usage
│   ├── numpy_lib.py
│   ├── pandas_lib.py
│   ├── matplotlib-pyplot.py
│   ├── seaborn_lib.py
│   ├── requests_lib.py
│   └── beautiful_soup.py
├── llm-apis/                         # AI / LLM and external API examples
│   ├── openai-api.py
│   ├── assemblyai-api.py
│   ├── clarifyai_apy.py
│   ├── vercel_api_gateway.py
│   └── how_to_count_tokens.py
├── frameworks/                       # Web framework projects
│   ├── fastapi-dir/                  # Minimal FastAPI app (health & users endpoints)
│   │   ├── main.py
│   │   └── models.py
│   └── django-projects/
│       └── dictionary_project/       # Simple Django dictionary-style project
│           ├── dictionary_app/
│           ├── dictionary_project/
│           └── manage.py
├── machine-learning/
│   └── fastapi-ml-skeleton/         # ML project skeleton served via FastAPI
│       ├── data/data.csv            # example dataset
│       ├── models/my_model.joblib   # trained model artifact
│       ├── src/
│       │   ├── train.py             # training logic
│       │   └── main.py              # FastAPI app with /predict endpoint
│       ├── run.py                   # uvicorn entry point
│       └── README.md
├── rag/
│   └── rag-app-main/                # RAG demo (cloned from nileshhadalgi016/rag-app)
│       ├── main.ipynb               # PDF → chunks → embeddings → vector store → Q&A
│       ├── flow.tldr
│       └── Think-And-Grow-Rich_2011-06.pdf
├── leetcode/                        # Small LeetCode-style solutions
│   ├── merge_strings.py
│   └── mimimum_additions_to_make_valid_string.py
├── random_trials/                   # Miscellaneous experiments & CLI mini-projects
│   ├── basic_calculator.py
│   ├── password_strength_checker.py
│   ├── my_banking_system.py
│   ├── student_management.py
│   └── ...                          
├── files/                           # Example CSV datasets
│   ├── finance_data.csv
│   └── wine_data.csv
├── rag/..., sub-READMEs, notebooks  # Extra focused demos inside subfolders
└── management_system/               # raw python management system - learning project to consolidate OOP understanding
```

### 🚀 Getting started

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

### 🧪 Running selected projects

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

### 🤖 LLM / external API examples

- The scripts under `llm-apis/` show how to:
  - Call **OpenAI** models via the `openai` Python client.
  - Use **AssemblyAI** for speech‑to‑text or related audio tasks.
  - Talk to **Clarifai** and a **Vercel**-hosted API gateway.
- For these examples you will typically need API keys set as environment variables or in a `.env` file (see script comments for the expected variable names). **Do not commit your keys** to version control.

### 📚 How to use this repo for learning

- **Pick a topic folder** that matches what you want to learn (e.g. `data-structures/`, `oop/`, `computer-vision/`, `libraries/`, `llm-apis/`, `machine-learning/`).
- **Open scripts in your editor**, read through them, and run them from the terminal.
- **Experiment**:
  - Change input values and edge cases.
  - Add new functions or classes.
  - Refactor scripts into modules or packages as you grow more comfortable.
- **Use it as a cookbook**: when you need a quick reminder on how to do something (read CSVs with `pandas`, make a quick plot, build a small API endpoint, or call an AI service), search this repository for a nearby example and adapt it.

Over time this repo can evolve into a personal **Python cookbook + playground** where you keep adding new experiments, notes, and mini‑projects as you learn more.
