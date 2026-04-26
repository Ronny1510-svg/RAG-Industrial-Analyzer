import streamlit as st
import os
from Analista import iniciar_asistente # Importamos tu lógica

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Asistente de Ingeniería", 
    page_icon="⚙️",
    layout="centered"
)
# Títulos principales
st.title("Asistente Inteligente de Manuales")
st.markdown("Sube un manual técnico y hazle preguntas en tiempo real.")

# --- BARRA LATERAL (ENTRADAS DE USUARIO) ---
with st.sidebar:
    st.header("Configuración")
    # Entrada segura para la API Key
    api_key = st.text_input("Groq API Key", type="password")
    archivo = st.file_uploader("Sube tu manual (PDF)", type="pdf")

# --- LÓGICA DE LA APLICACIÓN ---
if archivo and api_key:
    pdf_path = "temp_manual.pdf"
    with open(pdf_path, "wb") as f:
        f.write(archivo.getbuffer())
    
    # Se verifica si el asistente ya está en la memoria de la sesión
    # Esto evita que el PDF se analice de nuevo con cada pregunta
    if "asistente" not in st.session_state:
        with st.spinner("Analizando manual técnico... esto puede tardar un momento."):
            # Conexion con el motor de Analista.py
            st.session_state.asistente = iniciar_asistente(pdf_path, api_key)
            st.success("¡Manual cargado y procesado!")

    # --- ÁREA DE CHAT ---
    st.divider()
    pregunta = st.text_input("¿Qué duda tienes sobre el manual?")
    
    if pregunta:
        with st.spinner("Pensando..."):
            respuesta = st.session_state.asistente.invoke(pregunta)
            st.markdown("### Respuesta:")
            st.write(respuesta)

else:
    st.info("Por favor, sube un archivo PDF y asegúrate de tener la API Key configurada.")
if __name__ == "__main__":
    pass