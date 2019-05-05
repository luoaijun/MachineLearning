from numpy import *

from Classification.KNN import KNN

'''
加载数据
'''


def create_dataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['好', '好', '不好', '不好']
    return group, labels


if __name__ == '__main__':
    knn = KNN.knn()
    dataSet, labels = create_dataset()
    inX = [1, 3]
    k = 4
    cc = knn.classify(inX, dataSet, labels, k)
    print(cc)