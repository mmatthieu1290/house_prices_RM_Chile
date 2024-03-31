import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
#import SessionState

with open('pricing.pkl','rb') as pricing:
    LR = pickle.load(pricing)

with open('preprocessor.pkl','rb') as pre:
    preprocessor = pickle.load(pre)      

### Config
st.set_page_config(
    page_title="Precio de las casas en la Region Metropolitana, Chile",
    layout="wide"
)

### HEADER
st.title('')



#delay = pd.read_excel('get_around_delay_analysis.xlsx')

choice_comuna = st.sidebar.selectbox("En qué comuna esta la casa?",\
    ['QuintaNormal', 'PedroAguirreCerda', 'EstaciónCentral', 'Colina',
       'LaFlorida', 'Maipú', 'SanBernardo', 'Santiago', 'LasCondes',
       'Lampa', 'Quilicura', 'PuenteAlto', 'LaPintana', 'Huechuraba',
       'SanMiguel', 'Ñuñoa', 'LaGranja', 'Pudahuel', 'Independencia',
       'Buin', 'Peñalolén', 'Talagante', 'PadreHurtado', 'Tiltil',
       'LoBarnechea', 'Providencia', 'LaReina', 'Conchalí', 'Peñaflor',
       'ElMonte', 'Macul', 'CaleradeTango', 'Paine', 'LaCisterna',
       'Melipilla', 'Recoleta', 'LoPrado', 'Vitacura', 'LoEspejo',
       'ElBosque', 'Cerrillos', 'Curacaví', 'Renca', 'Pirque',
       'SanJoaquín', 'IsladeMaipo', 'SanRamón', 'CerroNavia',
       'SanJosédeMaipo'])

dormitorios = st.sidebar.number_input("Indique el numero de habitaciones",1)

banios = st.sidebar.number_input("Indique el numero de baños",1)

mts_utiles = float(st.sidebar.number_input("Indique el metraje util",1))

mts_total = float(st.sidebar.number_input("Indique el metraje total",1))

parkings = float(st.sidebar.number_input("Indique el numero de estacionamientos",1))

input_data = pd.DataFrame(columns = ['Comuna', 'Dorms', 'Baths', 'Built Area', 'Total Area', 'Parking'], \
                          data=[[choice_comuna,dormitorios,banios,mts_utiles,mts_total,parkings]])

input_data['Comuna'] = input_data['Comuna'].astype(str)

input_data[[ 'Dorms', 'Baths', 'Built Area', 'Total Area', 'Parking']] = input_data[[ 'Dorms', 'Baths', 'Built Area', 'Total Area', 'Parking']].astype(float)

st.write(input_data)

st.write(dormitorios + banios)

X = preprocessor.transform(input_data[['Comuna', 'Dorms', 'Baths', 'Built Area', 'Total Area', 'Parking']])

#price = LR(X)

#st.write("El precio estimado de la casa es :",float(price))

