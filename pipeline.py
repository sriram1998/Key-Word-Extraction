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
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

script = sys.argv[0]


command = sys.argv[1]
tf1 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0, stop_words = 'english')
tf2 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0)
tf3 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0, stop_words = 'english')
tf4 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0)
tf5 = TfidfVectorizer(analyzer='word', ngram_range=(3,3), min_df = 0, stop_words = 'english')
tf6 = TfidfVectorizer(analyzer='word', ngram_range=(3,3), min_df = 0)
desc=defaultdict(list)

text=command
def preprocess(text):
  soup=  BeautifulSoup(text , "html.parser")
  text=soup.get_text()
  text=re.sub(r"\b\d+\b" , "< NUMBER >" , text)
  text=re.sub(r"(?:/[^/-]+)+?/\w+\.\w+" , "< PATH >" , text)
  text=re.sub(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?" , "< URL >" , text)
  text=re.sub(r"\w{1,}\d\w+" , "< ALPHANUM >" , text)
  text=re.sub(r'[^\w\s]','',text)
  return text
corpus=[]


def analysis(row ,  n , s , num):
 if n==1 and s==1:
  tfidf_matrix=tf1.fit_transform(corpus)
  feature_names=tf1.get_feature_names()
 if n==1 and s==0:
  tfidf_matrix=tf2.fit_transform(corpus)
  feature_names=tf2.get_feature_names()	
 if n==2 and s==1:
  tfidf_matrix=tf3.fit_transform(corpus)
  feature_names=tf3.get_feature_names()
 if n==2 and s==0:
  tfidf_matrix=tf4.fit_transform(corpus)
  feature_names=tf4.get_feature_names()
 if n==3 and s==1:
  tfidf_matrix=tf5.fit_transform(corpus)
  feature_names=tf5.get_feature_names()
 if n==3 and s==0:
  tfidf_matrix=tf6.fit_transform(corpus)
  feature_names=tf6.get_feature_names()
 dense=tfidf_matrix.todense()
 
 text1=dense[row].tolist()[0]
 phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]
 a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:num]	
 for i in range(0,num):
  tokenized = sent_tokenize(feature_names[a[i][0]])
  for i in tokenized:
     
    # Word tokenizers is used to find the words 
    # and punctuation in a string
    wordsList = nltk.word_tokenize(i)
 
    
 
    #  Using a Tagger. Which is part-of-speech 
    # tagger or POS-tagger. 
    tagged = nltk.pos_tag(wordsList)
 
    print(tagged)
  



text=preprocess(text)
desc[0].append(text)
desc[0]="".join(text)



for id,text in desc.iteritems():
 corpus.append(desc[id])

analysis(0 ,3,1 , 20)
sys.stdout.flush()