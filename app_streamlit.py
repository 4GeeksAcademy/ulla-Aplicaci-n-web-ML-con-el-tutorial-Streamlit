import streamlit as st
import numpy as np
import pickle
import os

# Configurar Streamlit para que escuche en el puerto correcto de Render
st.set_option('server.port', 10000)
st.set_option('server.enableCORS', False)
st.set_option('server.enableXsrfProtection', False)

# Cargar el modelo
model_path = os.path.join("models", "random_forest_classifier.sav")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Título de la app
st.title("Predicción de Riesgo de Diabetes")

# Formulario de entrada de datos
st.subheader("Introduce los datos del paciente:")

pregnancies = st.number_input("Número de embarazos", min_value=0)
glucose = st.number_input("Nivel de glucosa", min_value=0)
skin_thickness = st.number_input("Grosor de piel (mm)", min_value=0)
insulin = st.number_input("Insulina (mu U/ml)", min_value=0)
bmi = st.number_input("IMC", min_value=0.0)
dpf = st.number_input("Historial familiar (DPF)", min_value=0.0)
age = st.number_input("Edad", min_value=0)

# Botón para hacer predicción
if st.button("Predecir"):
    input_data = np.array([[pregnancies, glucose, skin_thickness, insulin, bmi, dpf, age]])
    result = model.predict(input_data)[0]
    if result == 1:
        st.error("Resultado: Positivo para riesgo de diabetes")
    else:
        st.success("Resultado: Negativo (sin riesgo)")
