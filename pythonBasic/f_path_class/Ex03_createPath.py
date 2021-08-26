from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())

p1 = Path('Ex03_createPath.py')
print(p1.stat())
# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p1 = Path('Ex03_createPath.py')
tm = p1.stat().st_ctime
print(tm)
from datetime import datetime
z = datetime.fromtimestamp(tm)
print(z)
# ------------------------------------------------
# 3. 디렉토리 생성
# p = Path('imsi2')
# p.mkdir(exist_ok=True) #없으면 만들어
#
# p2 = Path('temp/test/imsi3')
# p2.mkdir(parents=True) # /안먹히는걸 가능하게

# ------------------------------------------------
# 4. 파일 생성
f = Path('imsi/3.text')
f.write_text('홍길동 안녕', encoding='utf-8')

#f.rename('imsi/zzzzz.txt')
f.replace('imsi/aaaaa.txt')

f2 =Path('imsi/2.txt')
f2.touch()

# ------------------------------------------------
#  5. 경로 제거

# f = Path('imsi/2.txt')
# f.unlink()
#
# f = Path('imsi2')
# f.rmdir() #폴더가 비어있지 않으면 안지워짐

import shutil
shutil.rmtree('imsi')