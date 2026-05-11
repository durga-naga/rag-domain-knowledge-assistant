RAG Domain Knowledge Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on the content.

Overview

This project implements a Domain Knowledge Assistant using Retrieval-Augmented Generation. It extracts information from PDF files, performs semantic search using vector embeddings, and generates context-aware responses using a large language model.

Features

- Upload and process PDF documents
- Split text into meaningful chunks
- Generate embeddings using Sentence Transformers
- Perform similarity search using FAISS
- Generate responses using Groq LLM
- Interactive web interface using Streamlit

Technology Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Groq API
- PyPDF
- NumPy

Live Demo

https://rag-domain-knowledge-assistant-d9kteieh3tjfzmicxa9nkf.streamlit.app/

Workflow

1. User uploads a PDF file
2. Text is extracted from the document
3. Text is divided into chunks
4. Embeddings are generated for each chunk
5. FAISS retrieves relevant chunks based on query
6. Groq LLM generates final response using context

Project Purpose

This project demonstrates how Retrieval-Augmented Generation can be used to build intelligent document-based question answering systems.
