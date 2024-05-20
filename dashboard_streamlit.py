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
st.title('Simulador de precios en la Region Metropolitana, Chile')



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

with open(f'pricings/pricing_{choice_comuna}.pkl','rb') as pricing:
    LR = pickle.load(pricing)

dormitorios = st.sidebar.number_input("Indique el numero de habitaciones",1)

banios = st.sidebar.number_input("Indique el numero de baños",1)

mts_utiles = float(st.sidebar.number_input("Indique el metraje util",min_value = 0.0, value = 100.0, step = 5.0))


mts_total = float(st.sidebar.number_input("Indique el metraje total",min_value = mts_utiles, step = 5.0))

X = np.array([[mts_utiles,mts_total,float(dormitorios)+float(banios)]])

if LR.coef_[2] < 0:
  
  LR.coef_[0] = 0.1

price = mts_utiles * LR.predict(X)[0],

#st.write(price)

st.write("El precio estimado de la casa es :",round(float(price[0]),0)," UF.")

