__author__ = 'luning'
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

# for t, marker, c in zip(xrange(3),'>ox','rgb'):
#     plt.scatter(features[target==t,0],
#                 features[target==t,1],marker=marker,c=c)
# plt.xlabel('sepal length(cm)')
# plt.ylabel('sepal length(cm)')
#
#
# #plt.autoscale(tight=false)
# plt.grid()
# plt.show()

plength = features[:,2]
is_setosa = (target == 0)

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print(max_setosa,min_non_setosa)

features=features[~is_setosa]
labels=target[~is_setosa]
virginica = (labels == 2)

best_acc = - 1.0
for fi in xrange(features.shape[1]):
    thresh = features[:,fi].copy()
    thresh.sort()
    for t in thresh:
        pred = (features[:,fi] > t)
        acc = (pred == virginica).mean()
        if acc > best_acc:
            best_acc=acc;
            best_fi = fi
            best_t = t