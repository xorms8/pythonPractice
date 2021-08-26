
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)

for entry in e.items():
    print('e dict의 result :' ,entry)
    print('e dict의 키 밸류를 인덱스로 -> ',entry[0], entry[1])

for key, val in e.items():
    print('key=', key, 'value=', val)



#1~10까지 합 구하기
result =0
for i in range(1,11):
    result += i

print(result)
#답 :55

#1~10까지 홀수의 합
result =0
for i in range(1,11):
    if i % 2 == 1:
        result += i

print(result)

#1~10까지 홀수의 합 python 방식
result =0
for i in range(1,11,2):
    result += i

print(result)
"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""

for i in range(2,10):
    print(" ")
    for j in range(1,10):
        print(i, '*',j ,'=', i*j)



#---------------
#while

a = ['z', 'y' ,'x']

while a: #집합 요소에 빈 요소인 경우만 False, 요소 하나라도 있으면 True
    data = a.pop() # 마지막 요소를 뽑는 pop()
    print(data) # x y z
    if data == 'y' : break
    print(a)
else:
    print(a)
    print('end')

#1. 다음 코드의 실행 결과를 쓰시오

fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)

#내답 : 'apple'

#2. 다음 코드의 실행 결과를 쓰시오.
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])

#내답 : [3, 4.0]

#3. 다음 코드의 실행 결과를 쓰시오.
num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break # i가 1, 2 일땐 통과 !!
    i += 1
    num += i # 결국 num에 2+3
# 3
print(num)

#내답 : 2+3 =5

#4. 다음 코드의 실행 결과를 쓰시오.
result = 0
#5 3 1 -1 -3 -5 ---> -1 -1 -1 -1 -1 +1
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)

#내답 : -5
num1 = 1
#5. 다음 코드의 실행 결과를 쓰시오

num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue #위에 if문이 true면 아래 코드 통과
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num
print(num)
# 1 3 5 6 8 9

#6. 다음 코드의 실행 결과를 쓰시오.
coupon = 0
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)
money = 20000
#money = 1800

'''
20000> 3500
만약 쿠폰이 4보다 작으면
=16500 / 쿠폰 1
-------------------------
16500> 3500 / 쿠폰 1
만약 쿠폰이 4보다 작으면 
=13000 / 쿠폰 2
------------------------------
13000> 3500 / 쿠폰 2
만약 쿠폰이 4보다 작으면
= 9500 / 쿠폰 3 
-----------------------------
9500> 3500 / 쿠폰 3
만약 쿠폰이 4보다 작으면
= 6000 / 쿠폰 4
-------------------------------
6000 > 3500 /쿠폰 4
만약 쿠폰이 4보다 작지않으므로
6000 + 2800 = 8800
쿠폰 0
-----------------------------

8800 >3500 쿠폰0
만약 쿠폰이 4보다 작으면 
= 5300 / 쿠폰 1
-----------------------------
5300 > 3500 쿠폰 1
만약 쿠폰이 4보다 작으면
= 1800 / 쿠폰 2



결론 1800 쿠폰 2
'''


#7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j

print(result)
# 3 pwd


#=============파이썬 기초 프로그래밍 과제

'''
1. 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
또 숫자중에서 평균을 출력하여 보자.


정수를입력하세요: 10
정수를입력하세요: 20
정수를입력하세요: 30
정수를입력하세요: 40
정수를입력하세요: 50

평균= 30.0
'''
#sum = 0
#for i in range(1,6):
#    result = int(input('정수를 입력하세요 : '))
#    sum += result
#print('평균= ',sum / 5)

'''
2. 사용자에게서받은문자들을 역순으로 출력한다.
문자열입력:  abcde
결과 : edcba
'''

#words = input('문자열입력 : ')
#print('결과 : ', words[::-1])

'''
3. 사용자에게서받은정수들의평균과표준편차를계산하여출력한다. 평균과표준편차를프로그램을 작성하세요
정수리스트입력: 10 20 30 40 50
평균= 30.0
표준편차 15.81
'''

import numpy
numpy.numbers = [int(x) for x in input('정수리스트 입력 : ').split()]
print('평균 =', numpy.mean(numpy.numbers))
print('표준편차=', numpy.std(numpy.numbers))

'''
4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.

문자열을입력하시오: NUMBER

686237
'''
dial = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
strings = input('문자열입력->')
results = ''
for char in strings: #
    for i in range(len(dial)):
        if char.upper() in dial[i]:
            results += str(i + 1)
print(results)



