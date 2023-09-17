#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib practice

# In[1]:


import matplotlib.pyplot as plt


# ### 1. Pie chart 

# In[9]:


item = [1,2,3,4,5]
price = [10,20,30,50,60]

plt.pie(price, labels = item, autopct = '%0.1f%%' )
plt.show()


# ### 2. Scatter plot 

# In[13]:


item = [1,2,3,4,5,6,7,8,9]
price = [10,20,30,50,60,70,80,90,100]

plt.scatter(item,price)
plt.xlabel("Item id")
plt.ylabel("Price")
plt.title("Item price plot")
plt.show()


# ### 3. 2-D Plot 

# In[22]:


item = [1,2,3,4,5,6,7,8,9]
Online_price = [10,20,30,50,60,70,80,90,100]
Offline_price = [20,40,10,30,60,70,70,80,90]


plt.plot(item,Online_price, color = "red", marker = "+", label = "Online_price" )
plt.plot(item,Offline_price, color = "green", marker = "D", label = "Offline_price")
plt.xlabel('Item ID')
plt.ylabel('Price')
plt.title("Price Comparision")
plt.legend()
plt.show()


# ### 4. Bar Graph 

# In[26]:


item = [1,2,3,4,5,6,7,8,9]
Online_price = [10,20,30,50,60,70,80,90,100]
Offline_price = [20,40,10,30,60,70,70,80,90]

plt.bar(item,Online_price, color = "red")

plt.show()


# In[ ]:





# In[ ]:




