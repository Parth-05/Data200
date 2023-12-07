## Group Members:
# 1. Name: Parth Chinmaya Marathe Student ID: 017411199
# 2. Name: Srushti Doshi Student ID: 016713203
# 3. Name: Srushtee Upashi Student ID: 016769844
# 4. Name: Ashmit Pareek Student ID: 017401293

## Website URL: https://data200assignment1maratheppy.streamlit.app/

import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Assignment 3")
st.write("Group Members: ")
st.write('1. Name: Parth Chinmaya Marathe Student ID: 017411199')
st.write('2. Name: Srushti Doshi Student ID: 016713203')
st.write('3. Name: Srushtee Upashi Student ID: 016769844')
st.write('4. Name: Ashmit Pareek Student ID: 017401293')

def load_data():
    # getting path of directory
    path = os.path.dirname(__file__)
    # dataset path
    dataset_path = path + '/LifeExpectancy.csv'
    # reading the dataset
    data = pd.read_csv(dataset_path)
    return data

# Main function
def main():
    st.title("Visualizations")

    # Load data
    data = load_data()
    data.columns = data.columns.str.strip()

    # 1. Trend of Average Life Expectancy Over Years with a Year Range Slider:
    st.title('Trend of Average Life Expectancy Over Years')
    year_range = st.slider('Select Year Range', int(data['Year'].min()), int(data['Year'].max()), (2000, 2015))
    filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
    avg_life_expectancy = filtered_data.groupby('Year')['Life expectancy'].mean()

    fig, ax = plt.subplots()
    ax.plot(avg_life_expectancy, marker='o', linestyle='-', color='blue')
    ax.set_title('Average Life Expectancy Over Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Life Expectancy')
    ax.grid(True)
    st.pyplot(fig)
    st.write("Analysis: ")
    st.write('''
           The "Trend of Average Life Expectancy Over Years with a Year Range Slider" chart is a line graph that depicts the average life expectancy across all countries in your dataset for a selected range of years.
             
             This visualization is effective for observing changes and trends in global life expectancy over time.
             
             Here are some key observations and analyses that can be drawn from this chart:
            ''')
    st.write('''
                Global Health Trends:

                The line graph can reveal global trends in life expectancy, such as steady increases, plateaus, or even decreases over certain periods. This can reflect global health improvements, impacts of worldwide health initiatives, or global challenges like pandemics.
                Impact of Historical Events:

                Significant dips or spikes in the graph might correlate with historical events such as economic crises, wars, major disease outbreaks, or significant advancements in healthcare.
                Progress in Healthcare:

                A general upward trend in life expectancy is typically indicative of overall progress in healthcare, including better medical treatments, improved living conditions, and increased health awareness.

            ''')

    # 2. Health Expenditure vs. Life Expectancy with a Country Dropdown:
    country = st.selectbox('Select Country', data['Country'].unique(), key='country_select1')
    country_data = data[data['Country'] == country]

    fig, ax = plt.subplots()
    ax.bar(country_data['Life expectancy'], country_data['Total expenditure'], color='green')
    ax.set_title('Health Expenditure vs. Life Expectancy')
    ax.set_xlabel('Life Expectancy')
    ax.set_ylabel('Total Health Expenditure (% of GDP)')
    ax.grid(True)
    st.pyplot(fig)

    st.write("Analysis: ")
    st.write('''
                The "Health Expenditure vs. Life Expectancy with a Country Dropdown" chart is a bar plot that compares the total health expenditure as a percentage of GDP against life expectancy for a selected country over various years.
             
                This type of chart can provide insights into the relationship between a country's investment in health and the health outcomes of its population. 
             
                Here are some key observations and analyses that can be derived from this chart:
            ''')
    st.write('''
                Trend Analysis:

                The chart allows you to observe trends over time within a selected country. For instance, an increasing trend in health expenditure alongside an increase in life expectancy could indicate that the investments in healthcare are translating into better health outcomes.
                
                Healthcare Investment Efficiency:

                By comparing health expenditure with life expectancy, you can assess the efficiency of healthcare investments. High expenditure with relatively low life expectancy might suggest inefficiencies or other underlying issues affecting health outcomes.
                
                Country-Specific Health Policy Insights:

                Different countries will show different patterns in this chart, reflecting their unique healthcare policies, economic conditions, and public health challenges. This can help in understanding how different health strategies work in different socio-economic contexts.
            ''')

    # 3. Impact of Education on Life Expectancy with a Population Filter:
    data['Population'] = pd.to_numeric(data['Population'], errors='coerce')  # Coerce errors will turn non-convertible values into NaN

    # Filter only numeric columns for grouping
    numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    grouped_data = data[numeric_columns + ['Country']].groupby('Country').mean().reset_index()

    # Now the 'Population' column should be numeric, and the slider should work
    population_threshold = st.slider(
        'Minimum Population', 
        int(grouped_data['Population'].min()), 
        int(grouped_data['Population'].max()), 
        1000000
    )
    filtered_data = grouped_data[grouped_data['Population'] > population_threshold]

    # Plotting
    fig, ax = plt.subplots()
    scatter = ax.scatter(
        filtered_data['Schooling'], 
        filtered_data['Life expectancy'], 
        c=filtered_data['Population'], 
        cmap='viridis', 
        alpha=0.7
    )
    fig.colorbar(scatter, ax=ax, label='Population')
    ax.set_title('Impact of Education on Life Expectancy')
    ax.set_xlabel('Average Years of Schooling')
    ax.set_ylabel('Life Expectancy')
    ax.grid(True)
    st.pyplot(fig)

    st.write("Analysis: ")
    st.write('''
            The "Impact of Education on Life Expectancy with a Population Filter" chart is a scatter plot that visually represents the relationship between the average years of schooling and life expectancy in different countries. 
            The color intensity of each point is proportional to the country's population.
            
            Correlation Between Education and Life Expectancy:

            The chart typically shows a positive correlation between education (measured in average years of schooling) and life expectancy. Countries with higher levels of education often exhibit higher life expectancy, suggesting that education plays a crucial role in health outcomes.
            
            Population Density and Health Outcomes:

            The color intensity, representing population size, can provide additional context. For instance, countries with large populations and low education levels might be areas of concern, indicating a need for investment in education to improve health outcomes.
            ''')


    # 4. Using Population as the size of the bubble
    year = st.selectbox('Select Year', sorted(data['Year'].unique()))
    fig, ax = plt.subplots()
    year_data = data[data['Year'] == year]

    scatter = ax.scatter(year_data['GDP'], year_data['Life expectancy'], 
                         s=year_data['Population'] / 100000, alpha=0.5)

    ax.set_title(f'Bubble Chart for Year {year}')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Life Expectancy')
    ax.grid(True)
    st.pyplot(fig)

    st.write("Analysis: ")
    st.write('''
                The "Bubble Chart for Year" visualization uses GDP per Capita and Life Expectancy as its axes and represents each country as a bubble, with the size of the bubble proportional to the country's population. This type of visualization provides a multi-dimensional view of the data, allowing for several observations and analyses:

                Relationship Between GDP and Life Expectancy:

                The chart often reveals a positive correlation between GDP per Capita and Life Expectancy. Generally, countries with higher GDP per Capita tend to have higher life expectancy. This trend is a common observation in public health, indicating that wealthier countries often have better access to healthcare services.
                Population Size and Global Health:

                The size of the bubbles gives a sense of the population size of each country. Larger bubbles for countries with low GDP per Capita and lower life expectancy can indicate large populations potentially at risk due to poor healthcare systems or economic challenges.
                            
                Identifying Outliers:

                The chart can help in spotting outliers - countries that do not follow the general trend. For example, a country with a high GDP per Capita but relatively low life expectancy might indicate other factors affecting health beyond economic status, such as lifestyle, environmental issues, or healthcare accessibility.
             ''')

    # 5. Health Indicators Over Years
    selected_country = st.selectbox('Select Country', data['Country'].unique(), key='country_select2')
    country_data = data[data['Country'] == selected_country]

    # Selecting relevant health indicators
    indicators = ['Adult Mortality', 'infant deaths', 'under-five deaths', 'HIV/AIDS']

    fig, ax = plt.subplots()
    bottom = None
    for indicator in indicators:
        ax.bar(country_data['Year'], country_data[indicator], bottom=bottom, label=indicator)
        bottom = bottom + country_data[indicator] if bottom is not None else country_data[indicator]

    ax.set_title(f'Health Indicators Over Years for {selected_country}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Indicator Values')
    ax.legend(title='Health Indicators')
    st.pyplot(fig)

    st.write("Analysis: ")
    st.write('''
                The "Health Indicators Over Years" chart is a stacked bar chart that provides a visual representation of various health indicators for a selected country across different years. 
             
                Trend Analysis: The chart allows for the observation of trends over time for each health indicator. For instance, an overall decreasing trend in 'infant deaths' or 'under-five deaths' might indicate improvements in child healthcare and general health conditions in the selected country.

                Comparative Analysis: By observing the relative sizes of different segments in each bar, one can compare the prevalence or impact of different health issues within a year. For example, a large segment for 'HIV/AIDS' in certain years might highlight periods where the disease had a significant impact on the country's health.


            ''')

    # Linear Regression Plot
    filtered_data = data[['Life expectancy', 'GDP']].dropna()

    fig, ax = plt.subplots() # Create a new figure for the linear regression
    sns.regplot(x='GDP', y='Life expectancy', data=filtered_data, scatter_kws={'alpha':0.5}, ax=ax)
    ax.set_title('Linear Regression of Life Expectancy on GDP')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Life Expectancy')
    st.pyplot(fig)
    st.write("The linear regression graph plots Life Expectancy against GDP per Capita, with a regression line showing the general trend or relationship between these two variables.")
    st.write("Observations:")
    st.write('''
                Positive Correlation: The graph indicates a positive correlation between GDP per Capita and Life Expectancy. This means that as GDP per Capita increases, Life Expectancy tends to increase as well.

                Data Spread: The spread of the data points around the regression line suggests variability in how GDP correlates with Life Expectancy. Some countries with lower GDP have higher life expectancies than might be expected based on GDP alone, and vice versa.

                Outliers: There appear to be some outliers, particularly in countries with very high GDP per Capita but not proportionally high Life Expectancy. This could be due to other factors influencing health outcomes in those countries.
            ''')
    
    st.write("Analysis: ")
    st.write('''
                This visualization supports the common understanding that economic wealth, as indicated by GDP per Capita, is a significant factor in determining the health and longevity of a population. 
                
             However, it also highlights that GDP is not the only factor, as variations and outliers suggest the influence of other social, environmental, or healthcare-related factors.
            ''')
    






# Run the app
if __name__ == '__main__':
    main()
