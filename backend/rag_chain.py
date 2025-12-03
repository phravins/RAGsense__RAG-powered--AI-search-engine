import os, requests, bs4, torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GEN_MODEL   = "google/flan-t5-small"   # 250 M params – runs on CPU

# 1. Embeddings
embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL,
                                   model_kwargs={'device':'cpu'})

# 2. LLM
gen_pipeline = pipeline("text2text-generation",
                        model=GEN_MODEL,
                        tokenizer=GEN_MODEL,
                        max_new_tokens=200,
                        temperature=0.2,
                        device_map="cpu")
llm = HuggingFacePipeline(pipeline=gen_pipeline)

# 3. Text splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                          chunk_overlap=50)

def build_index(url: str) -> FAISS:
    """Download page, split, embed, return vectorstore."""
    html = requests.get(url, timeout=15).text
    soup = bs4.BeautifulSoup(html, "lxml")
    text = soup.get_text(" ", strip=True)
    docs = splitter.create_documents([text])
    vs = FAISS.from_documents(docs, embeddings)
    return vs

def answer(query: str, vs: FAISS) -> str:
    qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vs.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False)
    return qa.run(query)