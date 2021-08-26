#myfile.py

#(1) 모듈전체를 참조할 때
# import mymodule
#
# print('오늘의 날씨 ' ,mymodule.get_weather())
# print('오늘의 요일 ' ,mymodule.get_date())


#(2) 별칭 부여
# import mymodule as my
#
# print('오늘의 날씨 ' ,my.get_weather())
# print('오늘의 요일 ' ,my.get_date())



#(3) 모듈에서 필요한 부분만 임포트하기
from c_module_class.mypackage.exam.mymodule import get_weather

print('오늘의 날씨 ' ,get_weather())
#print('오늘의 요일 ' ,my.get_date())

from c_module_class.mypackage.exam.mymodule import get_weather as gw
print('오늘의 날씨' ,gw())

