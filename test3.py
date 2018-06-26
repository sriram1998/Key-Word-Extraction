from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
tf1 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0, stop_words = 'english')


  
print "test"
sys.stdout.flush()