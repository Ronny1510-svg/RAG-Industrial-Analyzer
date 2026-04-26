# RAG-Industrial-Analyzer
Asistente de Inteligencia Artificial basado en RAG (Retrieval-Augmented Generation) para el análisis técnico de manuales industriales. Desarrollado con Python, LangChain y Groq (Llama 3.3) para facilitar la consulta rápida de procedimientos de seguridad, mantenimiento y operación de maquinaria pesada.

**Asistente de Inteligencia Artificial para el análisis técnico de manuales industriales.**

Este proyecto implementa una arquitectura **RAG (Retrieval-Augmented Generation)** que permite interactuar con documentos PDF técnicos (como manuales de maquinaria o guías de seguridad). Utiliza **HuggingFace** para el procesamiento local de datos y **Groq (Llama 3.3)** para la generación de respuestas de alta velocidad (el modelo de IA puede ser cambiado).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12
* **Orquestador de IA:** LangChain (LCEL)
* **Modelo de Lenguaje (LLM):** Llama-3.3-70b-versatile vía Groq
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
* **Base de Datos Vectorial:** ChromaDB
* **Interfaz de Usuario:** Streamlit

## 🚀 Funcionalidades

* **Carga Dinámica:** Sube cualquier manual en formato PDF desde la interfaz.
* **Procesamiento Inteligente:** Segmentación de documentos para una recuperación mas precisa de información.
* **Consultas Técnicas:** Responde preguntas sobre seguridad, procedimientos de mantenimiento, códigos de error y especificaciones técnicas.
* **Seguridad de API:** Integración de API Key mediante entrada de usuario protegida.

## 📂 Estructura del Proyecto

* `App.py`: Gestión de la interfaz web con Streamlit.
* `Analista.py`: Motor de lógica RAG, encargado de la vectorización y conexión con el LLM.
* `requirements.txt`: Listado de dependencias necesarias para el entorno.

## 📋 Requisitos

El sistema requiere las librerías listadas en `requirements.txt`. El procesamiento de embeddings se realiza de forma local, mientras que la inferencia de lenguaje se ejecuta a través de Groq para garantizar una respuesta inmediata.

---

### Notas de Ingeniería
Este asistente fue diseñado bajo el principio de **desacoplamiento de datos**, separando la lógica del backend de la interfaz de usuario, permitiendo que el sistema sea escalable para diferentes tipos de documentación técnica industrial.
