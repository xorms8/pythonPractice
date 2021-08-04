"""
    [ 리스트 ]
      1- 임의의 객체를 순차적으로 저장하는 집합 자료형
      2- 각 값에 대해 인덱스 부여
      3- 변경가능 (**)
      4- 대괄호 [ ] 사용

      [참고]
      배열은 연속적으로 공간을 저장하는 것이니깐 파이션에는 없다
      파이션에서는 리스트를 사용한다
      배열은 생성시 크기를 지정하지만 리스트트 크기 제한이 없다
"""

# --------------------------------------------------------------------
# (1) 리스트 인덱스

arr = []                # 비워져 있는 리스트 생성
arr = [1,2,3,4,5]

""" [출력결과]
    [1, 2, 3, 4, 5, 10]
    [1, 2, 3, 4, 5, 10, 'hello']
    1
    10
    HELLO
    h
"""

arr.append(10)
arr.append('hello')
print(arr)
print(arr[0])
print(arr[5])
print(arr[6].upper())
print(arr[6][0])




# 이중 리스트 만들고 인덱싱하기
arr.append([])
print(arr)
# 비어있는 이중 리스트 'korea'를 추가
arr[7].append('korea')
print(arr)
print(arr[7][0][0])





""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상',['판교','부천']]]
    (1) '경상' 요소 추출
    (2) '부천' 요소 추출
    (3) '판'이라는 글자만 추출
"""
a = ['인천','부산',['전라','경상',['판교','부천']]]
print(a)
print(a[2][1])
print(a[2][2][1])
print(a[2][2][0][0])



""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']
    (1) '부산'부터 '대구'까지 추출
    (2) '대전'부터 '제주'까지 추출
    (3) '인천'부터 '서울'까지 추출
    (4) '광주'부터 '대구'까지 추출
"""
a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']

print(a[1:4])
print(a[3:6])
print(a[0:5])
print(a[3][1:3])

print("1번")
resultlist = []
for j in range(1,4):
    item = a[j]
    if(isinstance(item,list)):
        for i in range(len(item)):
            resultlist.append(item[i])
    else:
        resultlist.append(item)
print(resultlist)

print("2번")
resultlist = []
for j in range(3,6):
    item = a[j]
    if(isinstance(item,list)):
        for i in range(len(item)):
            resultlist.append(item[i])
    else:
        resultlist.append(item)
print(resultlist)

print("3번")
resultlist = []
for j in range(0,5):
    item = a[j]
    if(isinstance(item,list)):
        for i in range(len(item)):
            resultlist.append(item[i])
    else:
        resultlist.append(item)
print(resultlist)

print("4번")
resultlist = []
for j in range(3,4):
    item = a[j]
    if(isinstance(item,list)):
        for i in range(len(item)):
            resultlist.append(item[i])
    else:
        resultlist.append(item)
print(resultlist)


#0804 15:41 과제
#2. 리스트 다루기
#다음 코드의 실행 결과를 쓰시오
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])
#1.[0,1,2] [0,1]

a = [0, 1, 2, 3, 4]
print(a[::-1]) #리버스
#2.[4,3,2,1,0]


first = ["egg", "salad", "bread", "soup", "canafe"]

second = ["fish", "lamb", "pork", "beef", "chicken"]

third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]
print(order[0][:-2]) # egg salad bread
print(second[1::3]) #lamb chicken
print(third[0]) # apple
john = [order[0][:-2], second[1::3], third[0]]
del john[2] #third 삭제
#[['egg','salad','bread'], ['lamb' , 'chicken']]
john.extend([order[2][0:1]]) # apple

#extend : iterable의 각 항목을 넣음

print(john)
#3.[['egg','salad','bread'], ['lamb' , 'chicken'] , ['apple']]



list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)
#4 [1,2,3,4] None??????
#list_a.sort()는 return 값이 없는 함수이다. 그래서 list_b = list_a.sort() 로 실항하여도 list_b에는 값이 들어가지 않는다.
#만약 list_b 값을 sort된 값으로 받고 싶으면 list_b = sorted(list_a) 로 수정해야 한다. sorted는 return 값이 있다.


fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']

print(fruits[-3:], fruits[1::3])
#5 [['apple', 'banana', 'cherry', 'grape'] [banana .orange]

num = [1, 2, 3, 4]

print(num * 2)
#6  X  [[1, 2, 3, 4] [1, 2, 3, 4]]  / -> [1,2,3,4,1,2,3,4]


a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
#a= [1,2,3,4,'g']
b.append(6)
#b= ['a','b','c','d','e',6]
print('g' in b, len(b)) #len은 1부터
#7 False 6



list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']

list_b=[ ]

for i in range(len(list_a)):

    if i % 2 != 1: #짝수 값 인덱스면

        list_b.append(list_a[i])

print(list_b)

#8 if문 #짝수 값 인덱스면
# ['Hankook' , 'is' ,'academic', 'located' , 'South Korea']

#admission_year = input("입학 연도를 입력하세요: ")

#print(type(admission_year))
#9 3번 str 날짜는 문자열

country = ["Korea", "Japan", "China"]

capital = ["Seoul", "Tokyo", "Beijing"]

index = [1, 2, 3]

country.append(capital)
print(country)
print(country[3][1])
country[3][1] = index[1:]
#Tokyo = index [2,3]
print(country)
#10 ['Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]


a = [5, 4, 3, 2, 1]

b = a

c = [5, 4, 3, 2, 1]

print(a is b)
print(a is c)
'''
is 키워드는 주소를 비교한다.
a의 배열 주소 값은 b가 되었다 -> b = a 주소값이 같은 상황
a is c 를 비교할때 배열값은 [5,4,3,2,1]로 동일할테지만 주소값은 다른 배열이다.
같은 검은색 티셔츠를 입었지만 다른 집에서 나온 것처럼 타인이다.
'''


a = 1

b = 1

print(a is b)

True

a = 300

b = 300

print(a is b)

False
#원래 숫자 256을 벗어난 수에서는 새로운 주소를 할당하여 저장하기떄문에  False를 리턴하였지만
#최근 파이썬에는 두 값을 비교하는 형태로 바뀌었기 때문에 True를 리턴한다.


list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1
print(a,b,c) # [1, 2, 3, 4, 5, 6]
#3개의 요소가 들어가있는 배열을 변수에
list_2 = a + b + c

print(list_2)

# --------------------------------------------------------------------
# (2) 리스트 연산자

a = ['독','도','는']
b = ['대한민국','섬']



# --------------------------------------------------------------------
# (3) 리스트 관련 함수들
#           append()    : 요소 추가
#           sort()      : 리스트 정렬
#           reverse()   : 역순으로 뒤집기
#           index()     : 위치 반환
#           insert()    : 리스트에 요소 삽입
#           remove()    : 요소 제거
#           pop()       : 맨 마지막 요소를 꺼내기
#           count()     : 요소 개수 세기
#           extend()    : 리스트에 리스트를 더하기\
#           clear()     : 모든 요소를 제거

"""
    (1) 리스트 a에 0 요소 추가
    (2) 리스트 a에 9를 추가하여 출력 (a요소에는 추가하는 것은 아님)
    (3) 0번째 요소로 1을 추가
    (4) 3번째 요소로 1을 추가
    (5) 리스트 맨 마지막 요소를 꺼낸다
    (6) 요소 1을 삭제 ( 1이 여러개인 경우 맨 앞에 하나만 삭제됨 )
    (7) 리스트 모든 요소를 삭제
"""
a = [7, 2, 3, 5, 6] 
a.append(0)



"""
# [참고] 리스트에 리스트 구조에서 clear() 하는 경우
a1 = [1]
b1 = [7,6, 5,4,3, a1]
print(a1)
print(b1)
b1.clear()  # 종속관계로 되어 있기에 b1의 내용만 삭제되고 a1은 유지왼다
print(b1)
print(a1)
print()
"""


"""
    (8) 리스트 a의 모든 요소를 역순으로 뒤집기
    (9) 리스트 a 정렬하기
    (10) 리스트 a에 리스트 b를 더하기
    (11) 리스트 a에서 0번째부터 1번째 요소까지 삭제
"""
a = [3,5,4,8,0]
b = [1,2]





# --------------------------------------------------------------
#  (4) 리스트 요소 변경
#       - 2번째 요소를 'z'로 변경
#       - 0번째부터 1번째 요소를 'k'와 'o'로 변경

