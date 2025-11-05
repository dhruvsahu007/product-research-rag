from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="embeddings_store", embedding_function=embeddings)
def store_document(url: str, text: str):
    metadata = {"url": url}
    vectorstore.add_texts([text], metadatas=[metadata])
    vectorstore.persist()
def query_documents(query: str, top_k: int = 5):
    results = vectorstore.similarity_search(query, k=top_k)
    return [{"text": doc.page_content, "metadata": doc.metadata} for doc in results]
