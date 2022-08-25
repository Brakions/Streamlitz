import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualizaciones")
st.markdown("##### Visualizaciones")
st.subheader("Clase ")
st.write("***")
st.write("## Material")
st.markdown("[repo](https://share.streamlit.io/signup)")

st.title("Exploracion")

if st.checkbox("Mostrar"):
    st.write("Hi")

if st.checkbox("vista"):
  if  st.button("Mostrar"):
        st.write("5HEAD")