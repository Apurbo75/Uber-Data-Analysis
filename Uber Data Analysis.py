#!/usr/bin/env python
# coding: utf-8
%pylab inline
import pandas as pd
import matplotlib as mb

# In[ ]:


Raw = pd.read_csv('Desktop/uber-raw-data-apr14.csv')
Raw


# In[ ]:


dt ='4/1/2014 0:11:00'
dt = pd.to_datetime(dt)
dt


# In[ ]:


dt.day


# In[ ]:


dt.weekday_name


# In[ ]:


dt.month


# In[ ]:


Raw['Date/Time']= Raw['Date/Time'].map(pd.to_datetime)


# In[ ]:


def get_dom(dt):
    return dt.day

Raw['dom']=Raw['Date/Time'].map(get_dom)

def get_weekday(dt):
    return dt.weekday()

Raw['weekday']= Raw['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

Raw['hour']= Raw['Date/Time'].map(get_hour)
Raw.tail()


# In[ ]:


hist(Raw.dom, bins= 30, rwidth=0.8, range= (0,31))
xlabel('DATE OF THE MONTH')
ylabel("FREQUENCY")
title('Frequency- Day- plot')


# In[ ]:


for k, rows in Raw.groupby('dom'):
    #print((k, len(rows)))
    print((k,rows))


# In[ ]:


def count_rows(rows):
    return len(rows)
by_date= Raw.groupby('dom').apply(count_rows)
by_date


# In[ ]:


plot(by_date)


# In[ ]:


bar(range(1,31), by_date)


# In[ ]:


hist(Raw.weekday, bins=20, rwidth = 1, color = 'yellow')
xticks(range(7), 'Mon, Tue, Wed, Thu, Fri, Sat, Sun'.split())


# In[ ]:


A =(Raw.groupby('weekday hour'.split()).apply(count_rows).unstack())
mb.heatmap(A)


# In[ ]:


figure(figsize(20,20))
plot(Raw['Lon'], Raw['Lat'], '.', ms=1, alpha = 0.5)
xlim(-74.5,-73)
ylim(40.25,41.25)


# In[ ]:




