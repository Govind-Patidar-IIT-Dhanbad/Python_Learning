#!/usr/bin/env python
# coding: utf-8

# ### Copy a function

# In[5]:


def square(x):
    return x**2


# In[6]:


square(5)


# In[8]:


#function copy
s = square


# In[9]:


s(5)


# In[10]:


del square


# In[11]:


square(5)


# In[12]:


s(5)


# ### Closures 
# 
# A closure is like a function that carries a little piece of information from where it was made and uses that information later when you call it.

# In[13]:


def make_sandwich(ingredient):
    def sandwich():
        print("Making a sandwich with", ingredient)
    
    return sandwich


# In[14]:


#closures

cheese_sandwich = make_sandwich("cheese") # closures1
ham_sandwich = make_sandwich("ham") #closures2

cheese_sandwich()  # This makes a sandwich with cheese.
ham_sandwich()    # This makes a sandwich with ham.


# ### Decorator
# 
# A decorator in Python is a special type of function that allows you to modify or extend the behavior of other functions or methods without changing their code. 
# 
# 1. Function Wrapping: Decorators are functions that wrap around other functions. They take a function as input and return a new function that typically extends or modifies the behavior of the original function.
# 
# 2. @ Syntax: You can apply a decorator to a function using the "@" symbol followed by the decorator's name, placed above the function definition.
# 
# 3. Clean and Reusable: Decorators allow you to separate concerns in your code. You can define a decorator once and apply it to multiple functions, promoting code reusability and maintainability.

# In[16]:


# Decorator function
def my_decorator(func):
    def wrapper():
        print("this is demo")
        func()
        print("i think you got it")
    return wrapper

# Applying the decorator using "@" syntax
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


# In[43]:


def devide(a,b):
    return a/b


# In[44]:


devide(3,6)


# In[46]:


# But i wanted it to a>=b always and i have to do it without changing my original function

# we have to use decorator

def num_swipe(func):
    def swipe(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
    return swipe


# In[47]:


@num_swipe
def devide(a,b):
    print(a/b)


# In[48]:


devide(3,6)


# In[ ]:




