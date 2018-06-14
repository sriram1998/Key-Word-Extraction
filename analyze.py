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
vectorizer = CountVectorizer()
vectorizer2 = TfidfVectorizer()

#reading the csv file and creating dataframe.
data=pd.read_csv('csv/github_issues_preproct1.csv',usecols=['issue_title' , 'body'],encoding='utf8')
df = pd.DataFrame(data,columns=['issue_title','body'])
titlev=[]
bodyv=[]

for i , row in df.iterrows():
 title=data['issue_title'][i]
 body=data['body'][i]
 if type(body)==float:
  continue
 title_tokens=word_tokenize(title)
 body_tokens=word_tokenize(body)
 
 for w in title_tokens:
  titlev.append(w)
 for w in body_tokens:
  bodyv.append(w) 
 vectorizer.fit(titlev)
 vector = vectorizer.transform(titlev)
 vectorizer2.fit(bodyv)
 vector2=vectorizer2.transform(bodyv)

#print vectorizer2.vocabulary_
print "count vectoriZer"
print vector.shape
print vector2.shape
print "TfiDf"
print vector
print(vector2.todense())