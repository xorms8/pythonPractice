"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

#() 인자도 없고 리턴값도 없는 함수
# def func():
#     print('inside func')
#
# func()
# result =func() # 리턴값이 없으니 None을 출력
# print(result)

#(1) 리턴값이 여러개인 함수
def func(arg):
    return arg*2, arg+20
result = func(10)
print(type(result))
print(result)

print('unpacking')
a,b = func(5)
print(a,b)

# (2) 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!', name + '님')

func('안녕','홍길동')
func('길동','HELLO')

# (3) 키워드 인자 (keyword argument)
def func(greeting, name):
    print(greeting, '!!!!', name + '님')

func(greeting='안녕', name='홍길동')
func(name='길동', greeting='HELLO')

# (4) 인자(매개변수)의 기본값 지정하기
print('인자(매개변수)의 기본값 지정하기')

def func(greeting, name="기본값을 지정!"): #name들어오는값에 기본값을 지정한 상황
    print(greeting, '!!!!', name + '님')

# func('안녕', '홍길동', '서울') 인자가 넘치면 오류
func('안녕')
func('하이', "스미스")

def func(a,b,c=100):
    return a*2 + b*3 + c*4

print(func(1,2)) # 2 + 6+ 400 = 408
print(func(1,2,3)) # 2+ 6+ 12 = 20
print(func(c=1,b=2,a=3)) # 6+ 6+ 4 = 16




'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
print(' (5) 위치 인자 모으기 (*)')
def func(a,b,c=0,*args): # *********** 지정한 a,b,c 중요함 위치인자 값이 몇개인지 모르지만 들어올 거를 튜플로 처리하는 엄청난 놈
    sum = a + b + c
    #print('*args : ', args)
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다

#-------------------------------------------
# (6) 키워드 인자 모으기(**)
'''
    *args  : positional argument 만 받을 때
    **kwargs  : keyword argument 받을 때
'''
print('6. 키워드 인자 모으기')

# 특징 : 4,5 - 즉 2개까지는 무조건 들어온다, 3개는 c로 기본값 주자!

def func(a,b,c=0, *args, **kwargs):
    sum = a + b + c
    # print('*args : ', args)
    # for i in args: #튜플이 넘어올거임
    #     sum += i
    print("kwargs: ", kwargs) #kwargs 딕셔너리
    for k in kwargs:
        sum += kwargs[k]
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, kor=10, eng=20, math=30))
print(func(4, 5, 6, kor=10, math=30))

#4. 함수 카페 문제

#1.다음 코드의 실행 결과를 쓰시오
print('1.다음 코드의 실행 결과를 쓰시오')
def test(t):
    t = 20
    print("In Function:" ,t) #20

x = 30
print ("Before",x) # 10 / x=10값 그대로
test(x)
print("After",x) # 10 / x=10값 그대로, 위 함수는 이 밑의 print에서는 전혀 무관함 return이 없기 때문에

#2.다음 코드의 실행 결과를 쓰시오
print('2.다음 코드의 실행 결과를 쓰시오')

def sotring_function(list_value):
	return list_value.sort()

print(sotring_function([5,4,3,2,1]))
#답 : None

print('2-1.none 값 말고 정렬 후 출력해보기')
def sotring_function(list_value):
	return sorted(list_value)

print(sotring_function([5,4,3,2,1]))
#.sort()요거자체가 리턴값이 없다.
#sorted()요걸 써야 진짜 원하는 정렬값을 출력할 수 있다.


