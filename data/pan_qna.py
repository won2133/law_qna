import json
import os
from tqdm import tqdm
import pandas as pd
#디렉터리 불러오기
path = '파일 위치/115.법률-규정 텍스트 분석 데이터_고도화_상황에 따른 판례 데이터/3.개방데이터/1.데이터/Training/02.라벨링데이터'
dir_list = os.listdir(path)

q = []
a = []
for d in dir_list:
    dir_path = os.path.join(path, d)
    print(dir_path)
    file_list = os.listdir(dir_path)
    #print(len(file_list))
    for file in tqdm(file_list):
        with open(os.path.join(dir_path, file), 'r',encoding='UTF8') as f:
            data = json.load(f)
            for qna in data['jdgmnInfo']:
                q.append(qna['question'])
                a.append(data['Summary'][0]['summ_pass'])


#디렉터리 불러오기_validation
path = '파일 위치/115.법률-규정 텍스트 분석 데이터_고도화_상황에 따른 판례 데이터/3.개방데이터/1.데이터/Validation/02.라벨링데이터'
dir_list = os.listdir(path)

for d in dir_list:
    dir_path = os.path.join(path, d)
    print(dir_path)
    file_list = os.listdir(dir_path)
    for file in tqdm(file_list):
        with open(os.path.join(dir_path, file), 'r',encoding='UTF8') as f:
            data = json.load(f)
            for qna in data['jdgmnInfo']:
                q.append(qna['question'])
                a.append(data['Summary'][0]['summ_pass'])

#디렉터리 불러오기_other(qna)
path = '파일 위치/115.법률-규정 텍스트 분석 데이터_고도화_상황에 따른 판례 데이터/3.개방데이터/1.데이터/Other/Other'
dir_list = os.listdir(path)

for d in dir_list:
    dir_path = os.path.join(path, d)
    print(dir_path)
    file_list = os.listdir(dir_path)
    for file in tqdm(file_list):
        with open(os.path.join(dir_path, file), 'r',encoding='UTF8') as f:
            data = json.load(f)
            #print(data)
        
            q.append(data['question'])
            a.append(data['answer'])

df = pd.DataFrame({'question': q, 'answer':a})
df.to_csv('pan_qna.csv', index=False)
