#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 쓰기 위한 datetime module 추가
from datetime import date
# 엑셀파일을 읽기 위한 xlrd module 추가
from xlrd  import open_workbook, xldate_as_tuple
# 엑셀 형태로 쓰기 위한 xlwt module 추가
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# Workbok객체를 생성하여 변수를 output_workbook으로 정의한다.
output_workbook = Workbook()
# 생성한 객체에 sheet를 추가한다.
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 입력된 파일명을 엑셀형태로 연다
with open_workbook(input_file) as workbook:
    # 열은 엑셀파일의 시트의 january_2013를 연다
    worksheet = workbook.sheet_by_name('january_2013')
    # 연 파일의 열 수 만큼 반복
    for row_index in range(worksheet.nrows):
        # 열의 값을 저장하기 위한 배열
        row_list_output = []
        # 연 파일의 행 수 만큼 반복
        for col_index in range(worksheet.ncols):
            # cell_type(row_index, col_index): 열(row_index)과 행(col_index)의 위치에 있는 값의 타입 값을 반환 한다
            # 타입 값은 0이면 - empty, 1이면 TEXT 타입, 2이면 NUMBER 타입, 3이면 DATE 타입, 4이면 BOOLEAN, 5이면 ERROR, 6이면 BLANK이다.
            # 열과 행의 위치에 있는 값이 날짜형태이면
            if worksheet.cell_type(row_index, col_index) == 3:
                # xldate_as_tuple(value, type) 함수는 value 값을 type형태의 값을 튜블로 변환한다
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                # 날짜 형태의 특정 포맷으로 변경한다
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%y')
                # 특정 열을 저장하기 위한 배열에 날짜형태의 값을 추가한다
                row_list_output.append(date_cell)
                # 만들 파일의 열과 행에 날짜형태의 값을 입력한다.
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                # 날짜형태의 데이터가 아닐 경우 읽은 값을 non_date_cell 변수로 설정한다.
                non_date_cell = worksheet.cell_value(row_index, col_index)
                # 열 데이터의 배열에 추가한다.
                row_list_output.append(non_date_cell)
                # 만들 파일의 열과 행에 날짜형태가 아닌 값을 입력한다
                output_worksheet.write(row_index, col_index, non_date_cell)
# 파일읠 저장한다
output_workbook.save(output_file)