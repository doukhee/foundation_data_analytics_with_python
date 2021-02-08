#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 쓰기 위한 datetime module 추가
from datetime import date
# 엑셀파일을 읽기 위한 xlrd module 추가
from xlrd import open_workbook, xldate_as_tuple
# 엑셀 형태로 쓰기 위한 xlwt module 추가
from xlwt import Workbook
# 입력파일의 이름 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일명 두번째 인자로 받기
output_file = sys.argv[2]
# Workbook객체를 생성하여 변수를 output_workbook으로 정의한다
output_workbook = Workbook()
# 생성한 객체의 sheet를 추가한다
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 판매액의 컬럼 위치를 정의하기 위한 변수
sale_amount_column_index = 3
# 입력파일을 열기
with open_workbook(input_file) as workbook:
    # 작업할 시트를 이름으로 열어서 정의
    worksheet = workbook.sheet_by_name('january_2013')
    # 데이터를 받을 배열 선언
    data = []
    # 시트의 첫열을 값을 가졍괴
    header = worksheet.row_values(0)
    # 데이터 배열에 추가
    data.append(header)
    # 1부터 열의 끝까지 반복
    for row_index in range(1, worksheet.nrows):
        # 열의 값을 저장하기 위한 배열
        row_list = []
        # 판매액을 가져오기
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
        # 판매액이 1400.0보다 크면
        if sale_amount > 1400.0:
            # 행의 갯수만큼 반복
            for column_index in range(worksheet.ncols):
                # 열과 행의 위치에 있는 값 저장
                cell_value = worksheet.cell_value(row_index, column_index)
                # 열과 행의 위치에 있는 값의 형태 구하기 
                cell_type = worksheet.cell_type(row_index, column_index)
                # 값의 형태가 날짜형이면
                if cell_type == 3:
                    # 날짜형태를 튜블 형태로 변환
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 튜플형태로 변환한 값을 특정 날짜 포맷으로 변경
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    # 열 배열에 추가
                    row_list.append(date_cell)
                # 날짜형태가 아니면
                else:
                    # 열 배열에 추가
                    row_list.append(cell_value)
        # 열배열이 존재하면
        if row_list:
            # 데이터 배열에 열 데이터 배열 추가
            data.append(row_list)
    # 인덱스(list_index)와 값(output_list)을 가지고 data의 길이 만큼 반복 
    for list_index, output_list in enumerate(data):
        # 인덱스(element_index)와 값(element)을 가지고 data의 길이 만큼 반복
        for element_index, element in enumerate(output_list):
            # 출력할 시트에 열(list_index) 행(element_index)에 값(element) 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장하기
output_workbook.save(output_file)
