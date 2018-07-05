from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import re
import cPickle as pickle

desc=defaultdict(list)
corpus=[]
text="hi! thanks for putting this up for us all to use! i've got ardufocus on a arduino nano. from the standalone moonlight focusing software everything works. i can also control it as expected from putty to my com port. however, sgp won't connect to the device. when i click connect on the moonlight dro driver, the configuration window pops up, but show's no controllers. when i sniff on the serial port, i see that the ardufocus is sent :gh :2gh and then doesn't respond. i get :gh being sent, but i don't understand :2gh . when i do :gh manually from putty ardufocus responds correctly. any thoughts?"


desc[0].append(text)
desc[0]="".join(text)



for id,text in desc.iteritems():
 print desc[id]
 corpus.append(desc[id])
 print corpus


vectorizer = pickle.load(open("feature5.pkl"))
tfidf_matrix=vectorizer.transform(corpus)
feature_names=vectorizer.get_feature_names()
dense=tfidf_matrix.todense()
 
text1=dense[0].tolist()[0]

phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]


a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:10]
print len(a)
for i in range(0,len(a)):

  print feature_names[a[i][0]]

 





