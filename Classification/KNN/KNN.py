from numpy import *
import operator


class knn:
    # KNN-计算，归并，排序
    '''
    inX:输入向量
    dataSet:训练数据集
    labels:标签
    k:k值    
    '''

    def classify(self, inX, dataSet, labels, k):
        dataSetSize = dataSet.shape[0]
        diffMat = tile(inX, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistIndicies = distances.argsort()
        classCount = {}
        for i in range(k):
            voteIlabel = labels[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    '''
    处理数据：离线文本数据格式化为标准数据
    返回：训练数据集和标签集
    '''

    def getFile(self, fileName):
        fr = open(filename)
        numberOfLines = len(fr.readlines())  # get the number of lines in the file
        returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
        classLabelVector = []  # prepare labels return
        fr = open(filename)
        index = 0
        for line in fr.readlines():
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index, :] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
        return returnMat, classLabelVector

    '''
    归一化特征值
    '''
