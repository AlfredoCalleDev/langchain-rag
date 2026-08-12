import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Configuración de la aplicación.
    """

    def __init__(self) -> None:
        """Inicializa la configuración y valida las variables de entorno"""
        self.validate()

        # Modelos
        self.LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
        self.EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

        # Parámetros LLM
        self.DEFAULT_TEMPERATURE: float = 0.5
        self.MAX_RETRIES: int = 3

        # RAG
        self.CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
        self.CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))
        self.TOP_K_RESULTS: int = int(os.getenv("TOP_K_RESULTS", 3))

    def validate(self) -> None:
        """Valida las variables de entorno requeridas"""
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is not defined")


settings = Settings()
