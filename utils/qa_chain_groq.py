from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def create_qa_chain_groq(documents, groq_api_key: str):
    # Embeddings (como Groq não tem embeddings nativos, usamos HuggingFace)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    # Indexação vetorial
    vectordb = FAISS.from_documents(documents, embeddings)

    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # LLM usando Groq + DeepSeek, com a chave informada pelo usuário
    llm = ChatGroq(
        model="deepseek-r1-distill-llama-70b",  # pode trocar para outro modelo Groq
        temperature=0,
        api_key=groq_api_key
    )
    
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False
    )
    return qa_chain
