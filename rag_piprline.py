#llm powered summarization using langchains retrievalQa or similar

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain.prompts import PromptTemplate
def create_qa_chain():
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="embeddings_store", embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(temperature=0, model_name="gpt-4")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
qa_chain = create_qa_chain()
def answer_query(query: str):
    result = qa_chain.run(query)
    return result
def answer_query_with_sources(query: str):
    result = qa_chain({"query": query})
    return {
        "answer": result['result'],
        "source_documents": [
            {"page_content": doc.page_content, "metadata": doc.metadata}
            for doc in result['source_documents']
        ]
    }
