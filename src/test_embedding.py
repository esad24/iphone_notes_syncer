from langchain_community.embeddings import HuggingFaceEmbeddings

print("Lade Modell...")
embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2",
    

)

print("Berechne Test-Wörter...")

vektor_hund = embeddings.embed_query("Hund")
vektor_auto = embeddings.embed_query("Auto")

print("\nErgebnisse (die ersten 5 Zahlen des Vektors):")
print(f"Hund: {vektor_hund[:5]}")
print(f"Auto: {vektor_auto[:5]}")

print("\n" + "="*40)
if vektor_hund == vektor_auto:
    print("PC generiert für alles dieselben Zahlen!")
else:
    print("Alles perfekt! Die KI unterscheidet die Wörter.")
print("="*40)