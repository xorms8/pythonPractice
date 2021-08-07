msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

#(1) unpacking : 각 요소를 분해(풀기)

a,b,c, = li #파이썬은 변수 갯수만 맞춰놓으면 하나씩 요소를 풀어줌
print(a)
print(b)
print(c)
#a
#b
#c

a,b,c = di.items() #파이썬은 변수 갯수만 맞춰놓으면 하나씩 요소를 풀어줌
print(a)
print(b)
print(c)
# ('k', 5)
# ('j', 6)
# ('l', 7)

#(2) 리스트의 요소로 튜플인 경우의 예
alist = {(1,2), (3,4) ,(5,6)}
    #for 문과 unpacking 이용하여 튜플의 요소끼리 더한 값을 출력
    #[결과] 1+2=3 , 3+4=7, 5+6=11
for a,b in alist:
    print(a+b)
#3
#7
#11

for a,b in alist:
    print('{}+{}={}'.format(a,b, a+b))

#1+2=3
#3+4=7
#5+6=11

# (3) enumerate() : 인덱스와 같이 추출하고자

'''
    자바에 Iterator의 예쩐 버전 enumerator 비교
'''
user_list = ['개발자', '코더', '전문가', '분석가']

for user in user_list:
    print(user)
    '''
개발자
코더
전문가
분석가
    '''
for user in enumerate(user_list):
    print(user)
    '''
(0, '개발자')
(1, '코더')
(2, '전문가')
(3, '분석가')
    '''
for idx, item in enumerate(user_list):
    print(idx, '번째', item)
'''
0 번째 개발자
1 번째 코더
2 번째 전문가
3 번째 분석가
'''

# (4) zip () : ****************
'''
    a= []
    b= []
    a와 b의 인덱스 값으로 묶음
    print(list(zip(a,b)))
    결과 : [(a[0],b[0]) , (a[1],b[1]) ..........]
'''
days = ['월', '화', '수']
doit = ['잠자기', '공부하기,','놀기', '밥먹기']

print(list(zip(days, doit)))
# [('월', '잠자기'), ('화', '공부하기,'), ('수', '놀기')]

print(dict(zip(days, doit)))
# {'월': '잠자기', '화': '공부하기,', '수': '놀기'}

##3개도 되나 ?
days = ['월', '화', '수']
doit = ['잠자기', '공부하기,','놀기', '밥먹기']
mons = [5,6,7,8]
print(list(zip(days, doit,mons)))
print(dict(zip(days, doit,mons)))