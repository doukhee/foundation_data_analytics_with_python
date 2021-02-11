#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 경로를 가져오기 위한 module 추가
import glob
# 경로를 간단히 하기 위한 module 추가
import os
# 인자를 받아서 처리 하기 위한 module 추가
import sys
# 날짜형태의 값을 다루기 위한 module 추가
from datetime import date
# 엑셀의 날짜형태 및 파일 열기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력 폴더의 경로를 첫번째 인자로 받는다
input_folder = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 엑셀 파일을 만들기 위한 객체 선안
output_workbook = Workbook()
# 엑셀 파일의 sheet를 all_data_all_workbooks로 설정
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')
# 데이터를 저장하기 위한 배열
data = []
# 첫번째 시트인지 확인하기 위한 flag
first_worksheet = True
# 폴더 안에 있는 모든 엑셀 파일 열기
for input_file in glob.glob(os.path.join(input_folder, "*.xls*")):
    # 엑셀 파일 명을 출력
    print(os.path.basename(input_file))
    # 엑셀 파일 열기
    with open_workbook(input_file) as workbook:
        # 엑셀 파일의 모든 sheet의 데이터를 가져오기 위한 반복문
        for worksheet in workbook.sheets():
            # 첫번째 시트이면
            if first_worksheet:
                # 첫줄 읽어오기
                header_row = worksheet.row_values(0)
                # 목차를 데이터 배열에 추가
                data.append(header_row)
                # 이제부터 첫번째 시트가 아닌 것을 알려주기 위해서 flag 변경
                first_worksheet = False
            # 시트의 행만큼 데이터를 읽어오기 위한 반복문
            for row_index in range(1, worksheet.nrows):
                # 행 데이터를 저장하기 위한 배열
                row_list = []
                # 시트의 열 데이터를 읽어오기 위한 반복문
                for column_index in range(worksheet.ncols):
                    # 행과 열에 있는 값 읽어오기
                    cell_value = worksheet.cell_value(row_index, column_index)
                    # 행과 열에 있는 데이터 타입 읽어오기
                    cell_type = worksheet.cell_type(row_index, column_index)
                    # 날짜형태의 데이터면
                    if cell_type == 3:
                        # 날짜형 데이터를 튜플 형태로 변경
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        # 튜플 형태로 변경한 데이터를 원하는 형태의 날짜 형태로 변경
                        date_cell = date(*date_cell[0:3]).strftime("%d/%m/%y")
                        # 행 데이터 배열에 추가
                        row_list.append(date_cell)
                    # 날짜형태의 데이터가 아니면
                    else:
                        # 행 데이터 배열에 추가
                        row_list.append(cell_value)
                # 행 데이터가 존재하면
                if row_list:
                    # 데이터 배열에 추가
                    data.append(row_list)
# 행과 값을 읽어오기 위한 튜플 형태의 반복문
for list_index, output_list in enumerate(data):
    # 열과 값을 읽어오기 위한 튜플 형태의 반복문
    for element_index, element in enumerate(output_list):
        # 출력 엑셀의 시트에 행과 열의 위치에 데이터 쓰기
        output_worksheet.write(list_index, element_index, element)
# 출력 파일 저장
output_workbook.save(output_file)
