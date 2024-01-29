#!/usr/bin/env python
# coding: utf-8

# Library Imports:
# 
# The code starts by importing two important libraries: numpy for numerical operations and pandas for data manipulation.
# Exploring Input Directory:
# 
# The os.walk function is used to explore the contents of the input directory in Kaggle notebooks.
# It iterates through the directory structure, capturing the current directory (dirname), subdirectories (denoted by _), and file names (filenames).
# Printing File Paths:
# 
# For each file found in the input directory, the code prints the full path of the file using os.path.join(dirname, filename).
# Purpose:
# 
# This code is useful when working on Kaggle, as it helps to quickly list all the files in the input directory. Kaggle typically places datasets in the '/kaggle/input/' directory, and this code helps you see what data is available for analysis.
# Comments:
# 
# The comments in the code provide explanations for each step, making it easier to understand the purpose of the code.
# In summary, this code is a simple script that prints the full paths of all files in the Kaggle input directory, facilitating data exploration and analysis in Kaggle notebooks.

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# In[5]:


import os # Add this line to import the 'os' module

# Specify the path using a raw string
path = r'C:\kaggle\input'

# Exploring the specified directory
for dirname, _, filenames in os.walk(path):
    for filename in filenames:
        # Printing the full path of each file in the specified directory
        print(os.path.join(dirname, filename))


# In[7]:


import pandas as pd

# read in the ab_test.csv file
ab_test = pd.read_csv('C:\Users\hatic\OneDrive\Desktop\Kaggle\input')

# read in the countries_ab.csv file
countries = pd.read_csv('/kaggle/input/countries_ab.csv')

# merge the two files on the id field
data = pd.merge(ab_test, countries, on='id')

# preview the merged data
print(data.head())


# In[8]:


import pandas as pd

# Raw string containing the directory path
directory_path = r'C:\Users\hatic\OneDrive\Desktop\Kaggle\input'

# Assuming 'ab_test.csv' is the CSV file you want to read
file_path = fr'{directory_path}\ab_test.csv'

# Read the CSV file
ab_test = pd.read_csv(file_path)

# Raw string containing the directory path
directory_path = r'C:\Users\hatic\OneDrive\Desktop\Kaggle\input'

# Assuming 'ab_test.csv' is the CSV file you want to read
file_path = fr'{directory_path}\countries_ab.csv'

# Read the CSV file
countries_ab = pd.read_csv(file_path)


# In[9]:


#MERGE the two files on the id field
data=pd.merge(ab_test, countries_ab, on='id')

#preview the MERGED DATA
print(data.head())


# In[10]:


df.info()
print(df.shape)


# In[11]:


df=data.copy()
df.info()
print(df.shape)
#In Pandas, the shape attribute of a DataFrame returns a tuple representing the dimensions of the DataFrame. 
#The tuple contains two elements: the number of rows and the number of columns.



# In[12]:


print(df.columns)


# In[13]:


#Based on the information from df.info(), we have a DataFrame with 294,478 entries and 5 columns.
#Here are some common data cleansing steps we might consider based on the provided information:

#Convert Timestamp to DateTime:

#It seems like the 'timestamp' column is currently of type 'object'. 
#..to convert it to a datetime data type for easier handling of date and time operations.

#df['timestamp'] = pd.to_datetime(df['timestamp'])
#Check for Duplicates:

#Check for and remove any duplicate rows in the DataFrame.

#df = df.drop_duplicates()
#Handle Missing Values (if any):

#Check if there are any missing values in the DataFrame and handle them accordingly. 
#In your case, based on df.info(), it seems there are no missing values 
#(Non-Null Count is the same as the total count).

#Ensure Data Consistency:

#Check if the data in the 'group' and 'landing_page' columns are consistent and make corrections if needed.

# Checking unique values in 'group' column
#print(df['group'].unique())

# Checking unique values in 'landing_page' column
#print(df['landing_page'].unique())
#Review Data Types:

#Ensure that the data types of each column are appropriate for their contents. 
#for example, 'converted' column seems to be of type int64, which is appropriate for binary values.


# In[14]:


# Assuming df is your original DataFrame

# Convert 'timestamp' to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Drop duplicates
df = df.drop_duplicates()

# Check for missing values (if any)
df.info()

# Check unique values in 'group' and 'landing_page' columns
print(df['group'].unique())
print(df['landing_page'].unique())


# In[15]:


# Assuming df is original DataFrame

