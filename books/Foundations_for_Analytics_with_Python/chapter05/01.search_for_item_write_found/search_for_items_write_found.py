#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv
# 폴더 경로를 가져오기 위한 module 추가
import glob
# 폴더 경로를 가져오기 위한 module 추가
import os
import sys
# 날짜 형태를 변경하기 위한 module 추가
from datetime import date
# 엑셀 파일을 읽고, 날짜형태를 변환하기 위한  module 추가
from xlrd import xldate_as_tuple, open_workbook
# 선택할 품목 번호가 있는 파일을 첫번째 인자로 받는다
item_numbers_file = sys.argv[1]
# 검색할 폴더의 목록을 두번째 인자로 받는다
path_to_folder = sys.argv[2]
# 출력파일명을 세번째 인자로 받는다
output_file = sys.argv[3]
# 선택할 품목을 저장할 빈 배열
item_numbers_to_find = []
# 선택할 품목이 있는 파일을 열기
with open(item_numbers_file, mode='r', newline='') as item_numbers_csv_file:
    # 파일을 읽어오기
    filereader = csv.reader(item_numbers_csv_file, delimiter=',')
    # 파일에 써있는 데이터의 행 만큼 반복
    for row in filereader:
        # 첫번째 위치한 값을 선탁할 품목을 저장할 배열에 추가
        item_numbers_to_find.append(row[0])
# 선택할 품목 번호 배열 출력
print(item_numbers_to_find)
# 출력 파일을 쓰기 위한 추가 모드로 쓰기 위한 객체 생성
filewriter = csv.writer(open(output_file, mode='a',newline=''), delimiter=',')
# 파일 갯수를 확인하기 위한 변수
file_counter = 0
# 행의 갯수를 파악하기 위한 변수
line_counter = 0
# 아이템의 수를 파악하기 위한 변수
count_of_item_numbers = 0
# 폴더 안에 있는 파일만큼 반복
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
    # 파일 갯수 하나 추가
    file_counter += 1
    # 파일의 확장자를 확인하기 위한 출력
    print("file name : {}".format(os.path.basename(input_file).split(".")[1]))
    # csv파일일 경우
    if os.path.basename(input_file).split(".")[1] == 'csv':
        # 파일을 읽기 모드로 열기
        with open(input_file, mode='r', newline='') as csv_in_file:
            # csv파일을 읽어오기 구분자는 쉼표로 설정
            filereader = csv.reader(csv_in_file, delimiter=',')
            # 첫줄 읽어오기
            header = next(filereader)
            # 첫줄 다음부터 파일이 끝날때까지 행의 데이터 읽어오기
            for row in filereader:
                # 출력할 행 데이터 저장할 빈 배열
                row_of_output = []
                # 첫줄의 열의 갯수 만큼 반복
                for column in range(len(header)):
                    # 열이 3 이하이면
                    if column < 3:
                        # 데이터를 가져와 String타입으로 변환 및 공백 제거
                        cell_value = str(row[column]).strip()
                        # 출력할 행 데이터 저장
                        row_of_output.append(cell_value)
                    # 열이 3이면
                    elif column == 3:
                        # $를 제거 및 쉼표를 제거 후 판매액 값을 String 타입으로 변환
                        cell_value = str(row[column]).lstrip("$").replace(',','').split('.')[0].strip()
                        # 출력할 데이터 배열에 저장
                        row_of_output.append(cell_value)
                # 출력할 배열에 파일 이름 저장
                row_of_output.append(os.path.basename(input_file))
                # 첫열의 값이 선택할 품목 배열에 있으면
                if row[0] in item_numbers_to_find:
                    # 출력파일에 데이터 쓰기
                    filewriter.writerow(row_of_output)
                    # 아이템 수 하나 올리기
                    count_of_item_numbers += 1
                # 읽은 행의 수 하나 증가
                line_counter += 1
    # 만약 파일의 확장자가 xls이나 xlsx일 경우
    elif os.path.basename(input_file).split(".")[1] == 'xls' or os.path.basename(input_file).split(".")[1] == 'xlsx':
        # 엑셀 파일의 시트 열기
        workbook = open_workbook(input_file)
        # 시트의 수만큼 반복하기 위한 반복문
        for worksheet in workbook.sheets():
            # 예외 처리를 위한 구문
            try:
                # 첫줄 읽어오기
                header = worksheet.row_values(0)
            # 인덱스 에러일 경우
            except IndexError:
                # 통과
                pass
            # 첫줄을 제외하고, 행의 끝까지 실행하기 위한 반복문
            for row in range(1, worksheet.nrows):
                # 데이터를 저장할 빈배열
                row_of_output = []
                # 첫 줄의 열만큼 반복 하기위한 반복문
                for column in range(len(header)):
                    # 열의 수가 3이하이면
                    if column < 3:
                        # 행과 열에 맞는 값을 읽어와서 String 타입으로 변환
                        cell_value = str(worksheet.cell_value(row, column)).strip()
                        # 데이터를 저장할 배열에 추가
                        row_of_output.append(cell_value)
                    # 열의 수가 3이면
                    elif column == 3:
                        # 판매액을 구해서 String 타입으로 저장
                        cell_value = str(worksheet.cell_value(row, column)).split('.')[0].strip()
                        # 데이터를 저장할 배열에 저장
                        row_of_output.append(cell_value)
                    else:
                        # 엑셀 타입의 날짜 형태를 읽어오기
                        cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                        # 날짜형태를 변경하여 저장
                        cell_value = str(date(*cell_value[0:3])).strip()
                        # 데이터를 저장할 배열에 저장
                        row_of_output.append(cell_value)
                # 데이터를 저장할 배열에 파일이름 저장
                row_of_output.append(os.path.basename(input_file))
                # 데이터를 저장할 배열에 시트의 이름을 저장
                row_of_output.append(worksheet.name)
                # 만약 선택할 품목이 있을 경우
                if str(worksheet.cell(row, 0).value).split(".")[0].strip() in item_numbers_to_find:
                    # 출력파일에 쓰기
                    filewriter.writerow(row_of_output)
                    # 아이템 수 하나 증가
                    count_of_item_numbers += 1
                # 읽은 행의 수 하나 증가
                line_counter += 1
# 읽은 파일 수를 학인하기 위한 출력
print("Number of files : {}".format(file_counter))
# 읽은 행의 수를 확인하기 위한 출력
print("Number of lines: {}".format(line_counter))
# 선택할 품목이 잇는 갯수를 확인하기 위한 출력
print("Number of item numbers: {}".format(count_of_item_numbers))
