#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# 데이터 베이스 접속을 위한 module 추가
import sqlite3
# csv 파일을 다루기 위한 module 추가
import csv
import sys
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 데이터베이스를 만들고 접속하는 객체를 가져온다
con = sqlite3.connect("./database.db")
# sql구문을 쓰기 위한 객체 생성
c = con.cursor()
# table을 생성하는 query
create_table = """CREATE TABLE IF NOT EXISTS Suppliers 
                (
                    Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE
                );"""
# query실행
c.execute(create_table)
# 상태 저장
con.commit()
# 엑셀 파일을 읽기 모드로 읽어오기
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# 한줄을 읽어오고 한 줄의 값을 None값으로 변환한다
header = next(file_reader, None)
# 행을 읽어오기 위한 반복문
for row in file_reader:
    # 데이터 저장을 위한 배열
    data = []
    # 열의 값을 읽어오기 위한 반복문
    for column_index in range(len(header)):
        # 행에 있는 값을 data 배열에 추가
        data.append(row[column_index])
    # 확인을 위한 출력
    print(data)
    # 데이터 삽입
    c.execute("INSERT INTO Suppliers VALUES (?,?,?,?,?);", data)
# 상태 저장
con.commit()
# 확인을 위한 한줄 출력
print('')
# 데이터 베이스에 저장된 값 읽어오기
output = c.execute("SELECT * FROM Suppliers")
# 읽어온 모든 데이터 모두 읽어오기
rows = output.fetchall()

# 읽어온 데이터를 출력하기 위한 반복문
for row in rows:
    # 출력 값을 저장하기 위한 배열
    output = []
    # 읽어온 값의 요소의 값을 가져오기 위한 반복문
    for column_index in range(len(row)):
        # 배열의 요소로 값을 읽어서 output 배열에 추가
        output.append(str(row[column_index]))
    # 확인을 위한 출력
    print(output)