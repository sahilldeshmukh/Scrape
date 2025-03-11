from flask import Flask, request, jsonify
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# Initialize Flask App
app = Flask(__name__)

# Load and Process Data
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)

# Initialize Sentence Transformer (Free Model)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

# Initialize ChromaDB
db = chromadb.PersistentClient(path="./chroma_db")
collection = db.get_or_create_collection("course_embeddings")

# Store Embeddings
for i, doc in enumerate(split_docs):
    embedding = embedding_model.encode(doc.page_content).tolist()
    collection.add(ids=[str(i)], embeddings=[embedding], metadatas=[{"text": doc.page_content}])

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "")
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    
    response = [res["text"] for res in results["metadatas"][0]]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)