# Check the column names in the DataFrame

print(df.columns)


# In[16]:


# Check the column names in the DataFrame
print(df.columns)

# Convert 'timestamp' to datetime if it exists
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
else:
    print("Column 'timestamp' not found in the DataFrame.")


# In[17]:


# Drop duplicates
df = df.drop_duplicates()

# Check for missing values (if any)
df.info()


# In[18]:


# Check unique values in 'group' and 'landing_page' columns
print(df['group'].unique())


# In[19]:


print(df['landing_page'].unique())


# In[20]:


#The error indicates that the columns 'group' and 'landing_page' are not present in your DataFrame. 
#This could be due to issues such as typos or the columns not being loaded correctly.

#Before attempting to print unique values, you should check the actual column names in your DataFrame using df.columns. 
#Here's an updated version of the code:

# Check the column names in the DataFrame
print(df.columns)

# Check if 'group' and 'landing_page' are in the DataFrame
if 'group' in df.columns and 'landing_page' in df.columns:
    # Print unique values in 'group' column
    print(df['group'].unique())
    
    # Print unique values in 'landing_page' column
    print(df['landing_page'].unique())
else:
    print("Columns 'group' and/or 'landing_page' not found in the DataFrame.")


# In[21]:


#data cleaning steps can vary based on the specific characteristics of your dataset. 
#Always tailor your data cleaning approach to the unique requirements and challenges of your data.
#Data cleaning involves various tasks to ensure that the dataset is accurate, consistent, and ready for analysis. 
#Here are some additional examples of data cleaning tasks using pandas:

#Handling Missing Values:

#Identify and handle missing values. You can use methods like isnull(), dropna(), or fillna().

# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df['column_name'].fillna(value, inplace=True)


# In[22]:


print(df.columns)


# In[23]:


# Correct the column name if there's a typo
df['correct_column_name'].fillna(value, inplace=True)


# In[24]:


# Check the column names in the DataFrame
print(df.columns)


# In[25]:


# Fill missing values in the 'con_treat' column
df['con_treat'].fillna(value, inplace=True)


# In[26]:


#It looks like you're encountering a NameError because the variable value is not defined 
#before you try to use it in the fillna method. 
#You need to specify a value that you want to use for filling missing values.

#Replace 'your_value' with the actual value you want to use for filling missing values in the 'con_treat' column. 
#It could be a specific number, string, or any other value that makes sense in the context of your data.

#If you want to fill missing values with the mean, median, or some other statistic, 
#you can use the appropriate method. For example, filling missing values with the mean:





# In[27]:


# Fill missing values in the 'con_treat' column with a specific value (replace 'your_value' with the value you want)
df['con_treat'].fillna('your_value', inplace=True)


# In[ ]:


# Fill missing values in the 'con_treat' column with the mean
df['con_treat'].fillna(df['id'].mean(), inplace=True)


# In[32]:


import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame
# Use value_counts() to get the count of unique values in 'country'
country_counts = data['country'].value_counts()

# Plotting a bar chart
plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar', color='blue')
plt.title('User IDs by Country')
plt.xlabel('Country')
plt.ylabel('Count')

# Adding labels on top of each bar
for i, count in enumerate(country_counts):
    plt.text(i, count + 10, str(count), ha='center', va='bottom')

plt.show()


# In[40]:


import matplotlib.pyplot as plt

# Assuming data is your DataFrame
country_data = data.groupby('country')['converted'].mean().reset_index()


# Assuming country_data is your DataFrame with country-wise conversion rates
plt.figure(figsize=(12, 6))
plt.bar(country_data['country'], country_data['converted'], color='skyblue')
plt.title('Conversion Rates by Country')
plt.xlabel('Country')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=45, ha='right')  # Rotate country names for better visibility

# Adding labels on top of each bar
for i, row in country_data.iterrows():
    plt.text(i, row['converted'] + 0.005, f'{row["converted"]:.3f}', ha='center', va='bottom')

plt.show()


# In[43]:


print(data.columns)


# In[44]:


print(data.head())


# In[46]:


data.info()


# In[47]:


data.describe()


# Data Cleaning

# In[50]:


#Handling Missing Values:

#Remove Rows with Missing Values:

df_cleaned = df.dropna()


# In[54]:


#Fill Missing Values with a Specific Value:
df['id'].fillna(count, inplace=True)


# In[58]:


#Handling Duplicates:

#Drop Duplicate Rows:

