import json
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
import shutil

NOTES_JSON_PATH = f"C:\\Users\\esad2\\Desktop\\Programmieren\\Projects\\myKnowledgeBase\\data\\notes_json\\notes.json"
CHROMA_PATH = f"C:\\Users\\esad2\\Desktop\\Programmieren\\Projects\\myKnowledgeBase\\data\\notes_json\\chroma_db_neu"

def bulild_vector_database():
    if not os.path.exists(NOTES_JSON_PATH):
        print("No notes")
        return
    
    if os.path.exists(CHROMA_PATH):
        print("Lösche Datenbank")
        shutil.rmtree(CHROMA_PATH)

    with open(NOTES_JSON_PATH, "r", encoding="utf-8") as f:
        notes = json.load(f)
    
    docs = []

    for note in notes:
        full_text = f"Titel: {note['title']}\nInhalt: {note['content']}"
        doc = Document(
            page_content=full_text,
            metadata={"title": note["title"]}
        )
        docs.append(doc)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\\n\\n", "\\n", " ", ""]
    )
    chunks = splitter.split_documents(docs)
    print(f"{len(chunks)}] Chunks erstellt")

    embeddings = HuggingFaceEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2",
        encode_kwargs={'normalize_embeddings': True}
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("Erfolgreiche ChromaDB Vektordatenbank erstellt")

if __name__ == "__main__":
    bulild_vector_database()