from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Cargar vectorstore
vectorstore = FAISS.load_local("Hermitage/vectorstore", OpenAIEmbeddings(), allow_dangerous_deserialization=True)

# Realizar consulta
query = "¿Cuál es la política de vacaciones?"
docs = vectorstore.similarity_search(query)

# Mostrar resultados
for i, doc in enumerate(docs):
    print(f"\n--- Resultado {i+1} ---")
    print(doc.page_content)

if not docs:
    print("❌ No se encontraron resultados para la consulta.")
else:
    for i, doc in enumerate(docs):
        print(f"\n--- Resultado {i+1} ---")
        print(doc.page_content)


