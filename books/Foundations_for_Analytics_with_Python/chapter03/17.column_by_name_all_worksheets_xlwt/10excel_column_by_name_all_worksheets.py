#-*- coding: utf-8 -*-
import sys
# 날짜형태의 값을 원하는 형태로 변환하기 위한 module 추가
from datetime import date
# 엑셀 형태의 파일을 열고, 날짜형태를 튜플 형태로 불러오기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀 파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 읽기 위한 파일을 첫번쨰 인자로 받는다
input_file = sys.argv[1]
# 출력 파일을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일을 엑셀 파일 형태로 쓰기 위한 객체 생성
output_workbook = Workbook()
# 출력파일의 엑셀 파일의 sheet를 select columns_all_worksheets로 설정
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')
# 특정 열의 값만 가져오기 위한 배열
my_columns = ['Customer Name', 'Sale Amount']
# 첫번쨰 sheet인지 확인 하기 위한 flag
first_worksheet = True
# 엑셀 파일 열기
with open_workbook(input_file) as workbook:
    # 쓰기 위한 데이터를 저장하기 위한 배열 첫번째 행을 가져올 값의 목차를 추가한 형태
    data = [my_columns]
    # 원하는 열의 값을 가져오기 위한 index 저장을 위한 배열
    index_of_cols_to_keep = []
    # 엑셀 파일의 sheet를 읽어오기 위한 반복문
    for worksheet in workbook.sheets():
        # 첫번째 시트이면
        if first_worksheet:
            # 첫 줄을 읽어와서 header로 저장
            header = worksheet.row_values(0)
            # 헤더의 열만큼 반복 하기 위한 반복문
            for column_index in range(len(header)):
                # 헤더행에 원하는 값이 있으면
                if header[column_index] in my_columns:
                    # 원하는 값의 인덱스를 저장
                    index_of_cols_to_keep.append(column_index)
            # 첫번째 시트가 아닌 것을 알려주기 위한 flag 바꾸기
            first_worksheet = False
        # 첫줄을 제외한 행을 가져오기 위한 반복문
        for row_index in range(1, worksheet.nrows):
            # 시트 당 데이터를 저장하기 위한 배열
            row_list = []
            # 특정 값이 있는 인덱스에 있는 열의 데이터 가져오기
            for column_index in index_of_cols_to_keep:
                # row_index(행), column_index(열)에 있는 값 가져오기
                cell_value = worksheet.cell_value(row_index, column_index)
                # row_index(행), column_index(열)에 있는 타입 가져오기
                cell_type = worksheet.cell_type(row_index, column_index)
                # 날짜 형태이면
                if cell_type == 3:
                    # 날짜형태의 값을 튜플 형태의 값으로 변환
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 날짜형태의 값을 특정 형태로 변환하기
                    date_cell = date(*date_cell[0:3]).strftime("%d/%m/%y")
                    # row_list에 날짜형태의 값을 추가
                    row_list.append(date_cell)
                # 날짜 형태가 아니면
                else:
                    # row_list에 값을 저장
                    row_list.append(cell_value)
            # 출력 파일을 위한 배열에 row_list추가
            data.append(row_list)
    # 행을 가져오기 위한 반복문
    for list_index, output_list in enumerate(data):
        # 열을 가져오기 위한 반복문
        for element_index, element in enumerate(output_list):
            # 출력할 엑셀 파일에 행과 열에 값 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)