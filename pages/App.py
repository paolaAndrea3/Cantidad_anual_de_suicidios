import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

# Título principal de la aplicación
st.title("Análisis Interactivo de Suicidios en Antioquia (2005-2022)")

# Carga el dataset (asegúrate de que la ruta sea correcta)
try:
    df = pd.read_csv('static/datasets/Cantidad_anual_de_suicidios_reportados_en_el_Departamento_de_Antioquia_desde_2005_20250506.csv')
except FileNotFoundError:
    st.error("Error: No se encontró el archivo de datos. Asegúrate de que la ruta sea correcta.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {e}")
    st.stop()

# Barra lateral para los filtros
with st.sidebar:
    st.header("Filtros")

    # Filtro por rango de año con slider
    años_unicos = df['Anio'].unique()
    min_anio = int(años_unicos.min())
    max_anio = int(años_unicos.max())
    rango_anios = st.sidebar.slider("Seleccionar Rango de Años", min_value=min_anio, max_value=max_anio, value=(min_anio, max_anio), key="slider_anio")
    anio_inicio, anio_fin = rango_anios

    # Filtro por región (multiselect)
    regiones_unicas = df['NombreRegion'].unique()
    region_seleccionada = st.sidebar.multiselect("Seleccionar Región(es)", regiones_unicas, key="multiselect_region")

    # Opcional: Filtro por código de región (multiselect)
    codigos_region_unicos = df['CodigoRegion'].unique()
    codigo_region_seleccionado = st.sidebar.multiselect("Seleccionar Código de Región(es)", sorted(codigos_region_unicos), key="multiselect_codigo_region")

# Filtrado de datos basado en las selecciones
df_filtrado = df.copy()
df_filtrado = df_filtrado[(df_filtrado['Anio'] >= anio_inicio) & (df_filtrado['Anio'] <= anio_fin)]
if region_seleccionada:
    df_filtrado = df_filtrado[df_filtrado['NombreRegion'].isin(region_seleccionada)]
if codigo_region_seleccionado:
    df_filtrado = df_filtrado[df_filtrado['CodigoRegion'].isin(codigo_region_seleccionado)]

# Tabla de datos filtrados
st.subheader("Tabla de Datos Filtrados")
st.dataframe(df_filtrado)