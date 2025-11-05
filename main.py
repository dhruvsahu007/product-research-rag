from fastapi import FastAPI
from models import CrawlRequest, QueryRequest
from crawler import crawl_product_page
from embeddings_store import store_document, query_documents

app = FastAPI()

@app.post("/crawl")
def crawl_endpoint(request: CrawlRequest):
    product_info = crawl_product_page(request.url)
    store_document(product_info)
    return {"status": "success", "data": product_info}

@app.post("/query")
def query_endpoint(request: QueryRequest):
    results = query_documents(request.query)
    return {"status": "success", "results": results}    
