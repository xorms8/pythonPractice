"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

#name = input('이름 입력 ->')
#print('당신은' , name , '입니다')

#format() 이용하여 출력
#print('당신은 {} 입니다.'.format(name))
#%이용하여 동일하게 출력
#print('당신은 %s 입니다.' % name )
#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
age = float(input('나이를 입력하세요 : '))
age +=1
print(age)

height = eval(input('키를 입력하세요 : ')) #오 정수형(ex: 150) int type 실수를 넣으면 (ex:150.5) float type
print(height)
print(type(height))

print('1+2')
print(eval('1+2'))



#----------------------------------
# 단을 입력받아 구구단을 구하기
'''
dan = int(input('단을 입력하세요:'))
for i in range(1,10):
    print("{} * {} = {}".format(dan, i, dan*i))
'''



#-----------------------------------------
# print() 함수
print('안녕', '친구')

for i in range(5): #자동으로 개행되어서 출력됨
    print(i)
'''
0
1
2
3
4
'''
for i in range(5):
    print(i, end=',' if i<4 else '') #,로 구분할거야 i가 4보다 작을때 까지 / 그게 아니면 '' -> ,안찍을거야
#0,1,2,3,4
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
'''
    public class Test{
        public static void main(String [] args){
            
        }
    }
    파일명 : Test.java
    
    javac Test.java (컴파일 성공 : Test.class)
    java Test
    
    java Test 192.168.0.1 scott tiger
                [0]        [1]    [2] 
                요 0,1,2, 192.168.0.1 scott tiger 요 값들이 args 아규먼트 값으로
'''
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

# python ./a_datatype_class/Ex10_stdio.py ourserver scott tiger

import sys
args = sys.argv[1:]
for i in args:
    print(i)
