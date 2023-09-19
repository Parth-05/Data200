import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Homework 3")
st.write('Name: Parth Chinmaya Marathe')
st.write('Student ID: 017411199')
file_path = os.path.join(os.getcwd(), "toy_dataset.csv")
path = os.path.dirname(__file__)
myfile_path = path + '/toy_dataset.csv'
print(myfile_path)
st.write(myfile_path)
# dir = path.Path(__file__).abspath()
# sys.append.path(dir.parent.parent)
# path_to_model = './models/final_model.pkl'
data = pd.read_csv(myfile_path)
gen_count = data['Gender'].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(gen_count.index, gen_count.values, color='orange')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Count')
ax1.set_title('Distribution of Gender in Toy Dataset')

st.pyplot(fig1)

df_grouped = data.groupby('City')['Income'].mean().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(df_grouped['City'], df_grouped['Income'], color='blue')
ax2.set_xlabel('City')
ax2.set_xticklabels(df_grouped['City'], rotation=45, ha='right')
ax2.set_ylabel('Average Income')
ax2.set_title('Average Income by City')

st.pyplot(fig2)


