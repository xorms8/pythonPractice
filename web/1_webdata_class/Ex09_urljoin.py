"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
from urllib import parse

baseUrl = "http://www.example.com/html/a.html"

#함수나 디렉토리 연결
print(parse.urljoin(baseUrl, 'b.html'))
print(parse.urljoin(baseUrl, 'sub/c.html')) #http://www.example.com/html/sub/c.html
print(parse.urljoin(baseUrl, '/sub/d.html')) #http://www.example.com/sub/d.html
print(parse.urljoin(baseUrl, '../sub/e.html')) #http://www.example.com/sub/e.html
print(parse.urljoin(baseUrl, '../temp/f.html')) #http://www.example.com/temp/f.html

print(parse.urljoin(baseUrl, 'http://www.daum.net'))