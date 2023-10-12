## Group Members:
# 1. Name: Parth Chinmaya Marathe Student ID: 017411199
# 2. Name: Srushti Doshi Student ID: 016713203
# 3. Name: Srushtee Upashi Student ID: 016769844
# 4. Name: Ashmit Pareek Student ID: 017401293

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title
st.title("Assignment 1")
st.write("Group Members: ")
st.write('1. Name: Parth Chinmaya Marathe Student ID: 017411199')
st.write('2. Name: Srushti Doshi Student ID: 016713203')
st.write('3. Name: Srushtee Upashi Student ID: 016769844')
st.write('4. Name: Ashmit Pareek Student ID: 017401293')

def load_data():
    # getting path of directory
    path = os.path.dirname(__file__)
    # dataset path
    dataset_path = path + '/toy_dataset.csv'
    # reading the dataset
    data = pd.read_csv(dataset_path)
    return data

# Main function
def main():
    st.title("Dataset Visualizations")

    # Load data
    data = load_data()

    # Creating dropdown for selecting city as filter
    selected_city = st.selectbox("Choose a city", data['City'].unique())
    #filtering data based on selected city
    filtered_data = data[data['City'] == selected_city]

    # 1. Histogram of Age
    plt.title("Age Distribution in " + selected_city)
    plt.hist(filtered_data['Age'], bins=30, color='blue', alpha=0.7)
    plt.xlabel("Age")
    plt.ylabel("Count")
    st.pyplot(plt)
    plt.clf()  # Clear the plot to ensure no overlap with the next plots.
    #Plot Analysis
    st.write("Analysis: ")
    st.write("The histogram plot shows the distribution of ages in " + selected_city +".")

    # 2. Bar chart of Illness count
    plt.title("Illness Count in " + selected_city)
    illness_counts = filtered_data['Illness'].value_counts()
    illness_counts.plot(kind='bar', color=['blue', 'red'])
    plt.xlabel("Illness")
    plt.ylabel("Count")
    st.pyplot(plt)
    plt.clf()  # Clear the plot to ensure no overlap with the next plots.
    st.write("Analysis: ")
    st.write("The bar chart represents the count of people with and without illness in " + selected_city +".")

    # 3. Pie chart of Gender distribution
    plt.title("Gender Distribution in " + selected_city)
    gender_counts = filtered_data['Gender'].value_counts()
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(plt)
    plt.clf()  # Clear the plot to ensure no overlap with the next plots.
    st.write("Analysis: ")
    st.write("The pie chart shows the gender distribution in " + selected_city +".")


    # 4. Line chart of Age vs Average Income
    plt.title("Age vs Average Income")
    avg_income_by_age = filtered_data.groupby('Age')['Income'].mean()
    avg_income_by_age.plot(kind='line', color='blue', marker='o')
    plt.xlabel("Age")
    plt.ylabel("Average Income")
    plt.title("Age vs Average Income")
    st.pyplot(plt)
    plt.clf()  # Clear the plot to ensure no overlap with the next plots.
    st.write("Analysis: ")
    st.write("The line shows the relationship between age and average income in " + selected_city +".")

    # 5. Average Income by City
    plt.title("Average Income by City")
    avg_income = data.groupby('City')['Income'].mean()
    avg_income.plot(kind='bar', color='skyblue')
    plt.ylabel("Average Income")
    st.pyplot(plt)
    plt.clf()  # Clear the plot to ensure no overlap with the next plots.
    st.write("Analysis: ")
    st.write("The bar chart shows the average income for each city in the entire dataset.")

# Run the app
if __name__ == '__main__':
    main()
