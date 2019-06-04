from collections import Counter


def nr(str):
    dictCount = Counter(str)  # 第一步计数
    dictSort = sorted(dictCount.items(), key=lambda d: d[1], reverse=True)  # 第二步排序
    dictSout = dict(dictSort)
    dictNr = []

    for j in range(list(dictSout.values())[0]):
        for i in range(dictSout.__len__()):
            if list(dictSout.values())[i] > 0:
                dictNr += list(dictSout.keys())[i]
                dictSout[list(dictSout.keys())[i]] = list(dictSout.values())[i] -1
            else:
                dictNr += ''

    print(str)
    print(dictNr)


if __name__ == '__main__':
    s = ['a', 'a', 'a', 'v', 'c', 'c', 's', 's', 'f', 'f', 'g']
    nr(s)
