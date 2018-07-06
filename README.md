# Extracting key information from Issue description.

Dataset used : github issues from kaggle.

# Python files and what they do:
1.)Sample the datatset consisting of 10 million rows to required amount by running sampling.py

2.)Extract only those rows which has atleast 2 words common between title and description using extract.py

3.)Pre process the csv file using preproc.py

4.)TF-IDF analysis is done in analyze.py

5.)pipeline.py accepts an user given text and processes it. Run on Node server.


# Run the App
6.)Run npm install 

7.)start the server by nodemon server.js



#dependencies and versions:
npm version:6.1.0
node version: 10.5.0

#Python dependencies:
import csv
import sklearn , version : 0.19.1
from sklearn.feature_extraction.text import TfidfVectorizer
import collections
import pandas as pd
import re
import string
import sys
import unicodedata
import nltk  , version:3.3
import cPickle as pickle
import contractions
import inflect
from bs4 import BeautifulSoup



