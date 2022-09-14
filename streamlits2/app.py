import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns
import numpy as np

#Cargamos los data frame 
circuits=pd.read_csv("datasets\circuits.csv")
constructor=pd.read_csv("datasets\constructor.csv")
drivers=pd.read_csv("datasets\drivers.csv",encoding="utf-8")
pitstop=pd.read_csv("datasets\pitstop.csv")
#races=pd.read_csv("datasets\races.csv",encoding="utf-8")
#result=pd.read_csv("datasets\result.csv")
#dc=pd.read_csv("datasets\result.csv")
#dc=pd.read_csv()
#dc=pd.read_csv()


st.title("Proyecto individual")
st.markdown("###### ***Pandas-Streamlit***")
st.subheader("Pregunta 1")
st.markdown("###### ***Año con más carreras***")
st.subheader("Pregunta 2")
st.markdown("###### ***Piloto con mayor cantidad de primeros puestos***")
st.subheader("Pregunta 3")
st.markdown("###### ***Nombre del circuito más corrido***")
st.subheader("Pregunta 4")
st.markdown("###### ***Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British***")
st.write("***")
st.write("## Consigna")
st.markdown("[Repo ](https://github.com/FnegreteHenry/PI01_DATA03)")

st.title("Exploracion de datasets")

if st.checkbox("DF circuits"):
    st.dataframe(circuits)

if st.checkbox("DF costructor"):
    st.dataframe(constructor)


if st.checkbox("DF drivers"):
    st.dataframe(drivers)


if st.checkbox("DF pitstop"):
    st.dataframe(pitstop)


if st.checkbox("DF races"):
    st.dataframe(races)


if st.checkbox("DF result"):
    st.dataframe(result)

if st.checkbox("vista"):
  if  st.button("Mostrar"):
        st.write("5HEAD")