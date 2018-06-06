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
data=pd.read_csv('csv/github_issues_preproc1.csv',encoding='utf8')
df = pd.DataFrame(data,columns=['issue_url','issue_title','body'])
print data.shape



vectorizer.fit(data['body'])
vector = vectorizer.transform(data['body'])

print "count vectoriZer"
print vector.shape
print vectorizer.vocabulary_

vectorizer2.fit(data['body'])

print "TfiDf"
print(vectorizer2.vocabulary_)
print(vectorizer2.idf_)

vector2 = vectorizer2.transform(data['body'])

print(vector2.shape)
print(vector2.toarray())