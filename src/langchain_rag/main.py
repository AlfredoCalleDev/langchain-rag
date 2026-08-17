from langchain_rag.config.settings import settings
from langchain_rag.chains.rag import build_rag_chain
from langchain_rag.indexers.document_indexer import index_documents
from langchain_rag.prompts.assistant import assistant_prompt
from langchain_rag.ai.llm import get_llm


def start_app():
    vector_store, num_chunks = index_documents(
        documents_path=settings.DOCUMENTS_PATH,
        chroma_path=settings.CHROMA_PATH,
        collection_name=settings.COLLECTION_NAME,
    )

    if vector_store is None:
        print("\n Pasos para empezar")
        print(f" 1. Crea la carpera: {settings.DOCUMENTS_PATH}")
        print(" 2. Agrega archivos .txt o .pdf")
        print(" 3. Vuelve a ejecutar este script")
        return

    rag_chain, retriever = build_rag_chain(
        vector_store=vector_store,
        prompt=assistant_prompt,
        llm=get_llm(temperature=settings.DEFAULT_TEMPERATURE),
    )

    while True:
        user_question = input("Pregunta: ").strip()

        retrieved_chunks = retriever.invoke(user_question)

        if not retrieved_chunks:
            print(f"\n❌ No se encontraron documentos relacionados con tu pregunta")
            continue

        print(f"\n📚 Documentos encontrados:")

        for chunk in retrieved_chunks:
            print(f"- {chunk.metadata['source']}")

        print("\n IA: ", end="", flush=True)
        answer = rag_chain.invoke(user_question)
        print(answer)

        print("\n")


if __name__ == "__main__":
    start_app()
