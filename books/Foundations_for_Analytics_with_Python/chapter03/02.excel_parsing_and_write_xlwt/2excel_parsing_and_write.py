#-*- coding: utf-8 -*-
import sys
from xlrd import open_workbook
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# Workbook객체를 생성하여 변수를 output_workbook으로 정의 한다.
output_workbook = Workbook()
# add_sheet() 시트 추가하는 함수
# sheet를 jan_2013_output 이름으로 정의하고, sheet를 output_worksheet로 변수 선언
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 엑셀 파일을 열기
with open_workbook(input_file) as workbook:
    # 연 엑셀파일의 january_2013의 sheet를 연다 그리고, 변수를 worksheet로 선언
    worksheet = workbook.sheet_by_name('january_2013')
    # 열의 갯수 만큼 반복
    for row_index in range(worksheet.nrows):
        # 행의 갯수만큼 반복
        for column_index in range(worksheet.ncols):
            #worksheet.cell_value(row_index, column_index): sheet의 값의 열(row_index)과 행(column_index)의 위치의 값을 읽어온다
            # 출력파일의 열의 위치와 행의 위치에 맞게 값 쓰기
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
# 파일 저장
output_workbook.save(output_file)