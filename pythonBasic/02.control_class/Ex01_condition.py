"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    if a>b:
        print(a)

    print(b)


    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = -1;
if a :
    print('True1') # ****** 0이 아닌 수는 값이 있다고 쳐서 True가 반환됨 !
else :
    print('False1')

a= 10
b= -1
print(a and b) # -1 ->a는 true지만 and 조건이기 때문에 b의값을 대조해야하는 상황 ->b도 true 이므로 b의 값으로 출력됨
print(a or b) # 10 ->이미 a 가 true 값이기 떄문에 or조건과 크게 상관없이  a의 값인 10이 나옴

''' B의 값에 따라 true false를 반환함
    A   B       A & B(and)    A | B (or)
    =================================
    t   t         t             t
    t   f         f             t
    f   t         f             t
    f   f         f             f
'''
if a and b: #둘다 0이 아닌 변수값이면
    print('True2') # True2 출력
else :
    print('False2')

if a or b: #둘중에 하나라도 0이 아닌 변수값이면
    print('True3') # True3출력
else :
    print('False3')


a = 0
if a:
    c = 2
elif b:
    c = 4
else :
    c = 6

print(c)




#--------------------------------------------------------
word = 'korea'

if word.find('k'): # korea 중에서 'k' 포함하면 출력
    print('1>', word)
# word.find('k')의 index 값을 보면 0이다 그래서 if문에 false로 들어간다
# if 0 : -> false
if word.find('z'): # korea 중에서 'z' 포함하면 출력
    print('2>', word)
# word.find('z')의 값은 'korea'에 없다. 그래서 -1을 반환한다. 근데 -1은 파이썬 if문의 true 값이다.
# if -1 : ->true