#3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
print('3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def is_yes(your_answer):
	if your_answer.upper() == "YES" or your_answer.upper() == "Y":
		result = your_answer.lower()

print(is_yes("Yes"))
#답 : 'None' ->함수에 return이 없으면 - > None !

#4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
print('4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def add_and_mul(a, b, c):
	return b + a * c + b

print(add_and_mul(3, 4, 5) == 63) # 23 == 63 ->False

#5. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
print('5. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def args_test_3(one, two, *args):
	print(one + two + sum(args))
	print(args)

args_test_3(3, 4, 5, 6, 7)

# three 로 인해 error
# three 제거하면
#25
#(5, 6, 7)

#6. 다음 코드의 실행 결과를 쓰시오.
print('6. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def rain(colors):
	colors.append("purple")
	colors = ["green", "blue"]
	return colors

rainbow = ["red", "orange"]
print(rain(rainbow))

# 답 : ['green', 'blue']

#7. 다음 코드의 실행 결과를 쓰시오.
print('7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def function(value):
    print(value ** 3)
print(function(2))

# 2의 3승 = 8

#8. 다음 코드의 실행 결과를 쓰시오.
print('8. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def get_apple(fruit):
	fruit = list(fruit)
	fruit.append("e")
	fruit = ["apple"]
	return fruit

fruit = "appl"
get_apple(fruit)
print(fruit)

#답 appl fruit = "appl" 전역변수로 함수 밖에서 변수가 지정되었다.
# 그렇다고 지역변수=함수 내 fruit 와 같게 해준것도 아니다.

#9. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
print('9. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def return_sentence(sentence, n):
	sentence += str(n)
	n -= 1
	if n < 0:
		return sentence
	else:
		return(return_sentence(sentence, n))

sentence = "I Love You"
print(return_sentence(sentence, 5))

#0일때 까지 도는 과정
#답 : ➂ I Love You543210

#10. 다음 코드의 실행 결과를 쓰시오.
print('10. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? ')
def test(x, y): # y, x
	tmp = x # tmp = y
	x = y # x = x
	y = tmp # y = y
	return y.append(x)

x = ["y"]
y = ["x"]
test(x, y)
print(y)

#전역변수라서 밖에서 선언한 y = ["x"]
#print(y) -> 'x'

#11. 다음 코드를 실행하면 결과값으로 120이 나온다. 빈칸에 들어갈 알맞은 코드를 작성하시오.
print('11. 다음 코드를 실행하면 결과값으로 120이 나온다. 빈칸에 들어갈 알맞은 코드를 작성하시오.')
def factorial_calculator(n):
	if n in (0, 1):
		return 1
	else:
	    return n * factorial_calculator(n-1)

print(factorial_calculator(5))


#[연습문제]
print('연습문제 1번')
def even_filter (list):
    list = [n for n in list if n % 2 == 0]
    return list

print(even_filter([1, 2, 4, 5, 8, 9, 10]))


print('연습문제 2번')
def is_prime_number (n):
    for i in range (2 , n):
        if n % i ==0:
            return False
    else:
        return True

print(is_prime_number(60))
print(is_prime_number(61))

print('연습문제 3번')




# [문항1] 홍길동씨의 주민등록번호는 880122-1234567 이다.
#   주민번호에서 생년월일만 birthday 변수에 저장하고 성별을 구하는 숫자를 gender 변수에 저장한 후
#   출력한다
#     pin = '880122-1234567'
#     (1)___________________
#     (2)___________________
#     print( birthday )
#     print( gender )
#
#     [출력결과]
#     홍길동님 생년월일 : 880122
#     성별 : 남자

#[문항 1]
'''

[문항1] 홍길동씨의 주민등록번호는 880122-1234567 이다.
  주민번호에서 생년월일만 birthday 변수에 저장하고 성별을 구하는 숫자를 gender 변수에 저장한 후
  출력한다
    pin = '880122-1234567'
    (1)___________________
    (2)___________________
    print( birthday )
    print( gender )

    [출력결과]
    홍길동님 생년월일 : 880122
    성별 : 남자
'''
print('문항1')
pin = '880122-1234567'
birthday = print("홍길동님 생년월일 : ", pin[:6])
if(int(pin.split("-")[1][0])) ==1:
	gender='성별 : 남자'
else:
	gender='성별 : 여자'
print(birthday)
print(gender)






#[문항 2]
print('문항 2')
a=[1,3,5,4,2]
print(sorted(a)[::-1])
a=[1,3,5,4,2]
a.sort(reverse=True)
print(a)

#[문항 3]
print('문항3')
a = ['독도는', '대한민국의', '아름다운', '섬입니다']
result =" ".join(a)
print(result)

#[문항4]
a=(1,2,3)
lista=list(a)
lista.append(4)
a=tuple(lista)
print(a)

i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

print('문항5')
a = [1, 2, 3]
a[1] = 5
print(a)


print('문항7')
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]

print(midterm_score)
print(midterm_score[1])
# 총점과 평균

sum=0
average=0
for i in range(len(kor_score)):
	sum += kor_score[i]
	average= sum / len(kor_score)

for i in range(len(math_score)):
	sum1 = sum + math_score[i]
	average1= sum1 / len(math_score)

for i in range(len(eng_score)):
	sum2 = sum + eng_score[i]
	average2= sum2 / len(eng_score)

print(len(midterm_score))
# for i in range(len(midterm_score)):
# 	sum3 = sum + midterm_score[i]
# 	average3= sum / len(midterm_score)
print('국어 총점 :',sum)
print('국어 평균 :',average)
print('수학 총점 :',sum1)
print('수학 평균 :',average1)
print('영어 총점 :',sum2)
print('영어 평균 :',average2)

print('전체 과목 총점 :',sum+sum1+sum2)
print('전체 중간고사 평균 :',(average+average1+average2)/3)