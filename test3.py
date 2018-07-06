from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import re
import cPickle as pickle

desc=defaultdict(list)
corpus=[]
#text="i have interest from cern about sayma board. they want to use it as general purpose amc carrier with plenty of q sfp channels. so the idea is to build rtm with sfp cages. initial plan is to use 4x sfp + 3x qsfp to utilise all 16 gigabit channels. there are easily available qsfp to sfp+ copper cables ideal for low distance connections. 4 sfp cages let us use low cost wdm transceivers for drtio longer distance connections. so the question is - would such board be attractive for artiq users? exisitin project of 8 channel rtm sfp carrier could be adopted easily."
text="hello. all newest ip-camera used rtsp video without mjpeg . how use rtsp webcam for octoprint?"

desc[0].append(text)
desc[0]="".join(text)



for id,text in desc.iteritems():
 
 corpus.append(desc[id])
 


vectorizer = pickle.load(open("feature5.pkl"))

tfidf_matrix=vectorizer.fit_transform(corpus)
print tfidf_matrix
feature_names=vectorizer.get_feature_names()
#print feature_names
dense=tfidf_matrix.todense()
print dense
text1=dense[0].tolist()[0]
#print text1

phrase_scores = [pair for pair in zip(range(0, len(text1)), text1) if pair[1] > 0]


a= sorted(phrase_scores, key=lambda t: t[1] * -1)[:200]
print len(a)
for i in range(0,len(a)):

  print feature_names[a[i][0]]

 





