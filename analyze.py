import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
tf1 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0, stop_words = 'english')
tf2 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0)
tf3 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0, stop_words = 'english')
tf4 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0)
tf5 = TfidfVectorizer(analyzer='word', ngram_range=(3,3), min_df = 0, stop_words = 'english')
tf6 = TfidfVectorizer(analyzer='word', ngram_range=(3,3), min_df = 0)

desc=defaultdict(list)

with open('csv/filtered/preproctest2fnew.csv',  'r') as sentences_file:
	reader=csv.reader(sentences_file , delimiter=",")
	reader.next()
	for row in reader:
		desc[row[1]].append(row[1])

for desc_id , text in desc.iteritems():
 
 desc[desc_id]="".join(text)
 	
print len(desc)

y=0
corpus=[]

for id , desc in desc.iteritems():
 
 if len(desc)>30 and len(desc)<200:
  corpus.append(desc)

 
def analysis(row , ngram , sw , num):
 if ngram==1 and sw==1:
  tfidf_matrix=tf1.fit_transform(corpus)
  feature_names=tf1.get_feature_names()
 if ngram==1 and sw==0:
  tfidf_matrix=tf2.fit_transform(corpus)
  feature_names=tf2.get_feature_names()	
 if ngram==2 and sw==1:
  tfidf_matrix=tf3.fit_transform(corpus)
  feature_names=tf3.get_feature_names()
 if ngram==2 and sw==0:
  tfidf_matrix=tf4.fit_transform(corpus)
  feature_names=tf4.get_feature_names()
 if ngram==3 and sw==1:
  tfidf_matrix=tf5.fit_transform(corpus)
  feature_names=tf5.get_feature_names()
 if ngram==3 and sw==0:
  tfidf_matrix=tf6.fit_transform(corpus)
  feature_names=tf6.get_feature_names()
 
 dense=tfidf_matrix.todense()
 print dense.shape
 
 #text2=tfidf_matrix[row-1].tolist()[0]
 text1=dense[row-1].tolist()[0]

 
 phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]


 a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:num]

 
 for i in range(0,num):

  print feature_names[a[i][0]]

analysis(548, 3 , 1 , 20)