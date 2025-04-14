#!/usr/bin/env python
# coding: utf-8

# # First importing important libraries to read and analyse data through visualization
# 

# In[45]:


import pandas as pd


# In[46]:


import matplotlib.pyplot as plt


# In[47]:


import seaborn as sns


# In[4]:


df=pd.read_csv("water potability.csv")


# In[5]:


df


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[10]:


# Quick statistical summary
df.describe()


# # Handling Missing values

# In[13]:


# Total missing values per column
df.isnull().sum()

ph has missing values

Sulfate has missing values

Trihalomethanes has missing values
# In[14]:


# Fill missing values with mean (can also try median)

df['ph'].fillna(df['ph'].mean(), inplace=True)


# In[15]:


df['Sulfate'].fillna(df['Sulfate'].mean(), inplace=True)


# In[16]:


df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean(), inplace=True)


# In[17]:


# If you want to Drop rows where data is missing
#df.dropna(inplace=True)
# or you can also write this code :- df.fillna(df.mean(),inplace=True)


# In[18]:


df.isnull().sum()


# In[32]:


df.describe()


# # Univariate Analysis

# In[20]:


#df.hist(figsize=(14,14))
#plt.show()

df.hist(figsize=(14,14))
plt.suptitle('Distribution of All Numerical Features', fontsize=16)
plt.show()


# Univariate analysis reveals clear differences in feature distributions, with some values skewed toward lower ranges and others showing outlier-heavy tails. The target variable is slightly imbalanced, and potential outliers were detected, especially for solids and sulfate content.

# # BoxPlot to detect outliers

# Boxplot basically shows 5 number summary i.e. Minimum , 25th percentile(Q1) , Median , 75th Percentile(Q3) , Maximum value. here all the values that fall above or below the boxplots , they are ploted as dots. These dots are called the outliers.

# In[21]:


plt.figure(figsize=(6,4))
sns.boxplot(x=df['Solids'], color='lightcoral')
plt.title('Boxplot of Solids')
plt.show()


# # Function to remove outliers

# In[33]:


data=df


# In[35]:


parameters=['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity','Potability']


# In[36]:


# Function to remove outliers
def remove_outliers(data,parameters):
    for parameter in parameters:
        Q1=data[parameter].quantile(0.25)
        Q3=data[parameter].quantile(0.75)
        IQR=Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        # Filter the DataFrame
        data=data[(data[parameter]>=lower_bound)&(data[parameter]<=upper_bound)]
    return data 

# Remove outliers
df = remove_outliers(data,parameters)

#Print the shape of the original and cleaned data 
print(f"Original data shape : {data.shape}")
print(f"Cleaned data shape :{df.shape}")


# In[37]:


df


# In[38]:


df.hist(figsize=(12,14))
plt.show()


# So here i concluded that all plots are normally distributed i.e it is unbiased. this means that mean ,median and mode are approximately same and Also concluded that in ph maximum values lies between the range 6 to 8 i.e values near the mean occur more frequently then the values far from mean , same as it is concluded for the remaining parameters.and in Potability, it can be concluded that non drinkable water is more than the drinkable water.

# # Bar Plot for Portability

# In[39]:


plt.figure(figsize=(5,4))
sns.countplot(x='Potability', data=df, palette='pastel')
plt.title('Count of Potable vs Non-Potable Water')
plt.xlabel('Potability (1=Safe, 0=Unsafe)')
plt.ylabel('Count')
plt.show()


# In[40]:


df.Potability.value_counts()


# In[41]:


per1=(1664/2657)*100
per1


# In[42]:


per2=(993/2657)*100
per2


# So here i analyse that the in my dataset 62.62% water is not drinkable or we can say not good for health and around 37% water is for human consumption

# # Correlation Matrix

# In[43]:


corr=df.corr()
corr


# # Correlation heatmap

# In[44]:


sns.heatmap(corr,annot=True,cmap="Blues",linewidths=0.1)
fig=plt.gcf()
plt.title("Correlation Matrix")
fig.set_size_inches(8,6)
plt.show()


# From the heatmap it is concluded that when a variable is compared to itself i.e Self-Correlation then the correlation is perfect. Therefore the correlation is always 1.
# 
# Negatives values shows the negative correlation that is with increase in one variable then the other variable decreases or we can say with decrease in another variable then the other tends to increases.
# 
# Positive values the positive Correlation between the variables i.e with the increase in one variable other also increases or vice versa.

# In[ ]:




