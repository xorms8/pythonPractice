"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    print('1-',p)
    savepath = "./" + p.netloc + p.path
    print('2-', savepath)

    if re.search('/$', savepath): # /$ : /로 끝나는
        savepath += "index.html"
        print('3-', savepath)

    #로컬폴더에 savepath 파일이 존재하는지 확인
    if os.path.exists(savepath): return savepath

    #다운 받을 폴더 생성
    savedir = os.path.dirname(savepath)

    if not os.path.exists(savedir): # 이 디렉토리 명이 존재하니 -> 존재하면 if문에 안걸림
        os.makedirs(savedir) #존재하지 않으면 디렉토리 생성

    #다운 받기
    try:
        request.urlretrieve(url, savepath) # 파일 다운 rqeust.urlretrieve
        time.sleep(2) #시간 간격
    except:
        print('다운로드 실패 :', url)
        return None




if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



