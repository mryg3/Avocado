import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_file.csv' with the actual file path
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'

# Use pandas to read the CSV file
dataset = pd.read_csv(file_path)

# Now 'dataset' contains the data from the CSV file
print(dataset.head())

import streamlit as st
# Load dataset to streamlit
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'
df = pd.read_csv(file_path)

# Streamlit 
st.title('vocado Prices and Sales Volume 2015-2023')
st.image("/Users/antoninazhadan/Documents/programming/cute_avocado.png", caption="Cute Avocado", width=200)
st.caption('Designed by Antonina Zhadan')

# Display the dataset
st.subheader('Avocado Dataset:')
st.dataframe(df)

print(f'Name of Columns is: \n {dataset.columns}')
print('Columns in dataset: '.format(dataset.shape[1]))
print('Raws in dataset:'.format(dataset.shape[0]))

# First five rows of my dataset
dataset.head()

#Last five rows of my dataset
dataset.tail()

#showing the info of each column in my dataset
dataset.info()

#see the names of columns
dataset.columns

#rename the columns

dataset.rename(columns={'SmallBags':'Small bags', 'LargeBags':'Large bags', 'XLargeBags':'XL bags'}, inplace=True)

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
avocado_data_cleaned['Small bags'] = avocado_data_cleaned['Small bags'].fillna(avocado_data_cleaned['Small bags'].mean())
avocado_data_cleaned['Large bags'] = avocado_data_cleaned['Large bags'].fillna(avocado_data_cleaned['Large bags'].mean())
avocado_data_cleaned['XL bags'] = avocado_data_cleaned['XL bags'].fillna(avocado_data_cleaned['XL bags'].mean() )

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
    
#Exploring the data

st.title('Exploring more data:')

# Count occurrences of each region
region_counts = dataset['region'].value_counts()

# Display the count of each region
st.header('First 10 Region Counts')
st.table(region_counts.head(10))

st.header('Last 10 region counts')
st.table(region_counts.tail(10))


#I want to see the sum all bags
# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 4))

# Calculate the sum of each bag type across all rows
total_sum_s_bags = dataset['Small bags'].sum()
total_sum_l_bags = dataset['Large bags'].sum()
total_sum_XL_bags = dataset['XL bags'].sum()

# List of bag types and their corresponding sums
bag_types = ['Small bags', 'Large bags', 'XL bags']
sums = [total_sum_s_bags, total_sum_l_bags, total_sum_XL_bags]

# Plot the bar chart
bars = ax.bar(bag_types, sums, color=['red', 'blue', 'black'])
ax.set_title('Total Sum of Each Bag Type')  # Corrected line
ax.set_xlabel('Bag Types')
ax.set_ylabel('Total Sum')

# Display the chart using st.pyplot() based on checkbox state
show_chart = st.checkbox('Check me to see the chart of total sum of all bags')
if show_chart:
    st.pyplot(fig)
else:
    st.write('Bar chart is hidden. Click the checkbox to show it.')

dataset['Date'] = pd.to_datetime(dataset['Date'])
# Group by 'Date' and calculate the average price
average_price_over_time = dataset.groupby('Date')['AveragePrice'].mean()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(18, 10))

# Plot the line chart
ax.plot(average_price_over_time.index, average_price_over_time.values, color='blue', marker='o')
ax.set_title('Average Price Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Average Price')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Display the chart using st.pyplot()
st.pyplot(fig)



# Print data types of all columns
st.write("Data Types of Columns:")
st.write(dataset.dtypes)


# Select only numeric columns for correlation
dataset_numeric = dataset.select_dtypes(include=['float64', 'datetime64[ns]'])
# Display the correlation heatmap
st.header('Correlation Heatmap')
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = sns.heatmap(dataset_numeric.corr(), annot=True)
st.pyplot(fig)



# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the pie chart
ax.pie([total_sum_s_bags, total_sum_l_bags, total_sum_XL_bags], labels=bag_types, autopct='%.2f%%', startangle=90, shadow=True)

# Set chart title and legend
ax.set_title('Distribution of Bag Types', fontweight='bold', fontsize=14)
ax.legend()

# Display the chart using st.pyplot()
st.pyplot(fig)