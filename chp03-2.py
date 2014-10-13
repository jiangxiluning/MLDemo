__author__ = 'ninglu'
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer,self).build_analyzer()
        return lambda doc : (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=1,stop_words='english',decode_error ='ignore')

posts = [open(os.path.join('data/ch03/toy',f)).read() for f in os.listdir('data/ch03/toy')]
X_train = vectorizer.fit_transform(posts)

print X_train.toarray()
print np.max(X_train.toarray(),axis=1)