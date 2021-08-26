"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
'''
try:
    f = open('./data/data.txt' ,'r',encoding='utf-8')
except FileExistsError as e:
    print("파일을 찾을 수 없습니다.",e)
else:
    while True:
        line =f.readline()
        if not line: break #더이상 line이 없으면 -> if not line
        print(line, end='') #원래 개행인데 print가 한번더 개생해서 end로 개행을 없앰
    f.close()
finally:
    print('종료')
'''

# try:
#     with open('./data/data.txt' ,'r',encoding='utf-8') as f : #with을 쓰는이유 -> close를 안해도 됨
#         while True:
#             line = f.readline()
#             if not line: break  # 더이상 line이 없으면 -> if not line
#             print(line, end='')  # 원래 개행인데 print가 한번더 개생해서 end로 개행을 없앰
# except FileExistsError as e:
#     print("파일을 찾을 수 없습니다.", e)
# print('종료')


try:
    with open('./data/data.txt' ,'r',encoding='utf-8') as f : #with을 쓰는이유 -> close를 안해도 됨
        contents= f.read()
        word = contents.split() #단어별로 자르는 split
        num = len(word)
        print(contents, word, num)
except FileExistsError as e:
    print("파일을 찾을 수 없습니다.", e)
else :
    print('파일명: {}, 총 단어수 :{}'.format(f.name, num))
print('종료')