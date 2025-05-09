import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar el CSV generado por los logs
df = pd.read_csv("logs/summary_export.csv")

st.title("📊 Hermitage AI Agent Dashboard")

# Filtro por fecha
fechas = df["Fecha"].unique()
fecha_seleccionada = st.selectbox("Selecciona una fecha:", fechas)
df_filtrado = df[df["Fecha"] == fecha_seleccionada]

# Gráfica de uso por agente
st.subheader("🧠 Agentes más utilizados")
st.bar_chart(df_filtrado["Agente"].value_counts())

# Preguntas frecuentes
st.subheader("❓ Preguntas más comunes")
st.write(df_filtrado["Pregunta"].value_counts().head(5))

# Tabla completa
st.subheader("📋 Todas las interacciones")
st.dataframe(df_filtrado[["Pregunta", "Agente", "Respuesta"]])

# Botón de descarga
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Descargar resumen en CSV",
    data=csv,
    file_name=f"resumen_{fecha_seleccionada}.csv",
    mime='text/csv'
)
