import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') 


st.header('Cuadro de Mandos: Análisis de Vehículos')


st.write('### Distribución del Inventario')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
    st.write('Construyendo un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)

# Crear una sección para el Gráfico de Dispersión
st.write('### Relación Precio vs. Kilometraje')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Construyendo un gráfico de dispersión para precio y odómetro')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
    