import json

# f = open('./data/temp.json','r',encoding='utf-8')
# data = f.read()
# print(data)
#
# items = json.loads(data) #읽어온 data를 json 구조로 -> dict타입으로
# print(items)
#
# print(type(data)) #str
# print(type(items)) #dict
#
# for k, val in items.items(): # dict의 items()는 키밸류 값을 같이 출력
#     print(k , ":" , val)


#sample.json 파일을 읽어서 항목별 총합 구하기


f = open('./data/sample.json','r',encoding='utf-8')
data = f.read()

items = json.loads(data) #읽어온 data를 json 구조로 -> dict타입으로
print(items)

print(type(data)) #str
print(type(items)) #dict


sum = 0
for k, val in items.items(): # dict의 items()는 키밸류 값을 같이 출력
    sum = val.get('price') * val.get('count')
    print('{}의 합산 결과 : '.format(k), sum)