import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
#Utilizamos pathlib para cambiar el Path
daces_csv = Path('datasets\daces.csv').parents[1] / "datasets\daces.csv"  
#daces=pd.read_csv(daces_csv)

constructor_csv = Path("datasets\constructor.csv").parents[1] / "datasets\constructor.csv"  
drivers_csv = Path("datasets\drivers.csv").parents[1] / "datasets\drivers.csv"
daces_csv = Path('datasets\daces.csv').parents[1] / "datasets\daces.csv"
result_csv = Path("datasets\desult.csv").parents[1] / "datasets\desult.csv"
circuits_csv = Path("datasets\circuits.csv").parents[1] / "datasets\circuits.csv"
pitstop_csv = Path("datasets\pitstop.csv").parents[1] / "datasets\pitstop.csv"

#Cargamos los data frame 
circuits=pd.read_csv(circuits_csv )
constructor=pd.read_csv(constructor_csv)
drivers=pd.read_csv(drivers_csv)
pitstop=pd.read_csv(pitstop_csv)
races=pd.read_csv(daces_csv)
result=pd.read_csv(result_csv )
#dc=pd.read_csv()
#dc=pd.read_csv()


st.title("Proyecto individual")
st.markdown("###### ***Pandas-Streamlit***")
st.subheader("Pregunta 1")
if st.checkbox(" Año con más carreras"):
    if  st.button("Año | Carreras"):
        st.write(races.value_counts("year").head(1))
st.subheader("Pregunta 2")
if st.checkbox("Piloto con mayor cantidad de primeros puestos"):
    if  st.button("ID | Primeros puestos"):
        st.write(result[result["position"]=="1"].value_counts("driverId").head(1))
        st.markdown("###### Id   , Veces")
    if  st.button("Piloto INFO"):
        st.write(drivers[drivers["driverId"]==1])
        
#st.markdown("###### ***Piloto con mayor cantidad de primeros puestos***")
st.subheader("Pregunta 3")
if st.checkbox("Nombre del circuito más corrido"):
    if  st.button("Nombre | Veces recorrido"):
        st.write(races.value_counts("name").head(1))
#st.markdown("###### ***Nombre del circuito más corrido***")
st.subheader("Pregunta 4")
#JOIN DE 2 DATASETS
resul_total=pd.merge(result,drivers, on="driverId")
#SOLO AMERICAN
RA=resul_total[resul_total["nationality"]=="American"]
#SOLO BRITISH
RB=resul_total[resul_total["nationality"]=="British"]
#Resultado general piloto con mas puntos
resul_total["driverRef"].value_counts("points")
#Resultado piloto con mas puntos(AMERICAN)
RA["driverRef"].value_counts("points")
#Resultado piloto con mas puntos(BRITISH)
RB["driverRef"].value_counts("points")
#Join de 3 data sets
result_constructor_total=pd.merge(resul_total,constructor,on="constructorId")
#SOLO AMERICAN
CA=result_constructor_total[result_constructor_total["nationality_x"]=="American"]
#SOLO BRITISH
CB=result_constructor_total[result_constructor_total["nationality_x"]=="British"]
#Resultado general constructor con mas puntos
result_constructor_total["constructorRef"].value_counts("points")
#Resultado cosntructor con mas puntos(AMERICAN)
CA["constructorRef"].value_counts("points")
#Resultado constructor con mas puntos(BRITISH)
CB["constructorRef"].value_counts("points")

if st.checkbox("Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British"):
    
    if  st.button("American"):
        st.write(RA["driverRef"].value_counts("points").head(1))
    if  st.button("British"):
        st.write(RB["driverRef"].value_counts("points").head(1))

if st.checkbox("Constructor con mayor cantidad de puntos en total"):
    
    if  st.button("American"):
        st.write(CA["constructorRef"].value_counts("points").head(1))
    if  st.button("British"):
        st.write(CB["constructorRef"].value_counts("points").head(1))
#st.markdown("###### ***Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British***")
st.write("***")
st.write("## Consigna")
st.markdown("[Repo ](https://github.com/FnegreteHenry/PI01_DATA03)")

st.title("Exploracion de datasets")

if st.checkbox("Circuits"):
    st.dataframe(circuits.head())

if st.checkbox("Costructor"):
    st.dataframe(constructor.head())


if st.checkbox("Drivers"):
    st.dataframe(drivers.head())


if st.checkbox("Pitstop"):
    st.dataframe(pitstop.head())


if st.checkbox("Races"):
    st.dataframe(races.head())


if st.checkbox("Result"):
    st.dataframe(result.head())

