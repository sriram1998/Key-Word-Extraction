#required imports
import collections
import pandas as pd
import re
import string
import unicodedata
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer



#reading the csv file and creating dataframe.
data=pd.read_csv('csv/preprocv2f.csv',usecols = ['issue_title','body'] , encoding='utf8')
df = pd.DataFrame(data,columns=['issue_title','body'])


#Noise removal functions
def strip_html(text):
 soup=	BeautifulSoup(text , "html.parser")
 return soup.get_text() 
def sub_num(text):
 sub=re.sub(r"\b\d+\b" , "< NUMBER >" , text)
 return sub
def sub_path(text):
 sub=re.sub(r"(?:/[^/-]+)+?/\w+\.\w+" , "< PATH >" , text)
 return sub
def sub_url(text):
 sub=re.sub(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?" , "< URL >" , text)
 return sub
def sub_alphanum(text):
 sub=re.sub(r"\w{1,}\d\w+" , "< ALPHANUM >" , text)
 return sub
def rem_punc(text):
 sub=re.sub(r'[^\w\s]','',text)
 return sub

 
 
#Passing each description to the functions
for i , row in df.iterrows():
 s=data['body'][i]
 s=strip_html(s)
 s=sub_num(s)
 s=sub_path(s)
 s=sub_url(s)
 s=sub_alphanum(s)
 s=rem_punc(s)
 st=data['issue_title'][i]
 st=strip_html(st)
 st=sub_num(st)
 st=sub_path(st)
 st=sub_url(st)
 st=sub_alphanum(st)
 st=rem_punc(st)
 
 df=df.replace(data['body'][i] , s)
 df=df.replace(data['issue_title'][i] , st)
 

#writing to new csv file
df.to_csv('csv/preprocv2fnew.csv' , encoding='utf-8' , index=False)




