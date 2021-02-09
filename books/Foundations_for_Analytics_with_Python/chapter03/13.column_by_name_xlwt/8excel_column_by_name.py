#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 변경하기 위한 module 추가
from datetime import date
# 엑셀 파일을 읽기 위한 module 추가
from xlrd import sheet, xldate_as_tuple, open_workbook
# 엑셀파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일을 엑셀 파일로 쓰기 위한 객체 생성
output_workbook = Workbook()
# 출력파일의 sheet 추가
output_sheet = output_workbook.add_sheet('jan_2013_output')
# 원하는 열을 선택하기 위한 배열
my_columns = ["Customer ID", 'Purchase Date']
# 입력파일을 열기
with open_workbook(input_file) as workbook:
    # 읽어올 sheet 가져오기
    worksheet = workbook.sheet_by_name('january_2013')
    # sheet의 순서를 이용해서 읽을 sheet 가져오기
    # worksheet = workbook.sheet_by_index(0)
    # 첫줄에 header를 추가하기 위한 배열 삽입 및 데이터 저장을 위한 배열 생성
    data = [my_columns]
    # 첫줄 가져오기
    header_list = worksheet.row_values(0)
    # 열 헤더의 인덱스 값을 저장하기 위한 배열
    header_index_list = []
    # 한줄의 행에 있는 열의 갯수 만큼 반복
    for header_index in range(len(header_list)):
        # 만약 첫줄에 원하는 값이 있을 경우
        if header_list[header_index] in my_columns:
            # 원하는 값의 인덱스를 열 헤더의 인덱스 저장을 위한 배열에 추가
            header_index_list.append(header_index)
    # 엑셀 파일을 읽어오기 위한 반복
    for row_index in range(1, worksheet.nrows):
        # 읽어온 값을 저장하기 위한 배열
        row_list = []
        # 원하는 값이 위치한 값이 열에 있을 경우
        for column_index in header_index_list:
            # 요소의 값을 읽어오기
            cell_value = worksheet.cell_value(row_index, column_index)
            # 요소의 타입을 가져오기
            cell_type = worksheet.cell_type(row_index, column_index)
            # 요소의 값이 날짜 형태이면
            if cell_type == 3:
                # 요소의 값을 엑셀의 날짜 형태로 변환
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                # 요소의 값을 날짜 형태 설정
                date_cell = date(*date_cell[0:3]).strftime("%d/%m/%y")
                # row_list에 추가
                row_list.append(date_cell)
            # 날짜 형태가 아니면
            else:
                # row_list에 추가
                row_list.append(cell_value)
        # 데이터 배열에 row_list 추가
        data.append(row_list)
    # 튜플 형태의 값을 읽어오기 위한 반복
    for list_index, output_list in enumerate(data):
        # 튜플 형태의 값을 읽어오기 위한 반복
        for element_index, element in enumerate(output_list):
            # 출력할 엑셀 파일에 행과 열에 요소 값 쓰기
            output_sheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)
