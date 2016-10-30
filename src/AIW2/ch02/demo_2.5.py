"""
book provide a simple example, but scikit-learn has more detailed sample

http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html#sphx-glr-auto-examples-cluster-plot-cluster-iris-py

"""

from sklearn.cluster import KMeans
from sklearn import datasets
from itertools import cycle, combinations
import matplotlib.pyplot as pl

iris = datasets.load_iris()
km = KMeans(n_clusters=3)
"""
iris.data - 是一个feature的二维数组:
    array([[ 5.1,  3.5,  1.4,  0.2],
       [ 4.9,  3. ,  1.4,  0.2],
       [ 4.7,  3.2,  1.3,  0.2],

iris.feature_names - 是feature各个的内容
    ['sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)']
iris.target_names - 各个数据的label:
    array(['setosa', 'versicolor', 'virginica'],
        dtype='<U10')
iris.target - 这个数据对应的label的encode, 0，1，2， 顺序和iris.target_names是一致的, sth like:
    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    
"""
km.fit(iris.data) # Compute k-means clustering.

"""
sth like:
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2,
       0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0], dtype=int32)
"""
predictions = km.predict(iris.data) # cal data which cluster they blong to 

colors = cycle('rgb') # create a infinite iterable r-g-b-r-g-b ...
markers = cycle('^+o')
labels = ["Cluster 1","Cluster 2","Cluster 3"]
targets = range(len(labels))

feature_index=range(len(iris.feature_names))
feature_names=iris.feature_names
combs=combinations(feature_index,2) # 计算数学中的combinations, c4-2 = 4!/2!*2! = 6

f,axarr=pl.subplots(3,2) # create a plot with subplot 3row, 2cols
axarr_flat=axarr.flat

for comb, axflat in zip(combs,axarr_flat):# plot 6 figures
        # in each figure do 3 repeat, draw different cluster with different color
        for target, color, label, marker in zip(targets,colors,labels,markers):
                feature_index_x=comb[0]
                feature_index_y=comb[1]
                axflat.scatter(iris.data[predictions==target,feature_index_x],
                                iris.data[predictions==target,feature_index_y],c=color,label=label,marker=marker)
                axflat.set_xlabel(feature_names[feature_index_x])
                axflat.set_ylabel(feature_names[feature_index_y])

f.tight_layout() # combat plot
pl.show() # display plot