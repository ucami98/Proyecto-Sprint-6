
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Sprint 6 Proyect')
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir grafico de dispersion')

if build_histogram:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para la columna odómetro')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.write('Precio del vehiculo segun año del auto.')
fig = px.bar(car_data, x='model_year', y='price', labels={
             'price': 'Price of vehicle'}, height=400)
st.plotly_chart(fig, use_container_width=True)

st.write('Precio del vehiculo segun color')
fig = px.bar(car_data, x='paint_color', y='price', labels={
             'price': 'Price of vehicle'}, height=400)
st.plotly_chart(fig, use_container_width=True)

st.write('Tipos de vehiculos y cantidad de cilindros')
fig = px.pie(car_data, values='cylinders', names='type')
st.plotly_chart(fig, use_container_width=True)
