import os
from dotenv import load_dotenv

load_dotenv()

# ✅ NUEVOS IMPORTS ACTUALIZADOS
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Ruta a los documentos demo
folder_path = "Hermitage/Data/demo_docs"

# Leer documentos .txt
docs = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, filename))
        docs.extend(loader.load())

# Dividir texto en fragmentos manejables
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embeddings y vectorstore
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embedding)

# Guardar en disco
vectorstore.save_local("Hermitage/vectorstore")

print("✅ Vectorstore generado y guardado con éxito.")
