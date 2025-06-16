# Diabetes Risk Prediction with Streamlit

This application predicts the risk of diabetes based on user-provided health indicators using a Random Forest model trained on the Pima Indians Diabetes dataset.

## 🚀 Features

- Web interface built with **Streamlit**
- Uses a pre-trained **Random Forest** model
- Simple form to input patient health data
- Displays prediction results in real time

## 🧠 Model

- Model: `RandomForestClassifier`
- Trained on: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Training and export done in [this notebook](https://github.com/4GeeksAcademy/ulla-decision-tree-project-tutorial/blob/main/src/explore.ipynb)

## 🧾 Input Fields

- Number of Pregnancies
- Glucose Level
- Skin Thickness (mm)
- Insulin (mu U/ml)
- Body Mass Index (BMI)
- Diabetes Pedigree Function (DPF)
- Age

## 📦 Project Structure

```
📁 models/
    └── random_forest_classifier.sav
📁 src/
    └── app_streamlit.py
```

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
```

## 📤 Deployment

This app is ready to be deployed on [Render](https://render.com/). Add a `render.yaml` like:

```yaml
services:
  - type: web
    name: diabetes-risk-streamlit
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app_streamlit.py --server.port=$PORT
    plan: free
```

## 👩‍💻 Author

Ulla Aller – [GitHub](https://github.com/ullaom)
