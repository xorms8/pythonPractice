"""
    파이썬에서 웹을 요청할 수 있는 라이브러리
        1- requests 라이브러리 (s붙음 주의) - 추가
        2- urllib 라이브러리 - 내장모듈

    차이점
        1- requests는 요청 메소드(get/post)를 구분하지만 urllib는 보내는 데이타 여부에 따라 구분됨
        2- 데이타 보낼 때 requests는 딕셔러니 형태로 urllib는 인코딩한 바이너리 형태로 보낸다
        
    requests 라이브러리 추가
    메뉴 > File > Settings > Project Interpreter > + 버튼 > 'requests' 검색 후 인스톨

[ requests 모듈 ]
(1) Rest API 지원
    import requests
    resp = requests.get('http://www.mywebsite.com/user')
    resp = requests.post('http://www.mywebsite.com/user')
    resp = requests.put('http://www.mywebsite.com/user/put')
    resp = requests.delete('http://www.mywebsite.com/user/delete')

(2) 파라미터가 딕셔너리 인수로 가능
    data = {'firstname':'John', 'lastname':'Kim', 'job':'baksu'}
    resp = requests.post('http://www.mywebsite.com/user', data=userdata)

(3) json 디코더 내장 (따로 json 모듈 사용 안해도 됨)
    resp.json()
"""

import requests

url = "http://www.google.com"

res = requests.get(url)

print(res.text)
print('-'*50)
print(res.content) # b'문자열'

'''
b '문자열' : byte 바이트 객체
'''
print ('+' * 50)
print(res.headers)
print ('+' * 50)

for i in res.headers:
    print(i, ':' , res.headers[i])

print('=' * 50)

for i in res.headers.items():
    print(i) #튜플 형식으로 나옴

print('=' * 50)

for i in res.headers.items():
    print(i[0], ':', i[1]) #튜플 형식으로 나옴