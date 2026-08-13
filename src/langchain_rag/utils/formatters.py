from langchain_core.documents import Document


def format_docs(docs: list[Document]) -> str:
    """Convierte una lista de documentos de LangChain en una sola cadena de texto.

    Args:
        docs (list[Document]): Lista de documentos

    Returns:
        str: Texto formateado
    """

    return "\n\n---\n\n".join(
        [
            f"[Fuente: {doc.metadata.get('source', 'desconocida')},"
            f"Página: {doc.metadata.get('page', "N/A")}]\n {doc.page_content}"
            for doc in docs
        ]
    )
