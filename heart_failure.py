# -*- coding: utf-8 -*-
"""Heart_Failure.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10_MYKVgtXpHtwK-pbphHCaye8n1Y-VBL
"""

import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

filename = 'decision_tree_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title('Heart Failure Prediction App')
st.subheader('Please enter your data:')

df = pd.read_csv('features.csv')
columns_list = df.columns.to_list()

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    prediction = loaded_model.predict(df)
    prediction_text = np.where(prediction == 1, 'Yes', 'No')
    st.subheader('Heart Failure:')
    st.write(prediction_text)