df.drop_duplicates(inplace=True)


# In[62]:


#Identify and Drop Duplicate Rows Based on a Specific Column:

df.drop_duplicates(subset='converted', keep='first', inplace=True)

df.drop_duplicates(subset='id', keep='first', inplace=True)



# In[64]:


#Changing Data Types:

# Assuming df is your DataFrame
df['id'] = df['id'].astype(int)

#This will convert the 'id' column to an integer data type. Note that this assumes that 
#there are no non-integer values in the 'id' column. 
#If there are non-integer values, you may need to clean or handle those values before converting the data type.

#Always be cautious when changing data types, and make sure that it makes sense for your analysis. 
#If you encounter any issues during the conversion, 
#it's a good idea to inspect the unique values in the 'id' column and handle any anomalies appropriately.


# In[73]:


# group the data by country and calculate the conversion rates for each group
country_data = data.groupby('country')['converted'].mean().reset_index()

# create a scatter plot of conversion rates by country
plt.scatter(country_data['country'], country_data['converted'])
plt.title('Conversion Rates by Country')
plt.xlabel('Country')
plt.ylabel('Conversion Rate')
plt.ylim(0, 0.16)
for i, row in country_data.iterrows():
    plt.text(row['country'], row['converted'] + 0.005, f'{row["converted"]:.3f}', ha='center', va='bottom')
plt.show()


# In[74]:


import numpy as np
import pandas as pd
from scipy import stats

# Assuming data is your DataFrame
control = data[data['page'] == 'old_page']
treatment = data[data['page'] == 'new_page']

# Loop through each country and calculate conversion rates
for country in data['country'].unique():
    # Filter the data by country and control/treatment groups
    country_control = control[control['country'] == country]['converted']
    country_treatment = treatment[treatment['country'] == country]['converted']
    
    # Calculate the conversion rates for each group
    control_rate = np.mean(country_control)
    treatment_rate = np.mean(country_treatment)
    
    # Conduct a hypothesis test to determine whether the difference in rates is significant
    _, p_value = stats.ttest_ind(country_control, country_treatment)
    
    # Print the results
    print(f'Country: {country}')
    print(f'Control conversion rate: {control_rate:.4f}')
    print(f'Treatment conversion rate: {treatment_rate:.4f}')
    print(f'P-value: {p_value:.4f}')
    
    if p_value < 0.05:
        print('Statistically significant difference\n')
    else:
        print('No statistically significant difference\n')


# This Python code performs the analysis, splitting the data into control and treatment groups, 
# calculating conversion rates for each country, and conducting a hypothesis test using the t-test.
# The results are printed for each country, indicating 
# whether there is a statistically significant difference in conversion rates between the control and treatment groups.

#  The provided analysis covers different statistical methods for A/B testing, each providing insights into whether the new page is better than the old page. Let's summarize the key points for each method:
# 
# Binomial Proportion Confidence Intervals:
# 
# Calculate Confidence Intervals (CI) for both Pnew and Pold.
# If CI intervals overlap, there's not enough evidence to reject the Null Hypothesis.
# If CI intervals don't overlap, one page may be considered better than the other.
# In the example, CI intervals overlap, indicating no significant difference.
# Z-test:
# 
# Use z-test to calculate the z-score and p-value for proportions.
# If p-value > 0.05, do not reject the Null Hypothesis.
# In the example, p-value is approximately 0.9, indicating no significant difference.
# Hypothesis testing on d̂ and Effect Size:
# 
# Consider the difference between Pnew and Pold (d̂).
# Calculate Confidence Intervals using the standard deviations.
# Check if 0 lies outside the CIdiff. If yes, the change is statistically significant.
# Consider practical significance if Dmin is outside CIdiff.
# In the example, the change is not statistically or practically significant.
# Sign Test:
# 
# Count the number of days the treatment conversion is greater than the control.
# Use a sign test for one-sided hypothesis testing.
# In the example, p-value > 0.05, indicating no significant difference.
# Chi-Squared Test:
# 
# Construct a 2x2 contingency table for observed frequencies.
# Use the Chi-Squared test to check for a relationship between conversion and treatment/control.
# In the example, p-value > 0.05, indicating no significant relationship.
# In summary, all the methods employed in the analysis suggest that there is no significant evidence to reject the Null Hypothesis, indicating that the new page is not better than the old page. Each method provides a different perspective on the data, contributing to a comprehensive understanding of the A/B test results.

# In[ ]:




