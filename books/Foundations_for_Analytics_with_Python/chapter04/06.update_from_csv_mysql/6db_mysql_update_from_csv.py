#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# database name : my_suppliers_python
# User : python_data
# Password: won1228A!
import csv
# mysql database를 다루기 위한 module 추가
import MySQLdb
import sys
# 읽어올 파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# mysql database에 접속을 위한 객체 설정 및 연결 후 객체 저장
con = MySQLdb.connect(host='localhost', port=3306, user='python_data',passwd='won1228A!', db='my_suppliers_python')
# 쿼리를 사용하기 위한 객체 생성
connection = con.cursor()
# csv 파일을 읽어오익
file_reader = csv.reader(open(input_file, mode='r', newline=''), delimiter=',')
# 첫 줄을 읽어온 후 값을 없애기
header = next(file_reader, None)
# 파일을 읽어오기 위한 반복문
for row in file_reader:
    # 데이터 출력을 위한 빈 배열 선언
    data = []
    # 데이터를 읽어오기 위한 반복문
    for column_index in range(len(header)):
        # 데이터의 빈 값 제거 및 추가
        data.append(str(row[column_index]).strip())
    # 데이터 확인을 위한 출력
    print(data)
    # 데이터 베이스에 있는 데이터 변경
    connection.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
# 데이터 베이스 상태 저장
con.commit()
# 구분을 위한 한줄 띄기
print("")
# 데이터 베이스에 저장된 값 읽어오기 위한 쿼리
connection.execute("SELECT * FROM Suppliers")
# 읽어온 데이터 출력
rows = connection.fetchall()
# 데이터 베이스에서 읽어온 값 반복해서 읽어오기
for row in rows:
    # 데이터 출력을 위한 빈 배열
    output = []
    # 값을 읽어오기
    for column_index in range(len(row)):
        # 데이터 출력을 위한 추가
        output.append(str(row[column_index]))
    # 확인을 위한 출력
    print(output)