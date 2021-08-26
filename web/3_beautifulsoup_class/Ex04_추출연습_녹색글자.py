from urllib.request import urlopen
from bs4 import BeautifulSoup

#녹색 글자만 추출하여 출력

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, 'html.parser') #html 파싱
green = soup.select('.green')

for i in green:
    print(i.text)