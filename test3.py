from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
tf1 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0, stop_words = 'english')
tf2 = TfidfVectorizer(analyzer='word', ngram_range=(0,1), min_df = 0)
tf3 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0, stop_words = 'english')
tf4 = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0)

desc=defaultdict(list)

with open('csv/preproct1f.csv',  'r') as sentences_file:
	reader=csv.reader(sentences_file , delimiter=",")
	reader.next()
	for row in reader:
		desc[row[1]].append(row[2])

for desc_id , text in desc.iteritems():
	desc[desc_id]="".join(text)

corpus=[]

for id , desc in sorted(desc.iteritems()):
	corpus.append(desc)
 

tfidf_matrix=tf4.fit_transform(corpus)
feature_names=tf4.get_feature_names()

dense=tfidf_matrix.todense()

#print sorted(dense[0].tolist(), key=lambda t: t[1] * -1)[:5]
text1=dense[51].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]
print len(phrase_scores)
a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]	
print feature_names[a[0][0]]
print feature_names[a[1][0]]