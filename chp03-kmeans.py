__author__ = 'luning'
import sklearn.datasets
MLCOMP_DIR = r"data/ch03"
data = sklearn.datasets.load_mlcomp("20news-18828",mlcomp_root=MLCOMP_DIR)
print(data.filenames)
print(len(data.filenames))
print data.target_names

groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys. \
ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'sci. \
space']

train_data = sklearn.datasets.load_mlcomp("20news-18828","train",mlcomp_root=MLCOMP_DIR, categories=groups)
print(len(train_data.filenames))

#test_data = sklearn.datasets.load_mlcomp("20news-18828","test",mlcomp_root=MLCOMP_DIR)
#print(len(test_data.filenames))

import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer,self).build_analyzer()
        return lambda doc : (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=10,max_df=0.5,stop_words='english',decode_error ='ignore')
vectorized = vectorizer.fit_transform(train_data.data)
num_samples, num_features = vectorized.shape

print("#samples: %d, #features: %d" % (num_samples, num_features))

num_clusters = 50
from sklearn.cluster import KMeans
km = KMeans(n_clusters=num_clusters,init='random',n_init=1,verbose=1)
km.fit(vectorized)

print(km.labels_.shape)

new_post = "Disk drive problems. Hi, I have a problem with my hard disk.\
After 1 year it is working only sporadically now.\
I tried to format it, but now it doesn't boot any more.\
Any ideas? Thanks."

new_post_vec = vectorizer.transform([new_post])
new_post_lable = km.predict(new_post_vec)[0]

print km.labels_