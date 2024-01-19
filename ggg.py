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
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'
df = pd.read_csv(file_path)

# Streamlit app
st.title('Avocado dataset')
st.image("/Users/antoninazhadan/Documents/programming/cute_avocado.png", caption="Cute Avocado", width=200)
st.caption('Designed by Antonina Zhadan')

# Display the dataset
st.subheader('Avocado Prices and Sales Volume 2015-2023:')
st.dataframe(df)

print(f'Name of Columns is: \n {dataset.columns}')
print('Columns in dataset: '.format(dataset.shape[1]))
print('Raws in dataset:'.format(dataset.shape[0]))
# Display the first few rows of the dataset

dataset.head()
dataset.info()

# Check for and count duplicated rows
duplicate_count = dataset.duplicated().sum()
print(f"Number of duplicated rows: {duplicate_count}")

# Summary statistics
dataset.describe().T


#DATA CLEANING 

# Display information about null values before cleaning
print("Null values before cleaning:")
print(dataset.isnull().sum())

# Drop rows with any null values
avocado_data_cleaned = dataset.dropna()

# Display information about null values after cleaning
print("\nNull values after cleaning:")
print(avocado_data_cleaned.isnull().sum())

# Drop duplicates
avocado_data_cleaned = avocado_data_cleaned.drop_duplicates()

#Display columns with missing data
col_with_missing_data = dataset.columns[dataset.isnull().any()]
print('Columns with missing data: ')
print(col_with_missing_data)

