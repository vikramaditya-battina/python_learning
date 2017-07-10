
# coding: utf-8

# In[2]:

y = lambda x: x * x
y(2)


# In[3]:

mul = lambda x, y: x * y


# In[4]:

mul(2, 3)


# Most of the lambda people use it to passing as parameter to the function

# In[7]:

#this will return the generator in the python3 
map(lambda x: x*2, [1,2,3,4,5,6,7,8,9])


# In[9]:

#this will return the list
(list)(map(lambda x: x*2, [1,2,3,4,5,6,7,8,9]))


# In[13]:

import functools
def r(x, y):
    print(x)
    print(y)
    return x + y
functools.reduce(r, [1,10,100,1000])


# In[14]:

functools.reduce(lambda x,y: x+y, [1,10,100,1000])


# In[16]:

#need to type to list to get list
(list)(filter(lambda x:x%2==0, [1,2,3,4,5,6,7,8,9,10]))


# End of Lambda

# In[ ]:



