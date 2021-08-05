"""
     {} 사용
    4- 변경가능[ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt[1]) #요거 인덱스 아닙니다 key 값입니다.
#three 값을 출력하려면 ?
print(dt['3'])

dt = {1:'one', 2:'two', '3':'three', 1:'first'}
print(dt) #결과 :  {1: 'first', 2: 'two', '3': 'three'} 1의 key값이 'first'가 뒤에 들어왔는데 덮어짐

dt = {1:'one', 2:'two', '3':'three', 3:'third'}
print(dt) #결과 : {1: 'first', 2: 'two', '3': 'three', 3:'third'}





# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}

#tuple 을 출력하려면 ?
print(dt2[(3,4)]) #(3,4) <-요거 자체가 key 값인 tuple이다

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
# 1- turple 값을 python으로 변경
dt2[(3,4)] = 'python'
print(dt2)
# 2- korea 키에 '한국' 값 추가
dt2['korea'] = '한국' # dt[키값] = 'value'
print(dt2)
# 여러개 추가할 때
dt2.update({5: 'five', 6: 'six', 7: 'seven'})
print(dt2)


print('--------- 3. Key로 Value값 찾기  --------------- ')
print('dt2 : ' ,dt2)
print(dt2[2])
print(dt2.get(2))

#print(dt2[3]) #에러
print(dt2.get(3)) # none
print(dt2.get(3 , '없음')) #none말고 default 값을 원하는 메시지로 변경 할수 있음




# Key와 Value만 따로 검색
print('===========# Key와 Value만 따로 검색=============')
print(dt2.keys())
#dict_keys([1, 2, (3, 4), 'korea', 5, 6, 7])
print(dt2.values())
#dict_values(['one', 'two', 'python', '한국', 'five', 'six', 'seven'])
print(dt2.items())
#ict_items([(1, 'one'), (2, 'two'), ((3, 4), 'python'), ('korea', '한국'), (5, 'five'), (6, 'six'), (7, 'seven')])