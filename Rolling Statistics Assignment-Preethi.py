#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Rolling Statistics Assignment- Preethi and Alvin

#We are importing all the packages 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#Here, we read the data file 'GOOG.csv'. 

#Note: Please paste the path location of GOOG.csv based on where you have saved it. Here, the csv file is saved in my 'Users' file
data=pd.read_csv('C:/Users/Preethi Abraham/Desktop/Brandeis Studies/Python for business analytics/GOOG.csv')


# In[4]:


#Viewing the data
data


# In[5]:


#We want the user to enter an integer from 2 to 254. If the user inputs a number beyong that range, it will display an error. 
#The loop will also display an error if the user enters anything apart from numbers from 2 to 254

while True:
  try:
    n=int(input('Enter a number from 2 to 254: '))
    # Check if input is in range
    if n in range(2,255):
      break
    else:
      print ('Your number is out of the range of 2 to 254')
  except:
    print ("You have not entered a number. Please try again")


# In[7]:


#Here, we are trying to plot all the observations from the 'Adj Close' column
data['Adj Close'].plot()


# In[9]:


#We find the mean values of the adjusted close price based on the user's input

print('Mean of stock prices for rolling window of ', n, 'is $')
for i in range(0,len(data)):
    mean=stats.mean(data['Adj Close'][i:i+n])
    print(mean)
    


# In[10]:


#We find the range of the adjusted close price based on the user's input

print('Range of stock prices for rolling window of', n, 'is $ ')
for i in range(0, len(data)):
    max_stock_price=max(data['Adj Close'][i:i+n])
    min_stock_price=min(data['Adj Close'][i:i+n])
    range_of_stock=round((max_stock_price-min_stock_price),2)
    print(range_of_stock)


# In[11]:


#We find the median values of the adjusted close price based on the user's input

print('Median values of stock prices for rolling window of', n, ' is $ ')
for i in range(0, len(data)):
    median=stats.median(data['Adj Close'][i:i+n]) 
    print(median)


# In[12]:


#We find the standard deviation values of the adjusted close price based on the user's input


print('Standard Deviation values of stock prices for rolling window of', n, ' is $ ')
for i in range(0, len(data)):
    std_dev=np.std(data['Adj Close'][i:i+n])
    print(std_dev)


# In[8]:


#If we want to see everything in a single table:

print("For the rolling window of: ", n)
print("Std Dev", "  Range  ", " Mean ", "   Median" )
for i in range(0, len(data)):
    std_dev=round(np.std(data['Adj Close'][i:i+n]),2)
    max_stock_price=max(data['Adj Close'][i:i+n])
    min_stock_price=min(data['Adj Close'][i:i+n])
    range_of_stock=round((max_stock_price-min_stock_price),2)
    mean=round(stats.mean(data['Adj Close'][i:i+n]),2)
    median=round(stats.median(data['Adj Close'][i:i+n]) ,2)
    print(std_dev,"  ",range_of_stock, "  ", mean, "  ", median)

    

