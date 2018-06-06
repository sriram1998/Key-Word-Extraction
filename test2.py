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
def replace_cont(text):
 return contractions.fix(text)

w=replace_cont("cia won't save")
print w