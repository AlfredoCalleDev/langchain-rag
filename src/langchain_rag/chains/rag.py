from langchain_chroma import Chroma
from langchain_core.runnables import Runnable, RunnablePassthrough
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_rag.config.settings import settings
from langchain_rag.ai.llm import get_llm
from langchain_rag.utils.formatters import format_docs


def build_rag_chain(
    vector_store: Chroma, prompt: ChatPromptTemplate
) -> tuple[Runnable, VectorStoreRetriever]:
    """Construye la cadena RAG

    Args:
        vector_store (Chroma): Almacén de vectores
        prompt (ChatPromptTemplate): Prompt del asistente

    Returns:
        tuple[Runnable, VectorStoreRetriever]: Cadena RAG y retriever
    """

    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": settings.TOP_K_RESULTS}
    )

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | get_llm(temperature=settings.LOW_TEMPERATURE)
        | StrOutputParser()
    )

    return rag_chain, retriever
