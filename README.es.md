
# Aplicación Web de Predicción de Riesgo de Diabetes

Esta aplicación web utiliza un modelo de Machine Learning para predecir el riesgo de diabetes en pacientes, a partir de variables clínicas como nivel de glucosa, índice de masa corporal, edad, entre otros.

## 🧠 Modelo

El modelo utilizado es un **Random Forest Classifier** entrenado previamente con el dataset de diabetes de Pima Indians, disponible en muchos repositorios públicos como Kaggle o UCI.

Las variables utilizadas son:
- Número de embarazos
- Nivel de glucosa
- Grosor de piel (SkinThickness)
- Insulina
- IMC (Índice de Masa Corporal)
- Historial Familiar (DiabetesPedigreeFunction)
- Edad

El modelo se encuentra guardado como archivo `.sav` en la carpeta `/models`.

## 💻 Interfaz Web con Streamlit

La aplicación ha sido desarrollada con **Streamlit**, lo que permite una experiencia interactiva, fácil de usar y ligera. El usuario puede introducir sus datos en un formulario y obtener una predicción inmediata sobre su riesgo de padecer diabetes.

### Captura de pantalla

![Streamlit App](https://github.com/ullaom/ulla-Aplicaci-n-web-ML-con-el-tutorial-Streamlit/assets/your_screenshot.png)

## 🚀 Cómo usar la aplicación localmente

1. Clona este repositorio:
```bash
git clone https://github.com/ullaom/ulla-Aplicaci-n-web-ML-con-el-tutorial-Streamlit.git
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app_streamlit.py
```

4. Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

## 🌐 Despliegue en Render

La aplicación también está desplegada en línea mediante Render. Puedes acceder desde aquí:

🔗 https://ullaom-machine-learning-python-template.onrender.com

## 📁 Estructura del Proyecto

```
├── app_streamlit.py       <- Script principal de la app Streamlit
├── models/
│   └── random_forest_classifier.sav   <- Modelo guardado
├── requirements.txt       <- Lista de dependencias
├── README.md              <- Documentación (en inglés)
└── README.es.md           <- Documentación (en español)
```

## 👩‍💻 Autora

**Ulla Aller**  
Bootcamp de Ciencia de Datos y Machine Learning  
4Geeks Academy (2025)