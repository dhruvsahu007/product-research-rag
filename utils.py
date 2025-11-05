#helper function for cleaning or chunking text data
def clean_text(text: str) -> str:
    return ' '.join(text.split())
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
def extract_metadata(url: str) -> dict:
    return {"source_url": url}
