from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0, stop_words = 'english')

desc=defaultdict(list)

with open('csv/github_issues_preproct1.csv',  'r') as sentences_file:
	reader=csv.reader(sentences_file , delimiter=",")
	reader.next()
	for row in reader:
		desc[row[1]].append(row[2])

for desc_id , text in desc.iteritems():
	desc[desc_id]="".join(text)

corpus=[]

for id , desc in sorted(desc.iteritems()):
	corpus.append(desc)
 

tfidf_matrix=tf.fit_transform(corpus)
feature_names=tf.get_feature_names()

print feature_names