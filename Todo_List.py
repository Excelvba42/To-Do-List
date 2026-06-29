#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


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




