#!/usr/bin/env python
# coding: utf-8

# ### Class 
# 
# 1. A class is like a blueprint or a template for creating something.
# 2. Think of it like a recipe for making cookies. The recipe tells you what ingredients you need and how to mix them.
# 3. In a class, you define what something should have and what it can do. For example, a "Car" class might have things like "color," "make," and "model," and it can do things like "start" and "stop."

# ### Object
# 
# 1. An object is like an actual thing created using the blueprint (class). (object is an instance of the class)
# 2. Going back to the cookie example, if you follow the recipe, you'll have real cookies. Each cookie you make is an object.
# 3. In programming, you create objects based on a class. So, if you have a "Car" class, you can create different cars (objects) with different colors, makes, and models.

# ### Define a class named car with 2 attributes, “color” and “speed”. Then create an instance and return speed. 

# In[1]:


class Car():
    def __init__(self,color,speed):
        self.color = color           # define attributes
        self.speed = speed
        
# define instance (object)

car1 = Car('red','100kmh')
car2 = Car('blue','200kmh')


# In[2]:


car1.speed

