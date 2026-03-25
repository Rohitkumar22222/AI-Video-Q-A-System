# 🎥 AI Video Q&A System (RAG-based)

> A Retrieval-Augmented Generation (RAG) system that enables semantic search and question answering over video lecture content using local LLMs.

---

## 🚀 Overview

This project builds an AI assistant that helps users **query and learn from video lectures** without manually searching through them.

It works by:
- Converting videos → text  
- Creating embeddings  
- Retrieving relevant content  
- Generating answers using an LLM  

---

## 🧠 Pipeline

Videos → Audio → Transcripts → Chunks → Embeddings  
          
User Query → Similarity Search → Context → LLM → Answer  

---

## ⚙️ Features

- Semantic search over video content  
- Local LLM support (Ollama / Llama)  
- Fast retrieval using embeddings  
- Fully offline and privacy-friendly  

---

## 🛠️ Tech Stack

- Python  
- Ollama (Llama 3.2)  
- Whisper (Speech-to-Text)  
- Sentence Transformers (Embeddings)  
- Joblib (Storage)  
- FFmpeg  

---

## 📂 Project Structure

videos/        # Input videos  
mp3/           # Extracted audio  
json/          # Transcripts  
embeddings/    # Vector data  
scripts/       # Processing scripts  
main.py        # Main RAG pipeline  

---

## ▶️ Getting Started

### 1. Clone the repo
git clone https://github.com/Rohitkumar22222/AI-Video-Q-A-System.git  
cd AI-Video-Q-A-System 

### 2. Install dependencies
pip install -r requirements.txt  

### 3. Add videos
Place your video files in:  
videos/  

---

## ⚡ Run the Pipeline

### Step 1: Convert videos to audio
python video_to_mp3.py  

### Step 2: Convert audio to text
python mp3_to_json.py  

### Step 3: Generate embeddings
python preprocess_json.py  

### Step 4: Run the assistant
python main.py  

---

## 💬 Example

Query:  
What are semantic tags in HTML?

Response:  
Semantic tags are HTML elements that describe their meaning clearly...  
Examples: <header>, <article>, <footer>  

Source: Video 11  

---

## 🚧 Limitations

- CLI-based interface  
- Limited dataset  
- Uses Joblib instead of scalable vector DB  

---

## 🚀 Future Improvements

- Add web UI (React / Streamlit)  
- Use vector databases (ChromaDB, Pinecone)  
- Improve LLM with cloud APIs  
- Add real-time streaming responses  

---

## 🎯 Use Cases

- AI assistant for courses  
- Educational search engines  
- YouTube lecture summarization  
- Personal knowledge base  

---

## 📜 License

MIT License  

---

## ⭐ Support

If you like this project:
- Star ⭐ the repo  
- Share it  
