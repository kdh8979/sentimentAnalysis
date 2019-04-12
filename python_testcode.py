# -*- coding: utf-8 -*-
from konlpy.tag import Twitter
import timeit
twitter = Twitter()

# 하하하
def tokenize_by_twitter(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in twitter.pos(doc, norm=True, stem=True)]

def tokenize_by_twitter_ver2(doc):
    result = []
    banPumsa = ['Punctuation','Josa']
    for t in twitter.pos(doc, norm=True, stem=True):
        if t[1] in banPumsa:
            continue
        if str(t[0]).__len__()<=1:
            continue
        result.append(t[0]+"/"+t[1])
    return result

def tokenize_by_mecab2(doc):
    result = []
    banPumsa = ['SF','SE','SS','SP','SO','SW','SL','SH','SN']
    for t in Analyzed_By_Mecab(doc):
        if t[1] in banPumsa:
            continue
        if str(t[0]).__len__()<=1:
            continue
        result.append(t[0]+"/"+t[1])
    return result

if __name__ == "__main__":
    start = timeit.default_timer()
    doc = "나는 등산은 별로야"
    result1 = tokenize_by_twitter(doc)
    print(result1)

    result2 = tokenize_by_twitter_ver2(doc)
    print(result2)
    stop = timeit.default_timer()
    print(stop - start)
