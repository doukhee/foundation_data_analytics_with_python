#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
# 날짜 형태의 값을 변경학 위한 module 추가
from datetime import date
# 엑셀 파일을 읽고, 날짜형태를 튜플 형태로 가져오기 위한 module 추가
from xlrd import open_workbook, xldate_as_tuple
# 엑세파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일을 엑셀형태로 하기 위한 객체 생성
output_workbook = Workbook()
# 출력 엑셀파일의 sheet의 이름을 set_of_worksheets로 추가
output_worksheet = output_workbook.add_sheet("set_of_worksheets")
# 읽어온 엑셀파일의 특정 sheet를 읽어오기 위한 index 배열
my_sheets = [0,1]
# 특정 조건을 위한 변수 선언
threshold = 1900.0
# 판매 액의 위치를 알려주기 위한 변수 선언
sales_column_index = 3
# 첫번째 sheet를 알려주기 위한 flag
first_sheet = True
# 입력 엑셀파일 열기
with open_workbook(input_file) as workbook:
    # 데이터 저장을 위한 배열
    data = []
    # 시트이 수만큼 반복하는 반복문
    for sheet_index in range(workbook.nsheets):
        # 만약 sheet의 index 값이 가져올 특정 sheet의 index와 같으면
        if sheet_index in my_sheets:
            # index로 시트 객체를 가져오기
            worksheet = workbook.sheet_by_index(sheet_index)
            # 첫번쨰 시트이면
            if first_sheet:
                # 첫줄을 읽어오기
                header_row = worksheet.row_values(0)
                # data 배열에 첫줄 추가
                data.append(header_row)
                # 첫번쨰 시트 flag 변경
                first_sheet = False
            # 파일의 첫줄을 제외한 행만큼 반복
            for row_index in range(1, worksheet.nrows):
                # 파일의 행 데이터를 저장하기 위한 배열
                row_list = []
                # 판매액을 가져오기
                sale_amount = worksheet.cell_value(row_index, sales_column_index)
                # 판매액이 특정 값보다 높으면
                if sale_amount > threshold:
                    # 행에 있는 열만큼 반복
                    for column_index in range(worksheet.ncols):
                        # 행과 열에 있는 값 읽어오기
                        cell_value = worksheet.cell_value(row_index, column_index)
                        # 행과 열에 있는 타입을 가져오기
                        cell_type = worksheet.cell_type(row_index, column_index)
                        # 행과 열에 있는 타입이 날짜 형태이면
                        if cell_type == 3:
                            # 날짜형태를 튜플 형태로 변경
                            date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                            # 날짜형태를 나타나는 포맷을 변경
                            date_cell = date(*date_cell[0:3]).strftime("%d/%m/%y")
                            # row_list에 추가
                            row_list.append(date_cell)
                        # 날짜 형태가 아니면
                        else:
                            # row_list에 추가
                            row_list.append(cell_value)
                # row_list가 비어있지 않으면
                if row_list:
                    # data 배열에 row_list 추가
                    data.append(row_list)
    # 행과 열을 가져오기 위한 튜플 형태의 반복문
    for list_index, output_list in enumerate(data):
        # 열과 값을 가져오기 위한 튜플 형태의 반복문
        for element_index, element in enumerate(output_list):
            # 출력파일의 시트에 값을 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)
