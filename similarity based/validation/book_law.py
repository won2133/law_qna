import json
import os
#디렉터리 불러오기
path = '파일위치/029.대규모 구매도서 기반 한국어 말뭉치 데이터/01.데이터/1.Training/라벨링데이터/TL_360'
file_list = os.listdir(path)
    
sList = []


for file in file_list:
    with open(os.path.join(path, file), 'r',encoding='UTF8') as f:
        print(file)
        data = json.load(f)
        print(len(data['paragraphs']))
        for paragraph in data['paragraphs']:
            for s in paragraph['sentences']:
                sList.append(s['text'])

print(sList[:10])
print(len(sList))

#파일 저장
f = open("book_law_data.txt",'a')
for s in sList:
    f.write(s+'\n')
f.close()
