"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'

response = req.urlopen(url) # html을 받아옴

soup = BeautifulSoup(response, 'html.parser') #html 파싱

subs = soup.select_one(('.head_info .value'))
print('미국 USD : ', subs.text)

