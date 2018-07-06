from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import collections
import pandas as pd
import re
import string
import sys
import unicodedata
import nltk
import cPickle as pickle
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

script = sys.argv[0]


command = sys.argv[1]

desc=defaultdict(list)

text=command
def preprocess(text):
  soup=  BeautifulSoup(text , "html.parser")
  text=soup.get_text()
  #text=re.sub(r"\b\d+\b" , "< NUMBER >" , text)
  text=re.sub(r"(?:/[^/-]+)+?/\w+\.\w+" , " PATH " , text)
  text=re.sub(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?" , "< URL >" , text)
  text=re.sub(r"\w{1,}\d\w+" , " ALPHANUM " , text)
  text=re.sub(r'[^\w\s]','',text)           
  return text
corpus=[]


def analysis(row ,  n , s , num):
 if n==1 and s==1:
  vectorizer = pickle.load(open("feature1.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()
 if n==1 and s==0:
  vectorizer = pickle.load(open("feature2.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()  
 if n==2 and s==1:
  vectorizer = pickle.load(open("feature3.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()
 if n==2 and s==0:
  vectorizer = pickle.load(open("feature4.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()
 if n==3 and s==1:
  vectorizer = pickle.load(open("feature5.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()
 if n==3 and s==0:
  vectorizer = pickle.load(open("feature6.pkl"))
  tfidf_matrix=vectorizer.fit_transform(corpus)
  feature_names=vectorizer.get_feature_names()
 dense=tfidf_matrix.todense()
 
 text1=dense[row].tolist()[0]
 phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]
 a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:num]	
 for i in range(0,5):
  tokenized = sent_tokenize(feature_names[a[i][0]])
  for j in tokenized:
     

    k=0
    wordsList = nltk.word_tokenize(j)
 
    
 
 
    tagged = nltk.pos_tag(wordsList)
    # for l in wordsList:
    #  k=k+1
    #  if k<3:
    #   print wordsList[k] 
    #  else:
    #   break    
    print(tagged)
    
  



text=preprocess(text)
desc[0].append(text)
desc[0]="".join(text)



for id,text in desc.iteritems():
 corpus.append(desc[id])

analysis(0 ,3,1 , 20)
sys.stdout.flush()