#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 변환하기 위한 module 추가
from datetime import date
# 엑셀파일을 열고, 날짜 형태를 튜플 형태로 가져오기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받기
output_file = sys.argv[2]
# 출력파일을 엑셀파이롤 만들기 위한 변수 선언
output_workbook = Workbook()
# 출력파일에 jan_2013_output이라는 sheet 추가
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 특정열을 거르기 위한 배열 선언
my_columns = [1, 4]
# 입력파일을 엑셀형태로 열기
with open_workbook(input_file) as workbook:
    # 입력파일의 january_2013 sheet열기
    worksheet = workbook.sheet_by_name('january_2013')
    # 데이터를 저장할 변수 선언
    data = []
    # 읽어온 파일의 행만큼 반복
    for row_index in range(worksheet.nrows):
        # 행 데이터를 담기 위한 배열
        row_list = []
        # 거르기 위한 열일 경우 만큼 반복
        for column_index in my_columns:
            # 행과 열의 요소에 있는 값 가져오기
            cell_value = worksheet.cell_value(row_index, column_index)
            # 행과 열의 요소에 있는 타입 가졍괴
            cell_type = worksheet.cell_type(row_index, column_index)
            # 날짜형태이면
            if cell_type == 3:
                # 날짜를 튜플 형태로 가졍괴
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                # 날짜형태를 원하는 형태로 변환
                date_cell = date(*date_cell[0:3]).strftime("%d/%m/%Y")
                # row_list에 추가
                row_list.append(date_cell)
            # 날짜 데이터가 아니면
            else:
                # row_list에 값 추가
                row_list.append(cell_value)
        # 데이터 배열에 추가
        data.append(row_list)
    # 튜플 형태를 계속해서 index, value형태로 가져오기 위한 반복
    for list_index, output_list in enumerate(data):
        # 행에 저장된 튜플 형태의 값을 가져오기 위한 반복
        for element_index, element in enumerate(output_list):
            # 출력파일에 행과 열에 값 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)
