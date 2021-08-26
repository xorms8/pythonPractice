"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path

#p = Path('C:\Windows')
p = Path('..')
print(p)
print(p.resolve()) #얘가 aBasic 까지

test = []
for x in p.iterdir():
    if x.is_dir():
        test.append(x)
print(test)

# (1) 해당 경로와 하위 목록들 확인
test = [x for x in p.iterdir() if x.is_dir()]
print(test)

p2 = Path('..')
print(p2.resolve())#얘가 aBasic 까지
j = p2.glob('a_datatype_class/*.py')
print(list(j))