##  Website URL
# https://data200hw3maratheppy.streamlit.app/

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title
st.title("Homework 3")
st.write('Name: Parth Chinmaya Marathe')
st.write('Student ID: 017411199')
# getting path of directory
path = os.path.dirname(__file__)
# dataset path
dataset_path = path + '/toy_dataset.csv'
# reading the dataset
data = pd.read_csv(dataset_path)

gen_count = data['Gender'].value_counts()

# Plot 1
fig1, ax1 = plt.subplots()
ax1.bar(gen_count.index, gen_count.values, color='orange')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Count')
ax1.set_title('Distribution of Gender in Toy Dataset')

st.pyplot(fig1)

df_grouped = data.groupby('City')['Income'].mean().reset_index()

# Plot 2
fig2, ax2 = plt.subplots()
ax2.bar(df_grouped['City'], df_grouped['Income'], color='blue')
ax2.set_xlabel('City')
ax2.set_xticklabels(df_grouped['City'], rotation=45, ha='right')
ax2.set_ylabel('Average Income')
ax2.set_title('Average Income by City')

st.pyplot(fig2)


