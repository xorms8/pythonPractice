import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

#1 웹 문서 가져오기

html = urlopen("https://www.seoul.go.kr/seoul/autonomy.do")
soup = BeautifulSoup(html, 'html.parser') #html 파싱

#2 웹 문서에서 추출한 데이터를 리스트에 저장

구청이름 = []
구청주소 = []
구청전화 = []
구청홈페이지 = []

구청이름 = soup.select('.tabcont strong')
구청주소 = soup.select('.tabcont li:nth-of-type(1)')
구청전화 = soup.select('.tabcont li:nth-of-type(2)')
구청홈페이지 = soup.select('.tabcont li:nth-of-type(3)')

for i,s,f,j in zip(구청이름,구청주소,구청전화,구청홈페이지):
    print('구청이름 :',i.text)
    print('구청주소 :',s.text )
    print('구청전화 :',f.text)
    print('구청홈페이지:',j.text)
    print('='*50)

#3. 리스트에 있는 내용을 아래처럼 출력

'''
    [예시]
    구청이름 : 강동구
    구청주소 : 
    구청전화 :
    구청홈페이지 :http~~~ 
    
'''