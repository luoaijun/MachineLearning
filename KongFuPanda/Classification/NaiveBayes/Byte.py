from numpy import *
import math


class Bytes:

    def createVocabList(self, dataSet):
        vocabSet = set([])
        for document in dataSet:
            vocabSet = vocabSet | set(document)
        return list(vocabSet)

    def setOfWords2Vec(self, vocabList, inputSet):
        returnVec = [0] * len(vocabList)

        for word in inputSet:
            if word in vocabList:
                returnVec[vocabList.index(word)] = 1
            else:
                print("the word: %s is not in my Vocabulary!" % word)
        return returnVec

    def bagOfWords2VecMN(self, vocabList, inputSet):
        returnVec = [0] * len(vocabList)
        for word in inputSet:
            if word in vocabList:
                returnVec[vocabList.index(word)] = +1
            else:
                print("the word: %s is not in my Vocabulary!" % word)
        return returnVec

    '''
    朴素贝叶斯分类器训练器
    trainMatrix：训练集
    trainCategory：分类
    '''

    def trainNB0(self, trainMatrix, trainCategory):
        numTrainDocs = len(trainMatrix)
        numWords = len(trainMatrix[0])
        pAbusive = sum(trainCategory) / float(numTrainDocs)
        p0Num = ones(numWords);
        p1Num = ones(numWords)  # change to ones()
        p0Denom = 2.0;
        p1Denom = 2.0  # change to 2.0
        for i in range(numTrainDocs):
            if trainCategory[i] == 1:
                p1Num += trainMatrix[i]
                p1Denom += sum(trainMatrix[i])
            else:
                p0Num += trainMatrix[i]
                p0Denom += sum(trainMatrix[i])
        p1Vect = log(p1Num / p1Denom)  # change to log()
        p0Vect = log(p0Num / p0Denom)  # change to log()
        return p0Vect, p1Vect, pAbusive

    def classifyNB(self, vec2Classify, p0Vec, p1Vec, pClass1):
        p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult
        p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
        if p1 > p0:
            return 1
        else:
            return 0
