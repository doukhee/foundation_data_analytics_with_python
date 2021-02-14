#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import csv
import sqlite3
import sys
# 입력 파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# ../../database/db/database.db에 접속을 한다
#con = sqlite3.connect("../../database/db/database.db")
# 메모리에 있는 데이터 베이스를 접속한다
con = sqlite3.connect(":memory:")
# 테이블 생성을 위한 쿼리 생성
query = """CREATE TABLE IF NOT EXISTS Sales
            (
                customer VARCHAR(20),
                product VARCHAR(40),
                amount FLOAT,
                date DATE
            );"""
# 쿼리 실행
con.execute(query)
# 상태 저장
con.commit()
# 입력 데이터 넣기
data = [
    ('Richard Locas', 'Notepad', 2.50, '2014-01-02'),
    ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
    ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
    ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')
]
# 데이터를 출력하기 위한 반복문
for tuple in data:
    # 데이터 출력
    print(tuple)
# 데이터 삽일을 위한 쿼리
statement = "INSERT INTO Sales VALUES(?,?,?,?)"
# 많은 데이터를 삽입 하기 위한 쿼리 실행
con.executemany(statement, data)
# 상태 저장
con.commit()
# csv파일을 읽어오기 위한 파일 리더 설정
file_reader = csv.reader(open(input_file, mode='r'), delimiter=',')
# 첫줄 읽어서 None으로 설정
header = next(file_reader, None)
# 한줄 띄기 위한 출력
print("")
# csv파일에서 데이터 양을 가져오기 위한 반복문
for row in file_reader:
    # 데이터를 담을 배열
    data = []
    # 값을 접근하기 위한 반복문
    for column_index in range(len(header)):
        # 데이터 배열에 값을 추가
        data.append(row[column_index])
    # 입력된 값을 출력
    print(data)
    # 메모리 데이터베이스에 있는 입력된 값으로 변경
    con.execute("UPDATE Sales SET amount=?,date=? WHERE customer=?;", data)
# 상태저장
con.commit()
# 결과 값을 저장 하기 위한 변수
cursor = con.execute("SELECT * FROM Sales")
# 테이블의 값을 읽어오기 위한 실행
rows = cursor.fetchall()
# 결과 값을 가져오기 위한 반복문
for row in rows:
    # 결과 값을 출력을 위한 변수
    output = []
    # 원하는 요소의 값의 출력을 위한 반복문
    for column_index in range(len(row)):
        # 결과 값을 추가
        output.append(str(row[column_index]))
    # 결과 값 한줄 출력
    print(output)
