import re, string, unicodedata
import nltk
import contractions
import inflect
import csv
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import enchant
import collections
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


from tqdm import tqdm
stopwords=set(stopwords.words('english'))
data=pd.read_csv('csv/github_issues_preproc1.csv',usecols = ['issue_title','body'] , encoding='utf8')
df = pd.DataFrame(data,columns=['issue_title','body'])
rem=0

#replace contractions like can't to cannot.
def replace_cont(text):
 return contractions.fix(text)

k=0

#checks for filtered rows.
def check_atl2(t , b):
 check=0
 if len(list(set(t).intersection(b)))>1:
  check=1
  return check 
 return check
 
def filter_rows(s):
 #print s	
 r=0
 data=[]
 with open('csv/github_issues_preproc1.csv', 'rb') as f,open('csv/preproc1f.csv', 'wb') as f_out:
  reader = csv.reader(f)
  writer = csv.writer(f_out)
  for row in reader:
    r=r+1
    if r==s:
     #print row
     data.append(row)	
     print data[0]
     for new_row in data:
      #print new_row[1]	
      writer.writerow(new_row)
      #print new_row
     #print "1 row written" 
 
for i , row in df.iterrows():
 title=data['issue_title'][i]
 body=data['body'][i]
 if type(body)==float:
  continue
 title_tokens=word_tokenize(title)
 body_tokens=word_tokenize(body)
 title_fil=[w for w in title_tokens if not w in stopwords]
 body_fil=[w for w in title_tokens if not w in stopwords] 
 title_fil=[]
 body_fil=[]
 for w in title_tokens:
 	if w not in stopwords:
 		w=unicodedata.normalize('NFKD' , w).encode('ascii' , 'ignore')
 		w=replace_cont(w)
 		title_fil.append(w)

 for w in body_tokens:
 	if w not in stopwords:
 		w=unicodedata.normalize('NFKD' , w).encode('ascii' , 'ignore')
 		w=replace_cont(w)
 		body_fil.append(w)
 
 
 if check_atl2(title_fil , body_fil)==1:
  k=k+1
  filter_rows(i+2) 

print "total:"
print k
#print rem
print df.shape