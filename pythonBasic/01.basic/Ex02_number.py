"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25
            - 16진수  0x25
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승 (n제곱)
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음         
"""

a = 5
b = 2

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""
add = a + b
minus = a - b
multi = a * b
division = a / b
tdivision = a // b
rest = a % b
square = a**b
print('a + b = ', add)
print('a - b = ', minus)
print('a * b = ', multi)
print('a / b = ', division)
print('a // b = ', tdivision)
print('a % b = ', rest)
print('a ** b = ', square)

#===========================
# 0803 과제
#
a=777
b=777
print(a==b, a is b)

#2. 다음 중 변수를 메모리에서 삭제하기 위해 사용하는 명령어는?
#➀ del ➁ delete ➂ remove ➃ pop ➄ clear
#답 1번

#3. 빈칸에 들어갈 각각의 코드 실행 결과를 쓰시오.
a=3.5
b=int(3.5)

print(a**((a//b))*2)
print(((a-b)*a)//b)
b=(((a-b)*a)%b)
print(b)
print((a*4) % (b*4))

#4. 입력받은 섭씨온도를 화씨온도로 변환하는 프로그램을 코딩하려고한다. 코드 순서가 올바른 것은?

#(1) fahrenheit = (( 9 / 5) * celsius) + 32

#(2) celsius = input("섭씨온도를 입력하세요:")

#(3) print("섭씨온도:",celsius, "화씨온도:", fahrenheit)

#(4) celsius = float(input("섭씨온도를 입력하세요:"))

#답 - > 4번 (4)의 섭씨 온도 입력은 X.XXXXX가 가능하기 때문


#5. 다음 변수 a의 자료형은
#답 -> 2번
#a = "True" ->문자형
#a = True -> 불린형
a = True
print(a)

#6. 다음과 같은 코드 작성 시, 실행 결과로 알맞게 짝지어진 것은?
a= 10.6
b= 10.5
print(a*b)
type(a+b)

# 답 : 3번 111.3 float

#7. 다음과 같은 코드를 작성했을 때, 실행 결과로 알맞은 것은?

a="3.5"
b=4
print(a*b)

#답 2번 3.53.53.53.5  // 3.5가 4번 출력됨 ㅋㅋㅋ 문자열을 곱해서 나타내는 파이썬

#8. a = "3.5", b = "1.5"일 때, print(a + b)의 실행 결과는?


