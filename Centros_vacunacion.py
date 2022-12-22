import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title('Centros de Vacunación COVID-19')
st.write('#### Se muestran los centros de vacunación programados según ubicación geográfica \
        a nivel nacional del territorio peruano')

df_cv = pd.read_csv('CV_depurado.csv')
df_de = pd.read_csv('departamentos.csv')

st.write('')
st.write('')
opc_dep = st.selectbox('Seleccione departamento',
        df_de['departamento'])

if (opc_dep == 'TODOS'):
        total = df_cv['id_centro_vacunacion'].count()
        st.write('#### Total de centros de vacunación: {}'.format(total))        
        st.map(df_cv)
        st.write('Fuente: https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion')
        st.write('')
        st.write('')
        st.write('###### Clic en la cabecera de columna para ordenar ascendente/descente')
        st.dataframe(df_cv)
else:
        df_filtrado = df_cv[df_cv['departamento'] == opc_dep]
        total = df_filtrado['id_centro_vacunacion'].count()
        st.write('Total de centros de vacunación: {}'.format(total))        
        st.map(df_filtrado)
        st.write('Fuente: https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion')
        st.write('')
        st.write('')
        st.write('###### Clic en la cabecera de cada columna para ordenar ascendente/descente')
        st.dataframe(df_filtrado)

st.write('')
#st.write('### Centro de vacunación por departamento')        
barras_cv = df_cv.groupby(by=['departamento']).count()
barras_cv = barras_cv.drop(['id_ubigeo', 'nombre', 'lat', 'lon', 
                                'entidad_administra', 'id_eess'], axis=1)
barras_cv = barras_cv.rename(columns={'id_centro_vacunacion':'numero de centros de vacunacion'})
barras_cv = barras_cv.reset_index()
barras_cv = barras_cv.sort_values(by = 'numero de centros de vacunacion')

fig = px.bar(barras_cv, y = 'departamento', x = 'numero de centros de vacunacion', 
             text = 'numero de centros de vacunacion', height=800, width=800, 
             orientation='h', labels={"departamento":"",
                                      "numero de centros de vacunacion":''})

fig.update_traces(textposition='outside', textfont_size = 14)
#para colocar los números fuera de las barras
fig.update_traces(texttemplate='%{text:.2s}')

fig.update_layout(font=dict(size=16), showlegend=False, #ocultra leyendas
                  title='Número de centros de vacunación por departamento',
                  xaxis=dict(showticklabels=False),
                  yaxis_tickfont_size=14) #ocultar ticks
           
#fig.update_yaxes(categoryorder = 'total ascending')
fig.update_yaxes(categoryorder = 'total ascending') #ordenar barras
st.write(fig)

st.write('')



