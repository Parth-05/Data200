import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title
st.title("Homework 4")
st.write('Name: Parth Chinmaya Marathe')
st.write('Student ID: 017411199')
# getting path of directory
path = os.path.dirname(__file__)
# dataset path
dataset_path = path + '/mountain_flowers.csv'
# reading the dataset
mountain_flowers = pd.read_csv(dataset_path)

flower_species = mountain_flowers['name']
petal_lengths = mountain_flowers['petal_length']

# Create a bar chart
plt.bar(flower_species, petal_lengths)

# Add labels and title
plt.xlabel('Flower Species')
plt.ylabel('Petal Lengths')
plt.title('Comparison of Petal Lengths of Mountain Flowers')

# Rotate x-axis labels if they are long
plt.xticks(rotation=45, ha='right')

st.pyplot(plt)
st.write("**Analysis/Observation:**") 
st.write("Thus we can see clearly see from the above graph that: \n"
"1. Violet flower species has the shortest petal length. \n"
"2. Bluebells flower species has the second longest petal length. \n"
"3. Colorado lotus flower species has the longest petal length.")

st.write('**Detailed Data View of Flower Species and Petal Length**')
name_petal_length_df = mountain_flowers[['name', 'petal_length']].rename(columns={'name': 'Flower Species', 'petal_length': 'Petal Length'})
st.write(name_petal_length_df)


