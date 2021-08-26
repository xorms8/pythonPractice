"""
    HTML 내부에 있는 링크를 추출하는 함수
        - CSS 파일과 a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

def enum_links(html,base):
    #-------------------------------------

    soup = BeautifulSoup(html ,'html.parser')
    links = soup.select('a')



    result = []

    for i in links:
        href = i.attrs['href']
        # print(i, ':', href)
        url = parse.urljoin(base, href)  # base + 상대경로
        result.append(url)

    return result

if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'  #base
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url) #response -> html
    print(result)

