#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# database name : my_suppliers_python
# User : python_data
# Password: won1228A!
import csv
# mysql 데이터 베이스를 쓰기 위한 모듈
import MySQLdb
import sys
# 날짜 형태를 변환 하기 위한 module 추가
from datetime import date, datetime
# 입력파일을 첫번쨰 인자로 받는다
input_file = sys.argv[1]
# 데이터 베이스 접속을 위한 객체 생성 및 연결
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers_python', user='python_data', passwd='won1228A!')
# 데이터베이스 접속 후 CRUD를 위한 객체 생성
connection = con.cursor()
# 입력 파일을 읽어오기
file_reader = csv.reader(open(input_file, mode='r'), delimiter=',')
# 첫줄을 읽어오기
header = next(file_reader)
# 파일을 읽어오기 위한 반복문
for row in file_reader:
    # 한줄 데이터 저장을 위한 배열 선언
    data = []
    # 데이터를 읽어오기
    for column_index in range(len(header)):
        # 4번쨰 데이터 안에 있을 경우
        if column_index < 4:
            # 숫자형태로 데이터 변경
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            # %Y: year is 2016; %y: year is 15
            a_date = datetime.date(datetime.strptime(str(row[column_index]), "%m/%d/%y"))
            # 날짜 형태로 데이터 변경
            a_date = a_date.strftime("%Y-%m-%d")
            # 데이터 추가
            data.append(a_date)
    # 한줄 데이터 만들기
    print(data)
    # 데이터베이스에 데이터 삽인
    connection.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
# 데이터 상태 저장
con.commit()
# 한줄 띄기
print("")
# 데이터 읽어오기
connection.execute("SELECT * FROM Suppliers")

# 읽어온 모든 데이터 가져오기
rows = connection.fetchall()
# 데이터 출력을 위한 반복문
for row in rows:
    # 데이터 출력을 위한 배열
    row_list_output = []
    # 데이터 요소의 값 가져오기
    for column_index in range(len(row)):
        # 데이터 출력을 위한 배열에 추가
        row_list_output.append(str(row[column_index]))
    # 데이터 출력
    print(row_list_output)
