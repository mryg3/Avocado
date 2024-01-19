import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

st.title('DATA CLEANING')

# Display information about null values before cleaning
st.header("Null values before cleaning: ")
st.write(dataset.isnull().sum())

# Drop rows with any null values
avocado_data_cleaned = dataset.dropna()

# Display information about null values after cleaning
st.header("Null values after cleaning: ")
st.write(avocado_data_cleaned.isnull().sum())

# Drop duplicates
avocado_data_cleaned = avocado_data_cleaned.drop_duplicates()

#Display columns with missing data
col_with_missing_data = dataset.columns[dataset.isnull().any()]
st.header('Columns with missing data: ')
st.write(col_with_missing_data)

#Fill the missing columns with data using mean
avocado_data_cleaned['SmallBags'] = avocado_data_cleaned['SmallBags'].fillna(avocado_data_cleaned['SmallBags'].mean())
avocado_data_cleaned['LargeBags'] = avocado_data_cleaned['LargeBags'].fillna(avocado_data_cleaned['LargeBags'].mean())
avocado_data_cleaned['XLargeBags'] = avocado_data_cleaned['XLargeBags'].fillna(avocado_data_cleaned['XLargeBags'].mean() )

#Drop unecessary columns
avocado_data_cleaned = avocado_data_cleaned.drop(['plu4046', 'plu4225', 'plu4770', 'TotalVolume', 'type'], axis=1)

st.subheader('Cleaned Data: ')
st.write(avocado_data_cleaned)

#Show some interesting plots

#Distribution of Average Price
#fig, ax = plt.subplots(figsize=(10, 8))
#ax.title('Distribution of AveragePrice')
#ax.hist(dataset['AveragePrice'], bins = 20, color='green',density=True)
#ax.xlabel('Average Price')
#ax.ylabel('Density')
#st.pyplot(fig)

#TotalBags and AveragePrice
#fig, ax = plt.subplots(figsize=(10, 8))
#ax.title('TotalBags and AveragePrice')
#ax.scatter(dataset['TotalBags'], dataset['AveragePrice'], color= 'brown', alpha=0.5) #alpha allows to see overlapping points easily
#ax.xlabel('Total Bags')
#ax.ylabel('Average Price')
#st.pyplot(fig)

# Calculate the mean AveragePrice by Region
#average_price_by_region = dataset.groupby('region')['AveragePrice'].mean()

# Plot the bar plot using Pandas plotting
#fig, ax = plt.subplots(figsize=(10, 8))
#average_price_by_region.plot(kind='bar', color='yellow')
#ax.title('AveragePrice by Region')
#ax.xlabel('Region')
#ax.ylabel('Average Price')
#st.pyplot(fig)

# Distribution of Average Price
if st.button('Show Distribution of Average Price chart'):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.hist(dataset['AveragePrice'], bins=20, color='green', density=True)
    ax.set_title('Distribution of AveragePrice')
    ax.set_xlabel('Average Price')
    ax.set_ylabel('Density')
    st.pyplot(fig)

# TotalBags and AveragePrice
if st.button('Show TotalBags and AveragePrice chart'):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.scatter(dataset['TotalBags'], dataset['AveragePrice'], color='brown', alpha=0.5)
    ax.set_title('TotalBags and AveragePrice')
    ax.set_xlabel('Total Bags')
    ax.set_ylabel('Average Price')
    st.pyplot(fig)

# Calculate the mean AveragePrice by Region
average_price_by_region = dataset.groupby('region')['AveragePrice'].mean()

# AveragePrice by Region
if st.button('AveragePrice by Region chart'):
    fig, ax = plt.subplots(figsize=(10, 4))
    average_price_by_region.plot(kind='bar', color='yellow')
    ax.set_title('AveragePrice by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Average Price')
    st.pyplot(fig)