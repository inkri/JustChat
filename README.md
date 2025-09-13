# JustChat
JustChat

Here’s a clean **README template** for your Hugging Face Space that explains your app, setup, and usage:

````markdown
# JustChat - AI Chat Agent

JustChat is an AI-powered conversational agent built with **FastAPI**, **LangGraph**, and **Hugging Face Transformers**.  
It allows users to ask questions, retrieve information from a knowledge base (via Hugging Face datasets), and search the web (DuckDuckGo) in a conversational manner.

---

## 📝 Features

- Chat with a lightweight **LLaMA-based model** (TinyLlama 1.1B)  
- Handles **conversation context** using LangGraph states  
- **RAG (Retrieval-Augmented Generation)** support with:
  - Hugging Face datasets
  - DuckDuckGo search for additional information  
- FastAPI-based API for interaction  

---

## ⚡ Live Demo

The app is hosted on Hugging Face Spaces:  
[https://huggingface.co/spaces/abhishekjaiswal90/JustChat](https://huggingface.co/spaces/abhishekjaiswal90/JustChat)

---

## 📦 Setup / Installation

1. **Clone the repo (local setup)**

```bash
git clone https://github.com/inkri/JustChat.git
cd JustChat
````

2. **Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run locally**

```bash
uvicorn agent_app:app --reload --host 127.0.0.1 --port 7860
```

5. Open your browser and test API at:

```
http://127.0.0.1:7860/docs
```

---

## 🔧 API Usage

### Endpoint: `/ask`

* **Method:** POST
* **Body:**

```json
{
  "prompt": "Your question here"
}
```

* **Response:**

```json
{
  "answer": "AI-generated response"
}
```

---

## 🛠️ Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face:
   [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Clone the Space:

```bash
git clone https://huggingface.co/spaces/USERNAME/JustChat
cd JustChat
```

3. Copy your `agent_app.py` and `requirements.txt` to the Space folder.
4. Commit and push:

```bash
git add .
git commit -m "Initial deploy"
git push
```

The app will be automatically built and hosted live.

---

## ⚡ Notes

* Requires Python 3.10+
* Model files are downloaded automatically on first run (ensure internet connection)
* DuckDuckGo search is used for retrieving online info.

---

## 📄 License

This project is **MIT licensed**.

```

---

If you want, I can also **prepare a ready-to-use `requirements.txt`** optimized for Hugging Face deployment so it builds without errors.  

Do you want me to do that?
```
