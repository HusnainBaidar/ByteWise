#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[8]:


df = pd.read_csv('Cleaned_DS_Jobs.csv')


# In[9]:


df


# In[10]:


df.columns


# In[13]:


def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'


# In[14]:


df['job_simp'] = df['Job Title'].apply(title_simplifier)
df.job_simp.value_counts()


# In[15]:


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'


# In[16]:


df['seniority'] = df['Job Title'].apply(seniority)
df.seniority.value_counts()


# In[17]:


df['job_state']= df.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'los angeles' else 'CA')
df.job_state.value_counts()


# In[18]:


df['desc_len'] = df['Job Description'].apply(lambda x: len(x))
df['desc_len']


# In[23]:


df['Industry'] = df.Industry.apply(lambda x: x.replace('\n', ''))
df['Industry']


# In[24]:


df.describe()


# In[25]:


df.columns


# In[26]:


df.Rating.hist()


# In[27]:


df.avg_salary.hist()


# In[29]:


df.company_age.hist()


# In[30]:


df.desc_len.hist()


# In[31]:


df.boxplot(column = ['company_age','avg_salary','Rating'])


# In[32]:


df.boxplot(column = 'Rating')


# In[33]:


df[['company_age','avg_salary','Rating','desc_len']].corr()


# In[37]:


cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(df[['company_age','avg_salary','Rating','desc_len']].corr(),vmax=.3, center=0, cmap=cmap,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# In[38]:


df.columns


# In[46]:


df_cat = df[['Job Title', 'Salary Estimate', 'Job Description', 'Rating',
       'Company Name', 'Location']]


# In[47]:


for i in df_cat.columns:
    cat_num = df_cat[i].value_counts()
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# In[51]:


df_cat = df[['Job Title', 'Salary Estimate', 'Job Description', 'Rating',
       'Company Name', 'Location', 'Headquarters', 'Size', 'Type of ownership',
       'Industry']]


# In[52]:


for i in df_cat[['Location','Headquarters','Industry']].columns:
    cat_num = df_cat[i].value_counts()[:20]
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# In[53]:


pd.pivot_table(df, index = 'job_simp', values = 'avg_salary')


# In[54]:


pd.pivot_table(df, index = ['job_simp','seniority'], values = 'avg_salary')


# In[55]:


pd.pivot_table(df, index = ['job_state','job_simp'], values = 'avg_salary').sort_values('job_state', ascending = False)


# In[56]:


pd.set_option('display.max_rows', None)
pd.pivot_table(df, index = ['job_state','job_simp'], values = 'avg_salary', aggfunc = 'count').sort_values('job_state', ascending = False)


# In[57]:


pd.pivot_table(df[df.job_simp == 'data scientist'], index = 'job_state', values = 'avg_salary').sort_values('avg_salary', ascending = False)


# In[64]:


df_pivots = df[['Rating', 'Industry', 'Sector', 'Revenue', 'python', 'spark', 'aws', 'excel', 'Type of ownership','avg_salary']]
for i in df_pivots.columns:
    print(i)
    print(pd.pivot_table(df_pivots,index =i, values = 'avg_salary').sort_values('avg_salary', ascending = False))


# In[67]:


from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[69]:


words = " ".join(df['Job Description'])

def punctuation_stop(text):
    """remove punctuation and stop words"""
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered


words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc= WordCloud(background_color="white", random_state=1,stopwords=STOPWORDS, max_words = 2000, width =2000
              , height = 1500)
wc.generate(text)

plt.figure(figsize=[10,10])
plt.imshow(wc,interpolation="bilinear")
plt.axis('off')
plt.show()


# In[ ]:




