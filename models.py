#define requests and response schemas for FastAPI
from pydantic import BaseModel
class CrawlRequest(BaseModel):
    url: str

class QueryRequest(BaseModel):
    query: str
    context: str
class QueryResponse(BaseModel):
    answer: str
    source_documents: list
    metadata: dict
class CrawlResponse(BaseModel):
    status: str
    message: str
    data: dict

    