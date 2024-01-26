#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data ={
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[23,35,45,36,28],
    'City':['New york','Los Angeles','Chicgao','Houston','Phoenix']
    
}
df= pd.DataFrame(data)
print(df)


# In[5]:


(df.iloc[2])


# In[8]:


(df.iloc[:,1])


# In[12]:


df.iloc[0:3]


# In[19]:


df.iloc[:,[0,2]]


# In[27]:


data= df.loc[df['Name']=='Charlie']
print(data)


# In[28]:


df.loc[:,['Age']]


# In[32]:


df.loc[df['Name'].isin(['Bob', 'Eva']), 'City']


# # Exersise 2

# In[35]:


df.loc[df['Age']>30]


# In[64]:


df[(df['City'] == 'Chicgao') | (df['City'] == 'Houston')]


# In[78]:


data ={
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[23,35,45,36,28],
    'City':['New york','Los Angeles','Chicgao','Houston','Phoenix']
    
}
dfa= pd.DataFrame(data)
print(dfa)
dfa.set_index('Name',inplace=False)


# In[97]:


print(dfa.loc['David'])


# In[99]:


dfa.loc[['Bob', 'Eva'], ['Age', 'City']]


# # Exercise 3

# In[110]:


datab={
    'Product': ['Apple','Banana','Carrot','Doughnut','Egg'],
    'Price':[0.5,0.3,0.4,1.0,0.2],
    'In Stock':[True,True,False,True,False]
}
dfb=pd.DataFrame(datab)
print(dfb)


# In[118]:


dfb.loc[dfb['In Stock'],'Product']


# In[124]:


dfb.loc[dfb['Product']== 'Doughnut','Price']=1.2
print(dfb)


# In[125]:


dfb.loc[dfb['Price']>0.5,'Product']


# In[128]:


dfb.loc[dfb['In Stock']==False,['Product','Price']]


# In[ ]:




