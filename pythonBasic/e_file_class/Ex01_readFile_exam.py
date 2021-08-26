""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
def count_words(filename):
    try:
        with open('./data/{}'.format(filename), 'r', encoding='utf-8') as f:  # with을 쓰는이유 -> close를 안해도 됨
            contents = f.read()
            word = contents.split()  # 단어별로 자르는 split
            num = len(word)
    except FileNotFoundError:
            pass
    else:
         print('파일명: {}, 총 단어수 :{}'.format(f.name, num))



# 존재하지 않는 파일명도 있음
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)

print('종료')