#!/usr/bin/env python
# coding: utf-8

# This project Conducts data analysis of FDIC's Failed Bank List, identifying trends, and predicting bank failures.

# In[1]:


import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


#this code reads the failed banked list from the fdic website 

listOfBanks=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
listOfBanks[0].head()


# In[ ]:





# In[6]:


#this code Displays the Column names of the table
listOfBanks[0].columns


# In[4]:





# In[7]:


#this code checks whether there is any empty values in each column 

listOfBanks[0].isnull().any()


# In[8]:


#this code is used to check any duplicated rows in the listofBanks
listOfBanks[0].duplicated().sum()


# In[8]:


updatedTable=listOfBanks[0].rename({'Bank NameBank':'Bank Name','CityCity':'City','StateSt':'State','Closing DateClosing':'Closing Date'},axis=1)
updatedTable.head()


# In[10]:


#to find number of failed banks that were in Missouri 
updatedTable['State'].value_counts()['MO']


# In[7]:





# In[12]:


# Tracing the city that  has the most numbers of failed banks?
updatedTable['City'].value_counts().index.tolist()[0]


# In[13]:


# to Verify the date in the 'Closing Date' column is a String not the DateTime object
type(updatedTable['Closing Date'][1])


# In[14]:


#finding the year  that has the most failed banks?
date= []
year= []
for i in updatedTable['Closing Date']:
    x,y = i.split(', ')
    date.append(x)
    year.append(y)

    
max(year,key=year.count)


# In[15]:


#finding the month that has the most failed banks 
day=[]
month=[]
for i in date:
    x,y = i.split(' ')
    month.append(x)
    day.append(y)

max(month,key=month.count)


# In[10]:


# finding Which institution acquired the second most numbers of failed banks?
updatedTable['Acquiring InstitutionAI'].value_counts().index.tolist()[1]


# In[9]:


# Changing the date in the Closing Date column to the dateTime object and display the first five rows of the table.  
updatedTable['Closing Date']=pd.to_datetime(updatedTable['Closing Date'])
updatedTable.head()


# In[18]:


#Display the Bank information which has a cert number 33901
updatedTable[updatedTable['CertCert']==33901]


# In[11]:


#finding the banks that failed between January 1, 2008 and December 31, 2010?
import datetime
failedWindow= len(updatedTable[(updatedTable['Closing Date']<datetime.datetime(2010,12,31))&(updatedTable['Closing Date']>datetime.datetime(2008,1,1))])
failedWindow


# In[12]:


#Reorganize the table to make the State and City as the indexes of the table. Display the first 20 rows of the new table
updatedTable.set_index(['State','City'],inplace=True)
updatedTable=updatedTable.sort_index()
updatedTable.head(20)


# In[13]:


# Display failed banks based in Kansas City, MO
updatedTable.xs('Kansas City',level=1,drop_level=False)


# In[14]:


#Display failed banks in Missouri and Kansas
updatedTable[(updatedTable.index.get_level_values('State')=='MO')|
                (updatedTable.index.get_level_values('State')=='KS')].sort_index(ascending=[False,True])


# In[15]:


# Display failed banks based in the Kansas City metro area which include Kansas City, Overland Park, Leawood and Olathe
pd.concat([updatedTable[(updatedTable.index.get_level_values('City') == 'Kansas City')],
           updatedTable[(updatedTable.index.get_level_values('City') == 'Overland Park')],
           updatedTable[(updatedTable.index.get_level_values('City') == 'Leawood')],
           updatedTable[(updatedTable.index.get_level_values('City') == 'Olathe')],
              ])


# In[24]:


#How many failed banks' names include the word National?
len(updatedTable[updatedTable['Bank Name'].str.contains("National")])

