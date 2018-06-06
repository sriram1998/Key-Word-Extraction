import re, string, unicodedata
import nltk
import contractions
import inflect
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
data=pd.read_csv('csv/github_issues_sampledv3.csv',usecols = ['issue_title','body'] , encoding='utf8')
df = pd.DataFrame(data,columns=['issue_title','body'])
rem=0

def replace_cont(text):
 return contractions.fix(text)


def check_common(t,b):
 result = False
 for x in t:
  for y in b:
   if x == y:
    result = True
    return result 
 return result

def check_atl2(t , b):
	print list(set(t).intersection(b))


for i , row in df.iterrows():
 title=data['issue_title'][i]
 body=data['body'][i]
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
 
 if check_common(title_fil , body_fil) == False:
  rem=rem+1
 check_atl2(title_fil , body_fil)  
  		




print "total:"
print rem