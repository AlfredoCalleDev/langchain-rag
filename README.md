# 🧠 LangChain RAG

![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.3%2B-green.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-orange.svg)
![uv](https://img.shields.io/badge/Package_Manager-uv-purple.svg)

Un sistema **RAG (Retrieval-Augmented Generation)** de línea de comandos, construido con LangChain, OpenAI y Chroma DB. Este proyecto permite conversar interactivamente con documentos locales (`.txt`, `.pdf`), garantizando un manejo eficiente y sincronizado de la base de datos vectorial a través de algoritmos de _Content Hashing_.

## ✨ Características Principales

- **Sincronización Inteligente de Chunks:** Utiliza hashes criptográficos (SHA-256) para identificar de forma única cada fragmento de texto. Si editas un documento, el sistema detecta los cambios, **elimina los fragmentos obsoletos y agrega los nuevos**, evitando la duplicación y ahorrando costos de llamadas a la API de Embeddings.
- **Soporte Multiformato:** Ingesta automática de archivos `.txt` y `.pdf` utilizando cargadores especializados (`PyPDFLoader` y `TextLoader`).
- **CLI Interactivo:** Un bucle infinito de chat en consola que te permite hacer preguntas continuas sobre tu base de conocimiento.
- **Arquitectura Modular:** El código está fuertemente dividido por responsabilidades (Loaders, Indexers, Splitters, Chains y Prompts).
- **Modo Debug:** Herramientas de formateo que permiten inspeccionar el contexto exacto inyectado al LLM para facilitar la depuración.

---

## 🛠️ Requisitos Previos

- **Python:** 3.12 o superior.
- **API Key de OpenAI:** Necesaria para el modelo de lenguaje y la generación de embeddings.
- Gestor de paquetes [uv](https://github.com/astral-sh/uv) (recomendado) o `pip`.

---

## 🚀 Instalación y Configuración

**1. Clonar el repositorio:**

```bash
git clone https://github.com/tu-usuario/langchain-rag.git
cd langchain-rag
```

**2. Instalar dependencias:**
Si utilizas el gestor rápido `uv` (Recomendado):

```bash
uv sync
```

Alternativamente, usando `pip` nativo:

```bash
python -m venv .venv
# Activar el entorno virtual (En Windows: .venv\Scripts\activate)
pip install -e .
```

**3. Configurar Variables de Entorno:**
El sistema depende de variables de entorno para funcionar. Copia el archivo de ejemplo y agrega tu clave de OpenAI:

```bash
cp .env.example .env
```

Abre el archivo `.env` y asegúrate de configurar tu `OPENAI_API_KEY`:

```env
OPENAI_API_KEY="sk-tu-api-key-aqui"
LLM_MODEL="gpt-4o-mini"
EMBEDDING_MODEL="text-embedding-3-small"
```

---

## 📚 Uso

**1. Agregar documentos:**
Coloca todos los archivos `.txt` o `.pdf` que desees consultar dentro de la carpeta `data/documents/` (si la carpeta no existe, el programa la creará en su primera ejecución).

**2. Ejecutar la aplicación:**
A través del script definido en tu entorno:

```bash
uv run langchain-rag
```

O ejecutando el archivo principal con Python:

```bash
python src/langchain_rag/main.py
```

**3. Interactuar:**
Una vez procesados e indexados los documentos (el sistema te indicará cuántos _chunks_ se actualizaron, agregaron o eliminaron), se abrirá la terminal:

```text
Pregunta: ¿Qué información tienes sobre [X]?

📚 Documentos encontrados:
- archivo.pdf

 IA: Según los documentos, la información es...
```

Para salir, simplemente presiona `Ctrl + C`.

---

## 🏗️ Estructura de carpetas del proyecto

```text
langchain-rag/
├── data/
│   ├── documents/           # 📥 Coloca aquí tus archivos .txt y .pdf
│   └── langchain_chroma/    # 🗄️ Base de datos vectorial de Chroma (Autogenerada)
├── src/langchain_rag/
│   ├── ai/                  # Proveedores de LLM y Embeddings
│   ├── chains/              # Cadenas RAG principales
│   ├── config/              # Gestión de configuraciones y .env
│   ├── indexers/            # Lógica de Hashing y Sincronización de Base de Datos
│   ├── loaders/             # Ingesta de archivos del disco
│   ├── prompts/             # System Prompts para el asistente
│   ├── splitters/           # Chunking de documentos
│   ├── utils/               # Formateadores y herramientas de depuración
│   └── main.py              # Punto de entrada
├── pyproject.toml           # Configuración de dependencias y scripts
└── .env                     # Variables de entorno
```

## ⚙️ Configuración Avanzada

Puedes modificar los parámetros de RAG dentro de `src/langchain_rag/config/settings.py` o sobrescribirlos usando el archivo `.env`:

- `CHUNK_SIZE` (default: 500)
- `CHUNK_OVERLAP` (default: 50)
- `TOP_K_RESULTS` (default: 3)
