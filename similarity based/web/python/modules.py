import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm
from math import *
from sentence_transformers import SentenceTransformer
from konlpy.tag import Kkma
import re


model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
kkma = Kkma()

def str_to_vector(emd):
    res = emd.split(' ')
    #print(emd)
    #print(len(r))
    r = []
    for a in res:
        if len(a) >2:
            r.append(a)
    if len(r) != 768:
        print(len(r))
    for i in range(len(r)):
        r[i] = r[i].replace('[', '')
        r[i] = r[i].replace(']', '')
        r[i] = r[i].replace('\n', '')
        r[i] = float(r[i])
    return np.array(r)


def tokenize_sentence(sentence):
    stopwords = ['하', '의', '에', '이', '는', '을', '가', '되', '를', '있', '여', '으로', '경우', '는가', '수', '아', '로', '그', '은', '고', '제', '것', '지', '에서', '저', '대하', '조', '어', '등', '행위', '관하', '해당', '보', '항', '에게', '및', '과', '받', '와', '없', '의하', '다고', '처분', '않', '또는', '였', '었', '나요', '따르']
    tokenized_sentence = []
    tokenized_sentence = kkma.morphs(sentence) # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    l = ''
    for s in stopwords_removed_sentence:
        s = re.sub(r"[^가-힣\s]", " ", s)
        l += s +' '
    return l

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def jaccard_similarity(x, y):
    intersection_cardinality = set(x).intersection(set(y))
    union_cardinality = set(x).union(set(y))

    return len(intersection_cardinality) / len(union_cardinality)

def return_answer(q, df):
    q = tokenize_sentence(q)
    embedding = model.encode(q)

    #유사도 계산 및 정렬
    sim_scores = [[k, 0.1*jaccard_similarity(df['question'][k], q)+0.9*cos_sim(df['emd'][k], embedding)] for k in range(len(df))]
    sim_scores.sort(key=lambda x: x[1], reverse=True) #sim_scores의 각 리스트 중 두번째 요소를 정렬 기준으로

    #상위 다섯 개 저장(중복 제거)
    result = [] #전체
    score = []
     for sim in sim_scores:
        a = df['answer'][sim[0]].split('다.')[:-1]
        if a not in result:
            result.append(a)
            score.append(sim[1])
        else:
            #print(a)
            pass
        if len(result) == 5:
            break
    print(score)
    return result

