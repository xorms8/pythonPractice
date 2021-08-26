from urllib.request import urlopen
from bs4 import BeautifulSoup

#아이템과 가격을 추출

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser') #html 파싱

item = []
price = []
item = soup.select('.gift td:nth-of-type(1)')
price = soup.select('.gift td:nth-of-type(3)')
for i,j in zip(item,price):
    print('아이템 : ',i.text)
    print('가격 : ',j.text)
    print('='*50)