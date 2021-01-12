#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[18]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[19]:


soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[20]:


title = soup.title
print(title)


# In[22]:


# Print out the text
text = soup.get_text()
print(soup.text)


# In[23]:


soup.find_all('a')


# In[24]:


all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# In[25]:


rows = soup.find_all('tr')
print(rows[:10])


# In[26]:


for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)


# In[27]:


str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


# In[ ]:




