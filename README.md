# LocalDrop

A lightweight file sharing application for your home NAS.

---

## About

LocalDrop is a little project I'm working on as a personal challenge — building something from scratch while getting better at web programming (and programming as a whole).

If you happen to stumble across this project and have the curiosity to check it out, I'm open to suggestions or anything that might help improve my learning. :)

---

## Installation

> **Note:** Not deployment-ready. For local/development use only.

**1. Set up a virtual environment and install dependencies**

```bash
python -m venv venv
pip install -r requirements.txt
```

**2. Activate the virtual environment**

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Run the development server**

```bash
uvicorn main:app --reload
```

The app will be available at `http://localhost:8000`.
