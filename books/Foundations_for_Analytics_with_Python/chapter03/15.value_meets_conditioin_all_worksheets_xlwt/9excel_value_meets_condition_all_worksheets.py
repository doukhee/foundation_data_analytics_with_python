#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 원하는 포멧으로 출력하기 위한 module 추가
from datetime import date
# 엑셀 파일의 날짜형 데이터를 튜플 형태로 가져오기, 엑셀 파일 열기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀 파일 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일의 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일을 엑셀 파일로 쓰기 위한 객체 생성
output_workbook = Workbook()
# 출력 파일에 sheet를 추가 
output_worksheet = output_workbook.add_sheet('filter_rows_all_worksheets')
# 판매액의 위치를 알려주기 위한 변순
sales_column_index = 3
# 2000.0 이상 판매된 값을 읽어오기 위한 조건
threshold = 2000.0
# 첫번쨰 시트인지 인지 알기 위한 불형 변수
first_worksheet = True
# 입력파일 읽기 모드로 열기
with open_workbook(input_file) as workbook:
    # 데이터 저장을 위한 배열 선언
    data = []
    # 모든 시트를 읽기 위한 시트의 수만큼 반복 (workbook.sheets()= 엑셀의 모든 시트 객체를 가져온다)
    for worksheet in workbook.sheets():
        # 첫번째 시트이면ㄴ
        if first_worksheet:
            # 첫줄 읽어오기
            header_row = worksheet.row_values(0)
            # 첫줄의 값을 데이터 배열에 저장
            data.append(header_row)
            # 첫번째 시트가 아닌 것을 알려주기 위한 값 변경
            first_worksheet = False
        # 시트의 첫 행 빼고 읽어오기 위한 반복
        for row_index in range(1, worksheet.nrows):
            # 한 줄을 저장하기 위한 변수 썬언
            row_list = []
            # 판매액을 가져오기
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            # 만약 판매액이 원하는 값보다 클 경우
            if sale_amount > threshold:
                # 열의 요소 만큼 반복
                for column_index in range(worksheet.ncols):
                    # 행과 열의 값을 읽어오기
                    cell_value = worksheet.cell_value(row_index, column_index)
                    # 행과 열의 타입을 가져오기
                    cell_type = worksheet.cell_type(row_index, column_index)
                    # 날짜 형태이면
                    if cell_type == 3:
                        # 튜플 형태의 날짜 값을 변경
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        # 날짜 형태를 원하는 형태로 변환 (처음 부터 3번째 위치까지의 값을 가지고 변환한다)
                        date_cell = date(*date_cell[0:3]).strftime("%d/%m/%y")
                        # 변환한 값을 row_list에 추가
                        row_list.append(date_cell)
                    else:
                        # 행과 열의 값을 row_list에 추가
                        row_list.append(cell_value)
            # row_list가 비어 있지 않으면
            if row_list:
                # data 배열에 row_list 추가
                data.append(row_list)
    # 이중 배열 형태를 index와 value로 가져오기 위한 반복문
    for list_index, output_list in enumerate(data):
        # 배열 형태의 값을 index와 value로 가져오기 위한 반복문
        for element_index, element in enumerate(output_list):
            # 출력 엑셀 파일에 list_index(행)와 element_index(열)의 위치에 값을 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)