#-*- coding: utf-8 -*-
import sys
# 정규표현식을 위한 module 추가
import re
# 날짜 형태를 변형하기 위한 module 추가
from datetime import date
# 엑셀 파일을 읽어오기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀 파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일을 첫번쨰 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일을 엑셀형태로 저장하기 위한 객체 선언
output_workbook = Workbook()
# 출력파일에 sheet의 이름을 jan_2013_output으로 추가한다
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 대문자J로 시작하는 값을 찾기 위한 정규 표현식
pattern = re.compile(r'(?P<my_pattern>^J.*)')
# 고개이름이 위치하는 열에 대한 정보를 알려주기 위한 변수 선언
customer_name_column_index = 1
# 엑셀 형태의 파일을 열기
with open_workbook(input_file) as workbook:
    # 연 엑셀파일에 특정 sheet를 이름으로 가져오기
    worksheet = workbook.sheet_by_name('january_2013')
    # 데이터를 저장하기 위한 배열 선언
    data = []
    # 첫행의 값을 가져오기
    header = worksheet.row_values(0)
    # 첫행의 값을 저장
    data.append(header)
    # 첫행을 제외하고 읽어오기 위한 반복문
    for row_index in range(1, worksheet.nrows):
        # 행의 데이터를 저장하기 위한 배열
        row_list = []
        # 정규표현식에 맞는 값이 고객명에 있을 경우
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
            # 행의 값만큼 반복
            for column_index in range(worksheet.ncols):
                # row_index와 column_index 위치에 있는 요소에 있는 값 읽어오기
                cell_value = worksheet.cell_value(row_index, column_index)
                # row_index와 column_index 위치에 있는 요소의 타입 읽어오기
                cell_type = worksheet.cell_type(row_index, column_index)
                # 날짜형태이면
                if cell_type == 3:
                    # 튜플형태로 데이터 변환 날짜형태 변환을 위한 
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 날짜형태를 특정한 형태로 변환
                    date_cell = date(*date_cell[0:3]).strftime("%m/%d/%Y")
                    # 날짜 형태의 값을 행 데이터에 추가?
                    row_list.append(date_cell)
                # 날짜 형태가 아니면
                else:
                    # row_list에 추가
                    row_list.append(cell_value)
        # row_list가 비어 있지 않는다면
        if row_list:
            # data 배열에 row_list 추가
            data.append(row_list)
    # 튜플 형태의 값을 index와 값을 읽어오기 위한 반복문
    for list_index, output_list in enumerate(data):
        # 튜플 형태의 값을 index와 값을 읽어오기 위한 반복문
        for element_index, element in enumerate(output_list):
            # 출력 엑셀 파일에 list_index, element_index에 값을 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)

