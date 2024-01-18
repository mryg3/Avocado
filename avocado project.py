import numpy as np
import pandas as pd

# Replace 'your_file.csv' with the actual file path
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'

# Use pandas to read the CSV file
dataset = pd.read_csv(file_path)

# Now 'dataset' contains the data from the CSV file
print(dataset.head())

import streamlit as st

# Load your dataset
file_path = 'Avocado_dataset.csv'
df = pd.read_csv(file_path)

# Streamlit app
st.title('Avocado dataset')

# Display the dataset
st.subheader('Dataset:')
st.dataframe(df)

