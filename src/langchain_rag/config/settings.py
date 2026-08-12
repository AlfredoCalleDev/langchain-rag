import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Configuración de la aplicación.
    """

    # Modelos
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    # Parámetros LLM
    DEFAULT_TEMPERATURE: float = 0.7
    LOW_TEMPERATURE: float = 0.1
    MAX_RETRIES: int = 3

    # RAG
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))
    TOP_K_RESULTS: int = int(os.getenv("TOP_K_RESULTS", 3))

    def __init__(self) -> None:
        """Inicializa la configuración y valida las variables de entorno"""
        self.validate()

    def validate(self) -> None:
        """Valida las variables de entorno requeridas"""
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is not defined")


settings = Settings()
