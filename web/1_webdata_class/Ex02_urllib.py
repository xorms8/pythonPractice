#*********** urllib.request (s가 없음)

from urllib import request
from urllib.error import URLError, HTTPError
#0. 웹 연결
try:
    url = "http://www.google.com"
    site = request.urlopen(url)
except HTTPError as e:
    print('HTTP error')
except URLError as u:
    print('URL ERROR')
else :
    # 1. 웹 문서 읽기
    page = site.read()
    print(page)
    print('-' * 50)

#2. 웹에 상태 학인
print(site.status)
print('-' * 50)

#3. 헤더정보 출력 (dict, 키밸류)
header = site.getheaders()
print(header)
