from langchain_core.runnables import Runnable, RunnablePassthrough
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_rag.config.settings import settings
from langchain_rag.utils.formatters import format_docs


def build_rag_chain(
    vector_store: VectorStore, prompt: ChatPromptTemplate, llm: BaseChatModel
) -> tuple[Runnable, VectorStoreRetriever]:
    """Construye la cadena RAG

    Args:
        vector_store (VectorStore): Almacén de vectores
        prompt (ChatPromptTemplate): Prompt del asistente
        llm (BaseChatModel): Modelo de lenguaje

    Returns:
        tuple[Runnable, VectorStoreRetriever]: Cadena RAG y retriever
    """

    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": settings.TOP_K_RESULTS}
    )

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever
