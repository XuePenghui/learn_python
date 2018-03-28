# coding=utf-8
# minist classification with pca and KNN
from sklearn.datasets import fetch_mldata
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn import neighbors
def getdata(label):
    return X[np.where(y==label)]

def getlabel(label):
    return y[np.where(y==label)]

mnist =  fetch_mldata('MNIST original')
X = np.array(mnist.data)
y = np.array(mnist.target)

x_1 = getdata(1)
x_2 = getdata(2)

y_1 = getlabel(1)
y_2 = getlabel(2)

X = np.concatenate((x_1,x_2),axis=0)
y = np.concatenate((y_1,y_2))


# pca降维
pca=PCA(n_components=1)
newX = pca.fit_transform(X)

# KNN
KNN = neighbors.KNeighborsClassifier(n_neighbors=1)

# KNN 分类结果
y_ = cross_val_predict(KNN,X,y)
print(classification_report(y,y_))
