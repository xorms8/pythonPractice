# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False

print(type(hungry)) # True
print(not hungry)  # False
print(hungry and sleepy) #False
print(hungry or sleepy) # True
print(hungry & sleepy) #False
print(hungry | sleepy) # True






"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


if('아'):
    print('True')
else:
    print('False')
-> 내 답 : True
if([]):
    print('True2')
else:
    print('False2')
-> 내 답 : False2
"""

if('아'):
    print('True')
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2')


if(0):
    print('True3')
else:
    print('False3')

if(-1):
    print('True4')
else:
    print('False4')


#문제

#1
a = 11
b = 9
print('a' + 'b')
# 내답 -> ab 답 :3

#2
fact = "Python is funny"
print(fact.count('n')) #3
print(fact.find('n')) #5
print(fact.rfind('n')) #13
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))
# 내답 -> 3 + 5 + (1+2+9)

#3
text = 'Gachon CS50 - programming with python'
text2 = " Human cs50 knowledge belongs to the world "
text.lower()
print(text[:5] + text[-1] + text[6] + text2.split()[0])
#내답 gacho + n + ' ' +  Human

#4
class_name = "introduction programming with python"
for i in class_name:
    if i == 'python':
        i = i.upper()
print(class_name)
#답 : introduction programming with python i의 값 즉 class_name 문자형은
# 문자형 python이 아니기 떄문

#5

a = '10'

b = '5-2'.split('-')[1]

print(a * 3 + b) #태근아.. a='10' 문자열 이잖니.. ㅋㅋ
#수정 답 -> 1010102

#6
a = "abcd e f g"

b = a.split()
#'abcd' 'e' 'f' 'g'
c = (a[:3][0])
#a ->'abc'의 0번째 값 = a
d = (b[:3][0][0])
#a -> 'abcd' 'e' 'f' 의 0번째 'abcd'값에서 ~0번째 = a
print(c + d)
#aa

#7

result = "CODE2018"

print("{0},{1}".format(result[-1], result[-2]))
# 8,1

#8
#3번
