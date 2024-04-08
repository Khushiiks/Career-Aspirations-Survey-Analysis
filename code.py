#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Your Career Aspirations of GenZ.csv")
print(data.head())


# In[2]:


print(data.columns)


# In[3]:


country = data["Your Current Country."].value_counts()
label = country.index
counts = country.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Current Country')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[5]:


question1 = data["Which of the below factors influence the most about your career aspirations ?"].value_counts()
label = question1.index
counts = question1.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Factors influencing career aspirations')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[6]:


question2 = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2 = data[question2].value_counts()
label = question2.index
counts = question2.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Will you pursue a Higher Education outside India with your investment?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[7]:


question3 = "How likely is that you will work for one employer for 3 years or more ?"
question3 = data[question3].value_counts()
label = question3.index
counts = question3.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely is that you will work for one employer for 3 years or more?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[8]:


question4 = "Would you work for a company whose mission is not clearly defined and publicly posted."
question4 = data[question4].value_counts()
label = question4.index
counts = question4.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Would you work for a company whose mission is not clearly defined and publicly posted?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[9]:


question5 = "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
question5 = data[question5].value_counts()
label = question5.index
counts = question5.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is misaligned with their actions?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:


question6 = "How likely would you work for a company whose mission is not bringing social impact ?"
question6 = data[question6].value_counts()
label = question6.index
counts = question6.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is not bringing social impact?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[11]:


question7 = "What is the most preferred working environment for you."
question7 = data[question7].value_counts()
label = question7.index
counts = question7.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What is the most preferred working environment for you?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[12]:


question8 = "Which of the below Employers would you work with."
question8 = data[question8].value_counts()
label = question8.index
counts = question8.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which of the below Employers would you work with?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[13]:


question9 = "Which type of learning environment that you are most likely to work in ?"
question9 = data[question9].value_counts()
label = question9.index
counts = question9.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which type of learning environment that you are most likely to work in?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[14]:


question10 = "What type of Manager would you work without looking into your watch ?"
question10 = data[question10].value_counts()
label = question10.index
counts = question10.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What type of Manager would you work without looking into your watch?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:




