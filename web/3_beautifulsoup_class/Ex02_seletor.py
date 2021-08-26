"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - CSS 선택자 검색할 때 : select() /  select_one()
    id = # class .
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""

# html 파싱
soup = BeautifulSoup(html, 'html.parser')

# (1) id 값으로 선택
course =soup.select_one('#course h1') # course 의 h1 자손 1개만 찾을시 _one
print(course.text)

# (2) class 값으로 선택

subs = soup.select(('ul.subs li'))

for i in subs:
    print(i.text)
