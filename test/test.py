
f = open("./data/test.txt", 'r',encoding='utf-8')
score = f.readlines()
score = list(map(int, score))
sum = 0
average = 0
for i in score: #합계
    sum = sum + i
    average = sum / len(score)

print("전체 합은 {} 입니다.".format(sum))
print("전체 평균은 %d 입니다."%average)

f.close()

#result.txt파일 만든 후 결과값 넣기

f = open("./data/result.txt", 'w',encoding='utf-8')
f.write("전체 합은 {} 입니다.".format(sum))
f.write("전체 평균은 %d 입니다."%average)
f.close()
