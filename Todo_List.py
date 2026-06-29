#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import os
from openpyxl import load_workbook
import easyocr
from PIL import Image
import numpy as nm
from google import genai
import pandas as pd


# In[35]:


task=st.text_input("Enter your task...")
if 'dd' not in st.session_state:
    st.session_state['dd']=[]
if st.button('Add task!'):
    if task!='':
        st.session_state['dd'].append(task)
        st.success('Task added')
    else:
        st.error('Enter task please')
for e,s in enumerate(st.session_state['dd'],start=1):
    st.write(f"{e}.{s}")


# In[ ]:





# In[34]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




