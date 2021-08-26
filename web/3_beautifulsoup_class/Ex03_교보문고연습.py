'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서

#화면에 있는 도서의 제목
# 총 xxx권이 보입니다

html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")

soup = BeautifulSoup(html, 'html.parser') #html 파싱
book = soup.select('.detail .title strong')
for i in book:
    print(i.text.strip())

print('총 {}권이 보입니다'.format(len(book)))


'''
[2] imgs 폴더를 생성하고 그 폴더안에 이미지를 다운받기
    각각의 이미지 이름은 책 제목
    디렉토리 생성 : mkdir() / makedirs()
'''
import os
from urllib import request
os.makedirs('imgs', exist_ok=True) #기존에 폴더가 있어도 잘 만들어짐

imgUrls = soup.select('.image .cover img')
print(len(imgUrls))

for i in imgUrls:
    imgsrc = i.attrs['src']
    imgtitle =i.attrs['alt'].strip().replace('/', '-')
    request.urlretrieve(imgsrc, 'imgs/' + imgtitle + '.jpg')
