

# In[39]:


import json
import objectpath


# In[44]:


with open('/Users/vishwaswarupredd/Downloads/\py_challange_input.json') as json_file:
    data = json.load(json_file)


# In[53]:


formats = data['Cricket'][0]


# In[60]:


formatsT = formats['formats'][0]


# In[61]:


formatsO = formats['formats'][1]


# In[73]:


regions = formatsT['regions'][0]
regions
matches = regions['matches']
matches


# In[85]:


for i in matches:
    print('match_id: ', i['id'])
    print('livestream_provider: ', i['streaming'])
    print('winner of the match: ', i['results'])
    print('httplink of match: ', i['httpLink'])
    print('region name', regions['name'])
    print('team 1 and team 2 playing in the match: ', i['team1'])
    print('team 2 playing in the match: ', i['team2'])


# In[ ]:




