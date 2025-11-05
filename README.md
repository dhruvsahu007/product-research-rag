Q: 1
Problem Statement: Product Research RAG System
Objective
Build an AI-powered Product Research System that allows users to input product page URLs and e-commerce product listings.

Your system should:

Crawl and extract relevant data from the given product page(s).

Store the textual and metadata information in a Vector Database using embeddings.

Enable hybrid retrieval — combining semantic similarity search (via embeddings) with metadata filtering.

Support natural language queries like:

“Find all products that have a price less than $50”

Generate summarized and relevant results using an LLM-powered RAG pipeline.

System Architecture Overview
Your pipeline should include the following layers:

Input Layer – Accept URLs from users.
Crawler Layer – Crawl each URL, extract meaningful text and metadata.
Preprocessing Layer – Clean, chunk, and prepare text.
Embedding + Storage Layer – Generate embeddings and store them in a vector database (e.g., Chroma or Pinecone).
Retrieval + Generation Layer – Perform hybrid search and respond to user queries using an LLM.
Technical Requirements
1. Crawling
Use one of the following tools to extract textual content and metadata:

Tool	Description	Documentation
BeautifulSoup	For static HTML scraping	https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Playwright	For JavaScript-rendered sites	https://playwright.dev/python/docs/intro
LangChain Document Loader	Pre-built crawlers for GitHub, URLs, and webpages	https://python.langchain.com/docs/integrations/document_loaders/
You must extract:

Title / Product Name
Description / README text
Tags or keywords (if available)
Metadata (e.g., stars, last updated date for GitHub repos)
Source URL
2. LangChain Components
Use LangChain for:

Text chunking → Text Splitters
Embedding generation → Embeddings
Vector storage → VectorStores
Retrieval and RAG pipeline → Retrieval-Augmented Generation
3. Vector Database Options
DB	Type	Documentation
Chroma	Local and lightweight	https://docs.trychroma.com/
Pinecone	Managed and scalable	https://docs.pinecone.io/docs
FAISS	Local in-memory	https://faiss.ai/
Store each document chunk with metadata

API Specifications
You must expose two endpoints:

1. POST /crawl
Description
Crawl one or more product pages, extract meaningful text and metadata, generate embeddings, and store them in your vector database.

2. POST /query
Description
Perform hybrid retrieval (semantic + metadata filter) and generate an AI-driven summary response.

Tech Stack
Backend: FastAPI
Crawler: BeautifulSoup / Playwright / LangChain loaders
Embeddings: OpenAI API / Sentence Transformers
Vector DB: Chroma / Pinecone / FAISS
Useful Documentation Links
Component	Docs
LangChain (Python)	https://python.langchain.com/docs/
LangChain (JS/TS)	https://js.langchain.com/docs/
BeautifulSoup	https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Playwright	https://playwright.dev/python/docs/intro
Chroma	https://docs.trychroma.com/
Pinecone	https://docs.pinecone.io/docs
OpenAI Embeddings	https://platform.openai.com/docs/guides/embeddings
Submission Guidelines
Push your code to a public GitHub repository:
README Must Include:

Project overview
Setup & run instructions
API documentation
Example queries and screenshots
All changes saved

Enter your answer here
