
# coding: utf-8

# In[71]:


import newspaper
cnn_paper = newspaper.build('http://cnn.com', memoize_articles=False)


# In[72]:


data = {'articles' : []}
n = 60;


for article in cnn_paper.articles:
    if n == 0:
        break
    try:
        content = Article(article.url)
        content.download()
        content.parse()
        content.publish_date
    except Exception as e:
        print(e)
        print("continuing...")
        continue
    entry = {}
    entry['link'] = content.url
    entry['date'] = content.publish_date
    entry['title'] = content.title
    entry['author'] = content.authors
    entry['text'] = content.text
    data['articles'].append(entry)
    n = n-1
    
    


# In[73]:


#this is for testing purposes
print (data['articles'])
print(len(data['articles']))


# In[74]:


import json
with open('data.json', 'w') as f:
  json.dumps(data, indent=4, sort_keys=True, default=str)

