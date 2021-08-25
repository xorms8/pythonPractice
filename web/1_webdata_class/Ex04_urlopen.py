
# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""
from urllib import request
url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
imgName = 'data/google.png'
#1.웹 페이지 열고 읽기
site = request.urlopen(url)
content = site.read()

#2. 파일에 저장
with open('google.png', "wb") as f: # wb (write, binary(이미지저장!!))
    f.write(content)