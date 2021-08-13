
from pathlib import Path

p = Path('logtemp')
if p.mkdir(exist_ok=True) == False: #폴더를 만들건데 그 값이 False면 만들고~
    p.mkdir()

import os
import random

f = os.path.exists('logtemp/temp_log.txt') #파일이 존재 하는지 여부를 변수로 저장
f2 = Path('logtemp/temp_log.txt') #파일 생성 Path
f3 = open(f2,'a',encoding='utf-8') #파일 오픈

newtime = os.path.getctime(Path.cwd()) #os를 이용한 newtime 변수값 받아오기

if f == False: #파일이 없으면~
    f2.touch()  # 파일 생성!

f3.write('%f\n'%(newtime+random.random())) #그리고 선언한 f3 파일오픈에 write-> newtime +random 값