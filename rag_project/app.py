import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_answer(context, question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
    {
    "role": "system",
    "content": """
You are a helpful AI assistant.

Use ONLY the provided context to answer questions.
If multiple relevant points exist, combine them into a clear and natural response.
Do not use external knowledge.
Keep answers concise and relevant.
"""
},

    {"role": "user", "content": f"""
Context:
{context}

Question:
{question}
"""}
]
    )
    return response.choices[0].message.content

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

st.title("Domain Knowledge Assistant (RAG + Groq)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a Question")

text = ""
chunks = []
index = None

if uploaded_file:

    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    st.success("PDF Loaded Successfully")

    chunks = re.split(r'\n\s*\n|(?<=\.)\s+', text)
    chunks = [c.strip() for c in chunks if len(c.strip()) > 30]

    st.info(f"Chunks created: {len(chunks)}")

    embeddings = model.encode(chunks).astype('float32')

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    st.subheader("Sample Content")
    for c in chunks[:10]:
        st.write(c)

if question and uploaded_file and index is not None:

    q_vec = model.encode([question]).astype('float32')

    _, indices = index.search(np.array(q_vec), k=8)

    context = ""
    for i in indices[0]:
        if i < len(chunks):
            context += chunks[i] + "\n"

    answer = get_answer(context, question)

    st.subheader("AI Answer")
    st.write(answer)

    with st.expander("Retrieved Context"):
        for i in indices[0]:
            if i < len(chunks):
                st.write(chunks[i])
