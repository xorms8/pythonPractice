
import datetime
today = datetime.date.today();
print('today is ', today)

#년 / 월 / 일 추출

print('연도', today.year)
print('월', today.month)
print('일', today.day)

print(today.year , "년" ,  today.month ,"월" , today.day,"일")

from datetime import timedelta
print("어제 날짜:" ,today +timedelta(days=-1))
#일주일전 날짜
print("일주일전 날짜:" ,today +timedelta(days=-7))
#열흘 후 날짜
print("열흘 후 날짜:" ,today +timedelta(days=+10))

#[참고] 한달 후
from dateutil.relativedelta import relativedelta

print("한달 후 날짜:" , today+ relativedelta(months = 1))

'''
1- 날짜형을 문자열로 변환
2- 문자열늘 날짜 형식으로 변환
'''

from datetime import date
today = date.today()
print(today.strftime('%Y/%m/%d'))
print(today.strftime('%Y %m %d'))


# 날짜 형식으로 변환하여 년/월/일을 추추

naljja = '2020-08-10 12:55:30' # 문자열
date_naljja = datetime.datetime.strptime(naljja,'%Y-%m-%d %H:%M:%S')
print(date_naljja)