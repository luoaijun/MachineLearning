from numpy import *

from Classification.NaiveBayes.Byte import Bytes
byte = Bytes()
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)

    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWords);
    p1Num = zeros(numWords)  # change to ones()
    p0Denom = 0.0;
    p1Denom = 0.0  # change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] #侮辱性的
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]#非侮辱性的
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom  # change to log()
    p0Vect = p0Num / p0Denom  # change to log()
    return p0Vect, p1Vect, pAbusive
def nativeTest():
    listPosts, listClasses = loadDataSet()
    list = createVocabList(listPosts)
    trainMat = []
    for postDoc in listPosts:
        trainMat.append(setOfWords2Vec(list,postDoc))
    p0V,p1V,pAb = trainNB0(trainMat,listClasses)

if __name__ == '__main__':
    # nativeTest()
    byte.testingNB()
