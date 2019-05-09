from numpy import *


class Bytes:
    def loadDataSet(self):
        postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                       ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                       ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                       ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                       ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                       ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
        classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
        return postingList, classVec

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

    '''
    朴素贝叶斯分类器训练器
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

    def testingNB(self):
        listOPosts, listClasses = self.loadDataSet()
        myVocabList = self.createVocabList(listOPosts)
        trainMat = []
        for postinDoc in listOPosts:
            trainMat.append(self.setOfWords2Vec(myVocabList, postinDoc))
        p0V, p1V, pAb = self.trainNB0(array(trainMat), array(listClasses))
        testEntry = ['love', 'my', 'dalmation']
        thisDoc = array(self.setOfWords2Vec(myVocabList, testEntry))
        print(testEntry, 'classified as: ', self.classifyNB(thisDoc, p0V, p1V, pAb))
        testEntry = ['stupid', 'garbage']
        thisDoc = array(self.setOfWords2Vec(myVocabList, testEntry))
        print(testEntry, 'classified as: ', self.classifyNB(thisDoc, p0V, p1V, pAb))