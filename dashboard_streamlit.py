import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
#import SessionState

### Config
st.set_page_config(
    page_title="Precio de las casas en la Region Metropolitana, Chile",
    layout="wide"
)

### HEADER
st.title('')



#delay = pd.read_excel('get_around_delay_analysis.xlsx')

choice_comuna = st.sidebar.selectbox("En qué comuna esta la casa?",\
    ['Buin', 'Calera de Tango', 'Cerrillos', 'Cerro Navia', 'Colina',
       'Conchalí', 'El Bosque', 'Estación Central', 'Huechuraba',
       'Independencia', 'Isla de Maipo', 'La Cisterna', 'La Florida',
       'La Granja', 'La Pintana', 'La Reina', 'Lampa', 'Las Condes',
       'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 'Maipú',
       'Melipilla', 'Ñuñoa', 'Padre Hurtado', 'Paine', 'Pedro Aguirre Cerda',
       'Peñaflor', 'Peñalolén', 'Pirque', 'Providencia', 'Pudahuel',
       'Puente Alto', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca',
       'San Bernardo', 'San Joaquín', 'San Miguel', 'Santiago',
       'Talagante', 'Vitacura'])

choice_comuna = choice_comuna.replace(' ','_')

with open(f'pricing_{choice_comuna}.pkl','rb') as pricing:
    LR = pickle.load(pricing)

dormitorios = st.sidebar.number_input("Indique el numero de habitaciones",1)

banios = st.sidebar.number_input("Indique el numero de baños",1)

mts_utiles = float(st.sidebar.number_input("Indique el metraje util",100))

mts_total = float(st.sidebar.number_input("Indique el metraje total",100))

parkings = float(st.sidebar.number_input("Indique el numero de estacionamientos",1))


X = np.array([[dormitorios,banios,mts_utiles,mts_total,parkings]])

price = LR.predict(X),

st.write(mts_utiles * price)

#st.write("El precio estimado de la casa es :",round(float(price),0)," UF.")

