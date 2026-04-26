import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def iniciar_asistente(archivo_pdf, groq_key):
    """
    Crea un sistema RAG (Retrieval-Augmented Generation) dinámico.
    Recibe la ruta de un PDF y la API Key del modelo de IA para inicializar.
    """

    # --- PROCESAMIENTO DEL DOCUMENTO ---
    # Se carga el PDF desde la ruta temporal proporcionada por la interfaz
    loader = PyPDFLoader(archivo_pdf)
    paginas = loader.load()

    # Para un mejor entendimiento se dividi el texto en (chunks) para que la IA pueda procesarlos de mejor manera
    # chunk_overlap asegura que no se pierda el contexto entre un trozo y otro
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    fragmentos = text_splitter.split_documents(paginas)

    # --- BASE DE DATOS DE VECTORES ---
    # Se Convierte el texto en números (vectores) en este caso usando un modelo local gratuito de HuggingFace
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma.from_documents(documents=fragmentos, embedding=embeddings)

    # --- CONFIGURACIÓN DE LA IA ---
    # Inicializamos Llama 3.3 a través de Groq para poder obtener respuestas ultrarrápidas
    llm = ChatGroq(
        temperature=0, 
        model_name="llama-3.3-70b-versatile", 
        groq_api_key=groq_key
    )
    # se Define la "personalidad" y las instrucciones para el bot
    prompt = ChatPromptTemplate.from_template("""
    Responde basándote solo en el manual técnico:
    {context}
    Pregunta: {input}
    """)

    # --- CONSTRUCCIÓN DE LA CADENA (LCEL) ---
    # Se Conectan las piezas: Contexto -> Prompt -> LLM -> Texto de salida
    asistente = (
        {"context": vector_db.as_retriever(), "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return asistente
if __name__ == "__main__":
    pass
