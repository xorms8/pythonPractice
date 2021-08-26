import cx_Oracle as oci

# 1) 연결(Connection) 얻어오기

conn = oci.connect("hr/1234@localhost:1521/xe")

print(conn.version)
# 2) 커서 객체 얻어오기

cursor = conn.cursor() #자바로 생각하면 전송객체

# 3) SQL문장

sql = "SELECT * FROM MEMBER"

# 4) SQL문장 실행

cursor.execute(sql) #실행하고싶습니다.
# datas = cursor.fetchall()
#print(datas)
# for row in datas:
#     print(row)
#     print(row[0], row[1])

# ->밑에 위에 같은 코딩

for rs in cursor:
    print(rs)
    print(rs[0], rs[1])



# 5) 커서 객체 닫기

cursor.close()


# 6) 연결 객체 닫기

conn.close()