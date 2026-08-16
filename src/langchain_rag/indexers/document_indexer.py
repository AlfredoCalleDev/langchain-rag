from langchain_rag.databases.vdb import get_or_create_vector_store
from langchain_core.vectorstores import VectorStore
from langchain_rag.loaders.file_loader import load_directory
from langchain_rag.splitters.document_splitter import split_documents
from langchain_rag.config.settings import settings


def index_documents(
    documents_path: str = None,
    chroma_path: str = None,
    collection_name: str = None,
) -> tuple[VectorStore, int]:
    """
    Procesa todos los documentos del directorio y los agrega al vector store

    Args:
        documents_path (str): Ruta del directorio
        chroma_path (str): Ruta del vector store
        collection_name (str): Nombre de la colección

    Returns:
        tuple: (vector_store, num_documents_added)
    """

    documents = load_directory(path=documents_path or settings.DOCUMENTS_PATH)

    if not documents:
        print(f"❌ No hay documentos para indexar")
        return None, 0

    chunks = split_documents(documents)

    if not chunks:
        print(f"❌ No hay chunks para indexar. Los archivos posiblemente estén vacíos.")
        return None, 0

    vector_store = get_or_create_vector_store(
        collection_name=collection_name or settings.COLLECTION_NAME,
        persist_path=chroma_path or settings.CHROMA_PATH,
    )

    num_indexed_chunks = vector_store._collection.count()

    print(f"✅ {num_indexed_chunks} chunks ya indexados")
    print(f"⌛ Indexando {len(chunks)} chunks nuevos...")

    vector_store.add_documents(chunks)

    new_num_chunks = vector_store._collection.count()

    print(f"✅ {new_num_chunks} chunks en total")

    return vector_store, vector_store._collection.count()
