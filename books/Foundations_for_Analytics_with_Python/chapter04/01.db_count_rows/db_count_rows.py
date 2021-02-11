#!/usr/bin/env python3
import sqlite3

# 메모리에 SQLite3의 데이터베이스를 만든다
con = sqlite3.connect(':memory:')
# 4가지 속성을 가지는 sales 테이블을 만든다
query = """CREATE TABLE sales (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
# 명령어 실행
con.execute(query)
# 명령 상태 저장
con.commit()
# 데이터 베이스의 sales 테이블에 저장할 데이터 생성
data = [
    ('Richard Lucas', 'Notepad', 2.50, '2014-01-02'), 
    ('Jenny Kim', 'Binder', 4.15, '2014-01-15'), 
    ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'), 
    ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')
    ]
# 데이터 삽입을 위한 SQL 구문 생성
statement = "INSERT INTO sales VALUES(?,?,?,?)"
# 하나의 데이터가 아닐 경우 사용하는 executemany를 사용하여 대량의 데이터 삽입
con.executemany(statement, data)
# 삽입 상태 저장
con.commit()
# 테이블의 값을 가져오기
cursor = con.execute("SELECT * FROM sales")
# fetchall() 모든 데이타를 한꺼번에 클라이언트로 가져올 때 사용된다
rows = cursor.fetchall()
# 전체 행을 알기 위한 변수
row_count = 0
# 모든 읽어온 값을 반복문
for row in rows:
    # 읽어온 값을 추력
    print(row)
    # 전체 행을 하나 증가
    row_count += 1
# 데이터 베이스 연결 상태 끊기
con.close()
# 전체 행의 수를 출력
print("Number of rows : {}".format(row_count))