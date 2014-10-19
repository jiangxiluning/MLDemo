__author__ = 'ninglu'
from gensim import corpora, models, similarities
import numpy as np
corpus = corpora.BleiCorpus('data/ch04/ap/ap.dat','data/ch04/ap/vocab.txt')

model = models.ldamodel.LdaModel(corpus, num_topics=100, id2word=corpus.id2word)

topics = [model[c] for c in corpus]
print(topics[0])

dense = np.zeros((len(topics), 100), float)
for ti,t in enumerate(topics):
    for tj, v in t:
        dense[ti,tj]= v


from scipy.spatial import distance
pairwise = distance.squareform(distance.pdist(dense))
pairwise.shape
largest = pairwise.max()

for ti in range(len(topics)):
    pairwise[ti,ti]=largest+1

def closet_to(doc_id):
    return pairwise[doc_id].argmin()

print(closet_to(0))