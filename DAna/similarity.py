from __future__ import division
from math import sqrt
import jieba
import pandas as pd
import jieba.analyse

jieba.initialize()
jieba.enable_parallel(4)

def keys_counter(content, per=0.33, top=20):
    """
    统计 词频，并用词的汉明重量 修正 33%。
    """
    items = jieba.cut_for_search(content)
    ds = jieba.analyse.extract_tags(content,withWeight=True)
    d = dict.fromkeys([i[0] for i in ds], 0)
    for i in items:
        if i in d:
            d[i] += 1
    d = pd.Series(d)
    ds = pd.Series({i[0]: i[1] for i in ds})
    return d - (d * ds * per)


class Raw:

    def __init__(self, *texts):
        self._raw = pd.DataFrame([keys_counter(text) for text in texts]).fillna(0)

    def similarity(self):
        data = self._raw
        length = len(data.index)
        count = len(data.columns)
        Table = pd.DataFrame(index=data.index, columns=data.index).fillna(0)
        for i in range(length):
            for i2 in range(length):
                d1 = data.loc[i]
                d2 = data.loc[i2]
                
                # SqrSum = lambda v : sum([x**2 for x in  v])
                sqr1 = (d1 **2).sum()
                sqr2 = (d2 **2).sum()
                N = (d1 * d2).sum() - d1.sum() * d2.sum() / count
                D = sqrt((sqr1 - d1.sum()**2/ count ) *( sqr2 - d2.sum()**2 / count ))
                print(N,D)
                if D== 0:
                    Table[i][i2] = 0
                Table[i][i2] = 1.0 - N/D
        return Table




