import collections
import pandas as pd
import numpy as np
import nltk

dfi = pd.DataFrame(columns=['issue_title','body'])
i=0

for df in pd.read_csv('csv/github_issues.csv' , usecols = ['issue_title','body'] , iterator=True , chunksize=10000):
 if i>10:
  dfi=pd.concat([dfi,df] , sort=False)
 i=i+1
 if i>20:
  break;
 
 
print dfi.shape
dfi.to_csv('csv/github_issues_sampledv3.csv' , encoding='utf-8' , index=False)





