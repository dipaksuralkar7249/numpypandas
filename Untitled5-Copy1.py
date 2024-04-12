#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import statistics as stats
baked_food = [150,150,200,170,300,125,220,100]
a = np.array(baked_food)
print("Mean  ",np.mean(a))
print("Median  ",int(np.median(a)))
print("Sorted Array  ",np.sort(a))
print("Sum of Array  ",np.sum(a))
print("Mode ",stats.mode(a))
print("standerd deviation ",np.std(a))


# In[28]:


#first demo of pandas
#taking input from dictionary
import pandas as pd
data = {"Names":["dipak","vivek","rohit","atul"],"age":[25,26,28,29],"salary" : [30000,40000,50000,150000]}
df = pd.DataFrame(data)
print(df)


# In[37]:


#taking data from excel file
import pandas as pd
data = pd.read_csv("H:/data analysis/customer.txt")
print(data)


# In[1]:


#taking data from excel file using openpyxl module

import openpyxl as op
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data)


# In[3]:


import pandas as pd
print(pd.read_excel("H:/data analysis/data.xlsx"))


# In[10]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data.head(2))


# In[14]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data.info())


# In[2]:


data.describe()


# In[5]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data)


# In[7]:


print(data.duplicated())


# In[11]:


print(data["names"].duplicated().sum())


# In[15]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data)


# In[19]:


print(data["names"].duplicated().sum())


# In[25]:


print(data)


# In[27]:


print(data)


# In[29]:


print(data.drop_duplicates())


# In[31]:


print


# In[2]:


import pandas as np
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data.isnull().sum())
            


# In[4]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
print(data.isnull().sum())


# In[8]:


print(data)


# In[9]:


print(data.dropna())


# In[11]:


print(data)


# In[1]:


import numpy as np
print(data.replace(np.nan,"hello"))


# In[12]:


import pandas as pd
data = pd.read_excel("H:/data analysis/data.xlsx")
data["Full_name"] = data["First_name"].str.title() + " "+ data["Last_name"].str.capitalize()
print(data)


# In[16]:


data["Bonas"] = (data["salary"] / 100) * 20
print(data)
print(data.replace("nan","NO"))


# In[ ]:




