# Scrape
## Overview  
This project is a Flask-based web scraper that extracts course data from https://brainlox.com/courses/category/technical, processes the text using LangChain, and stores embeddings in ChromaDB. It also provides a search API to retrieve relevant course information based on user queries.  

## Features  
- Scrapes web content using langchain.document_loaders.WebBaseLoader  
- Splits text into manageable chunks using RecursiveCharacterTextSplitter  
- Embeds text using sentence-transformers  
- Stores embeddings in ChromaDB  
- Provides a /search API for retrieving relevant course content  

## Installation  

### Prerequisites  
Ensure you have Python installed (preferably 3.8 or later).  

### Install Dependencies  
Run the following command:  
bash
pip install flask langchain sentence-transformers chromadb

## Usage  

### Running the Application  
1. Start the Flask server:  
   bash
   python scraper.py
   
2. The server will run on http://127.0.0.1:5000/  

### API Endpoint  

#### *Search for Courses*  
- *URL:* /search  
- *Method:* POST  
- *Request Body (JSON):*  
  json
  {
    "query": "machine learning"
  }
  
- *Response:* A list of the most relevant course descriptions.  

## Project Structure  

├── scraper.py  # Main script
├── requirements.txt  # Dependencies (optional)
├── chroma_db/  # ChromaDB persistent storage


## Future Enhancements  
- Support for multiple URLs  
- Enhanced ranking with advanced retrieval models  
- Deployment as a cloud API
