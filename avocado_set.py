import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Downloading my file
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'

# This helps to read the file
dataset = pd.read_csv(file_path)

# Now i have my dataset
print(dataset.head())

import streamlit as st
# Load dataset to streamlit
file_path = '/Users/antoninazhadan/Documents/programming/Avocado_dataset.csv'
df = pd.read_csv(file_path)

# Streamlit 
st.title('Avocado Prices and Sales Volume 2015-2023')
st.image("/Users/antoninazhadan/Documents/programming/cute_avocado.png", caption="Cute Avocado", width=200)
st.caption('Designed by Antonina Zhadan')

# Display the dataset             

st.header('Avocado Dataset:')
st.dataframe(df)

# First five rows of my dataset
dataset.head()

#Last five rows of my dataset
dataset.tail()

#showing the info of each column in my dataset
dataset.info()

#let's see what columns I have
st.write(f'Name of Columns is: ')
dataset.columns

#rename the columns
dataset.rename(columns={'SmallBags':'Small bags', 'LargeBags':'Large bags', 'XLargeBags':'XL bags'}, inplace=True)

# Number of duplicated rows
duplicate_count = dataset.duplicated().sum()
st.header("Number of Duplicated Rows:")
st.write(f"There are {duplicate_count} duplicated rows in the dataset.")

# Summary statistics
columns_to_display = ['AveragePrice', 'TotalVolume', 'Small bags', 'Large bags', 'XL bags']
st.header("Summary Statistics:")
st.write(dataset[columns_to_display].describe().T)



######################################################### DATA CLEANING ################################################################### 

st.title('DATA CLEANING')

# Let's see information about null values
st.header("Null values before cleaning: ")
st.write(dataset.isnull().sum())

# Now, I want to drop rows with any null values
st.text('droped the null values')
avocado_data_cleaned = dataset.dropna()

# Display information about null values after cleaning
st.header("Null values after cleaning: ")
st.write(avocado_data_cleaned.isnull().sum())

# Drop duplicates
avocado_data_cleaned = avocado_data_cleaned.drop_duplicates()

#I want to see the columns with missing data
col_with_missing_data = dataset.columns[dataset.isnull().any()]
st.header('Columns with missing data: ')
st.write(col_with_missing_data)

#Filling the missing columns with data using mean
avocado_data_cleaned['Small bags'] = avocado_data_cleaned['Small bags'].fillna(avocado_data_cleaned['Small bags'].mean())
avocado_data_cleaned['Large bags'] = avocado_data_cleaned['Large bags'].fillna(avocado_data_cleaned['Large bags'].mean())
avocado_data_cleaned['XL bags'] = avocado_data_cleaned['XL bags'].fillna(avocado_data_cleaned['XL bags'].mean() )

#I thought and decided to drop some unecessary columns
avocado_data_cleaned = avocado_data_cleaned.drop(['plu4046', 'plu4225', 'plu4770', 'TotalVolume', 'type'], axis=1)

st.subheader('Cleaned Data: ')
st.write(avocado_data_cleaned)



##################################################### SHOWING SOME INTRESTING PLOTS ##########################################################



# Let's see the distribution of Average Price
if st.button('Show Distribution of Average Price chart'):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.hist(dataset['AveragePrice'], bins=20, color='green', density=True)
    ax.set_title('Distribution of AveragePrice')
    ax.set_xlabel('Average Price')
    ax.set_ylabel('Density')
    st.pyplot(fig)

# Now the chart TotalBags and AveragePrice
if st.button('Show TotalBags and AveragePrice chart'):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.scatter(dataset['TotalBags'], dataset['AveragePrice'], color='brown', alpha=0.5)
    ax.set_title('TotalBags and AveragePrice')
    ax.set_xlabel('Total Bags')
    ax.set_ylabel('Average Price')
    st.pyplot(fig)

# And now I want to calculate the mean AveragePrice by Region
average_price_by_region = dataset.groupby('region')['AveragePrice'].mean()

# AveragePrice by Region
if st.button('AveragePrice by Region chart'):
    fig, ax = plt.subplots(figsize=(10, 4))
    average_price_by_region.plot(kind='bar', color='yellow')
    ax.set_title('AveragePrice by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Average Price')
    st.pyplot(fig)
    
    
    
####################################################### MORE DATA EXPLORATION ##############################################################



st.title('Exploring more data:')

# Exploring each region
region_counts = dataset['region'].value_counts()

# Let's display the count of each region (first 10 and last 10)
st.header('First 10 Region Counts')
st.table(region_counts.head(10))

st.header('Last 10 region counts')
st.table(region_counts.tail(10))


#I want to see the sum all bags
fig, ax = plt.subplots(figsize=(10, 4))

# Let's calculate the sum of each bag type in all rows
total_sum_s_bags = dataset['Small bags'].sum()
total_sum_l_bags = dataset['Large bags'].sum()
total_sum_XL_bags = dataset['XL bags'].sum()

# List of bag types and their sums
bag_types = ['Small bags', 'Large bags', 'XL bags']
sums = [total_sum_s_bags, total_sum_l_bags, total_sum_XL_bags]

# Plot the bar chart by Total sum of each bag type
bars = ax.bar(bag_types, sums, color=['red', 'blue', 'black'])
ax.set_title('Total Sum of Each Bag Type')  
ax.set_xlabel('Bag Types')
ax.set_ylabel('Total Sum')

# Let's display the chart using st.pyplot and creating a checkbox
show_chart = st.checkbox('Check me to see the chart of total sum of all bags')
if show_chart:
    st.pyplot(fig)
else:
    st.write('Chart is hidden. Click me to show it.')

#Let's convert "Data" into a datetime format
dataset['Date'] = pd.to_datetime(dataset['Date'])
# I want to add radio button to select the year
selected_year = st.radio("Select Year", sorted(dataset['Date'].dt.year.unique()))
# Let's see the data based on the selected year
filtered_data = dataset[dataset['Date'].dt.year == selected_year]
fig, ax = plt.subplots(figsize=(18, 10))
ax.plot(filtered_data['Date'], filtered_data['AveragePrice'], color='blue', marker='o')
ax.set_title(f'Average Price Over Time - {selected_year}')
ax.set_xlabel('Date')
ax.set_ylabel('Average Price')
st.pyplot(fig)

# In order to see better the chart I'm Rotateting x-labels for better visibility
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Print data types of all columns
st.write("Data Types of Columns:")
st.write(dataset.dtypes)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the pie chart by S S bags, L bags and XL bags
ax.pie([total_sum_s_bags, total_sum_l_bags, total_sum_XL_bags], labels=bag_types, autopct='%.2f%%', startangle=90, shadow=True)
ax.set_title('Distribution of Bag Types', fontweight='bold', fontsize=14)
ax.legend()
st.pyplot(fig)

# Making correlation (using only numerical values)
dataset_numer = dataset.select_dtypes(include=['float64', 'datetime64[ns]'])
# Let's see the correlation heatmap
st.header('Correlation Heatmap')
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = sns.heatmap(dataset_numer.corr(), annot=True)
st.pyplot(fig)