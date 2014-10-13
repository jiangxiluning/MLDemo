__author__ = 'ninglu'
import os,sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
# content = ["How to format my hard disk", " Hard disk format problems "]
# X = vectorizer.fit_transform(content)
# vectorizer.get_feature_names()

posts = [open(os.path.join('data/ch03/toy',f)).read() for f in os.listdir('data/ch03/toy')]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape

print('#samples:%d #feature:%d' % (num_samples,num_features))
print vectorizer.get_feature_names()
new_post = "imaging database"
new_post_vec = vectorizer.transform([new_post])

def dist_raw(v1,v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized -v2_normalized
    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec,new_post_vec)
    print '=== Post %i with dist=%.2f : %s' % (i,d,post)
    if d<best_dist:
        best_dist = d;
        best_i = i
        best_doc=post
print("Best Post is %s" % best_doc)