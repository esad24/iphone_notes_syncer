from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = f"C:\\Users\\esad2\\Desktop\\Programmieren\\Projects\\myKnowledgeBase\\data\\notes_json\\chroma_db_neu"

def search_notes():
    embeddings = HuggingFaceBgeEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2",
        encode_kwargs={'normalize_embeddings': True}
    )

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    while True:
        query = input("Deine Suchanfrage: ")

        if query == "exit":
            break
        if not query.strip():
            continue

        results = vectorstore.similarity_search_with_score(query, k=3)
        print(f"TOP 3 Treffer für: {query}")
        print("="*50)

        for i, (doc, score) in enumerate(results):
            title = doc.metadata.get("title", "Ohne Titel")
            print(f"\n[{i+1}] Notiz: {title} | Similarity Score: {score:.4f}")
            print("-" * 40)

            content = doc.page_content
            if len(content)  > 300:
                   print(content[:300] + "[...]")
            else:
                 print(content)

if __name__ == "__main__":
     search_notes()    
