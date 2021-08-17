alist = ["A","B","C"]
blist = ["ㄱ","ㄴ","ㄷ"]
result = []

for a, b in enumerate(zip(alist, blist)):
    print(a,b)
    try:
        result.append(b[a])
    except IndexError:
        result.append("Error")

print(result)
'''
답 : ['A', 'ㄴ', 'Error']

해석 :

for a,b의 enumerate(zip,alist,blist)) 는
append 말고 그냥 print(a,b) 라면 인덱스 순서대로
0 ('A', 'ㄱ')
1 ('B', 'ㄴ')
2 ('C', 'ㄷ')
이렇게 출력될 것이다.
try: 구문에 append로 (b[a])는
(0[0]) (1[1]) (2[2])로 증가 된 값이 들어갈 것이다.
즉, 0 ('A', 'ㄱ') 의 0[0] = 'A'
1 ('B', 'ㄴ') 의 1[1] = 'ㄴ'
2 ('C', 'ㄷ') 의 2[2] = none 없으므로 'Error' 가 들어갑니다.

'''

#==================================
print("문제 2번")
def sum_data( data_a, data_b ):
    for i in data_a:
        print("i값 :",i)
        for j in data_b:
            print("j값 :",j)
            result = i + j
        return result

a=[1,2]
b=[3,4]
print(sum_data(a,b))

#==================================
print("문제 3번")

class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for i in self.numberList:
            result += i
        return result

    def avg(self):
        avg = self.sum()
        return print(avg / len(self.numberList))


cal = Calculator([1,2,3,4,5])
print(cal.sum())
cal.avg()


#==================================
# print("문제 4번")
'''
국어점수를 입력->80
영어점수를 입력->88
수학점수를 입력->77
총점 -> xxxx
평균 -> xxxx
'''
# number1 = int(input("국어점수를 입력-> "))
# number2 = int(input("영어점수를 입력-> "))
# number3 = int(input("수학점수를 입력-> "))
#
# sum = number1+number2+number3
# avg = sum / 3
#
# print('총점 ->',sum)
# print('평균 ->',avg)


#==================================
print("문제 5번")
    # [실행결과]
    # 문자열을 입력 : I love coffee and study java and python
    # 금지어를 입력 : java C linux
    # 결과 : I love coffee and study **** and python

str = input("문자열을 입력 :",)
cuss = input("금지어를 입력 :",)
cuss = cuss.split()
for i in cuss:
    while str.count(i):
        str = str.replace(i, '*' * len(i))

print("결과 : {}".format(str))


#==============================
print("문제 6번")
'''
학생들의 성적이 score.txt 파일에 저장되어 있다.
이 성적을 읽어서 평균값을 구하고 다시 파일의 끝에 추가로 저장한다. (20점)

    [ score.txt ]  ==========>    [ score.txt ]
    99.1                                    99.1
    88.2                                    88.2
    77.3                                    77.3
    66.4                                    66.4
                                            평균값 : xxx.xx
                            
'''

# f = open("./data/score.txt", 'r',encoding='utf-8')
# score = f.readlines()
# score = list(map(float, score))
# sum = 0
# average = 0
# for i in score: #합계
#     sum = sum + i
#     average = sum / len(score)
#
# f2 = open("./data/score.txt", 'a',encoding='utf-8')
# f2.write("\n평균값: {:.2f}".format(average))
#
# f.close()
