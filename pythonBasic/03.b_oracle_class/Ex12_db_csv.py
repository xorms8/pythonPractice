import csv

import cx_Oracle as oci

# 테이블 생성 함수

def createDBTable():
    # 1) Connection 객체 얻어오기
    conn = oci.connect("hr/1234@localhost:1521/xe")
    # 2) Cursor 객체 얻어오기
    cursor = conn.cursor()  # 자바로 생각하면 전송객체
    # 3) SQL 문장 만들기
    sql = '''
        CREATE TABLE supply (
            id  number  not null,
            Supplier_Name   varchar2(50)    not null,
            Invoice_Number  varchar2(50)    not null,
            Part_Number     varchar2(50)    not null,
            Cost            number          not null,
            Purchase_Date   DATE DEFAULT SYSDATE,
            primary key(id)
            )
    '''
    sql_seq = 'CREATE SEQUENCE seq_supply_id'
    # 4) SQL 문장 실행하기
    cursor.execute(sql)  # 실행하고싶습니다.
    cursor.execute(sql_seq)
    # 5) Cursor 닫기
    cursor.close()
    # 6) Connetion 닫기
    conn.close()

#레코드 입력 함수
def insertDB(row):
    # 1) Connection 객체 얻어오기
    conn = oci.connect("hr/1234@localhost:1521/xe")
    # 2) Cursor 객체 얻어오기
    cursor = conn.cursor()  # 자바로 생각하면 전송객체
    # 3) SQL 문장 만들기
    sql ='''
        INSERT INTO supply(id, Supplier_Name, Invoice_Number, Part_Number, Cost, Purchase_Date)
        VALUES(seq_supply_id.nextval,:0, :1, :2, :3, :4)
    '''
    # 4) SQL 문장 실행하기
    cursor.execute(sql,row) #?????row를 여기에다 지정
    conn.commit() ##중요 커밋 꼭 해줘야함
    # 5) Cursor 닫기
    cursor.close()
    # 6) Connetion 닫기
    conn.close()

# 해당 테이블의 레코드 검색
def viewTable(table_name):
    # 1) Connection 객체 얻어오기
    conn = oci.connect("hr/1234@localhost:1521/xe")
    # 2) Cursor 객체 얻어오기
    cursor = conn.cursor()  # 자바로 생각하면 전송객체
    # 3) SQL 문장 만들기
    sql = 'SELECT * FROM {}'.format(table_name)
    # 4) SQL 문장 실행하기
    cursor.execute(sql)
    for rs in cursor:
        print(rs)
    # 5) Cursor 닫기
    cursor.close()
    # 6) Connetion 닫기
    conn.close()

def deleteTable(table_name):
    # 1) Connection 객체 얻어오기
    conn = oci.connect("hr/1234@localhost:1521/xe")
    # 2) Cursor 객체 얻어오기
    cursor = conn.cursor()  # 자바로 생각하면 전송객체
    # 3) SQL 문장 만들기
    sql = 'DROP TABLE {}'.format(table_name)
    # 4) SQL 문장 실행하기
    cursor.execute(sql)
    # 5) Cursor 닫기
    cursor.close()
    # 6) Connetion 닫기
    conn.close()


if __name__ == '__main__':
    # 1.테이블 생성
    #createDBTable()

    #2.csv 파일에서 일기
    file_name = '../files/supply.csv'
    f = open(file_name,'rt', encoding='utf-8')
    datas=csv.reader(f, delimiter=',')
    #print(datas)
    header =next(datas, None)
    print('제목줄 : ',header)
    print('-'*50)

    for row in datas:
        print(row)
        #insertDB(row)

    # 3. 해당 테이블을 검색
    print("해당 테이블을 검색 ==")
    viewTable('supply') #테이블 레코드 보는 함수 호출하고 supply 테이블을 볼거야!

    # 4. 해당 테이블 삭제
    print("해당 테이블을 삭제 ==")
    #deleteTable('supply')
