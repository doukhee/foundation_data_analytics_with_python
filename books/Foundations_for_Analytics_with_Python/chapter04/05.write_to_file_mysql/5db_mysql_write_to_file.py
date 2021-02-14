#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# database name : my_suppliers_python
# User : python_data
# Password: won1228A!
import csv
# mysql을 다루기 위한 module 추가
import MySQLdb
import sys
# 출력파일을 첫번째 인자로 받는다
output_file = sys.argv[1]
# mysql database에 접속하기 위한 객체 생성 및 설정
con = MySQLdb.connect(host='localhost', port=3306, user='python_data', passwd='won1228A!', db='my_suppliers_python')
# 데이터 베이스에 쿼리를 날리기 위한 객체 생성
connection = con.cursor()
# 파일을 쓰기 위한 객체 생성
filewriter = csv.writer(open(output_file, mode='w', newline=''), delimiter=',')
# 목록을 쓰기 위한 배열 선언
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
# 파일에 목록 쓰기
filewriter.writerow(header)
# 데이터 베이스에 특정 조건의 값을 가져오기 위한 쿼리
connection.execute("""SELECT * FROM Suppliers WHERE Cost > 700.0;""")
# 쿼리 실행 후 모든 값을 가져오기
rows = connection.fetchall()
# 출력파일에 쓰기 위한 반복문
for row in rows:
    # 파일에 읽어온 값 쓰기
    filewriter.writerow(row)