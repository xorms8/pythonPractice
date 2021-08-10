
#파이썬 리스트 -> csv 파일에 저장
import csv

data = [[1,'김','책임'],[2,'박','선임'],[3,'주','연구원']]

with open('./data/imsi.csv', 'wt', encoding='utf-8-sig') as f:
    cout = csv.writer(f)
    cout.writerows(data) #개행이 또들어감

#csv파일 읽어서 파이썬 리스트 저장


with open('./data/imsi.csv', 'rt', encoding='utf-8') as f: #r(t) t(텍스트) 기본, r(읽기)만 적어도 됨
    cin = csv.reader(f)
    result = [row for row in cin if row] # if row -> row가 있으면 ~~~~~~~~

print(result)
