import collections
import pandas as pd
import numpy as np
import nltk

dfi = pd.DataFrame(columns=['issue_title','body'])
i=0
#this iterates through chinks of 10000.
for df in pd.read_csv('csv/github_issues.csv' , usecols = ['issue_title','body'] , iterator=True , chunksize=60000):
 #set the value of i to select chunk.
 if i>4:
  dfi=pd.concat([dfi,df] , sort=False)
 i=i+1
 if i>5:
  break;
 
 
print dfi.shape
dfi.to_csv('csv/github_issues_sampledtest2.csv' , encoding='utf-8' , index=False)


