#-*- coding: utf-8 -*-
import sys
# 날짜 형태를 이용하기 위한 module 추가
from datetime import date
# 엑셀 파일을 읽기 위한 module 추가
from xlrd import open_workbook, xldate_as_tuple
# 엑셀 파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 입력파일을 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받기
output_file = sys.argv[2]
# 출력파일을 엑셀형태로 만들기 위한 객체 생성
output_workbook = Workbook()
# 출력파일에 sheet를 추가
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 특정 날짜 조건을 거르기 위한 조건
important_dates = ['01/24/2013', '01/31/2013']
# 날짜 값을 가지고 있는 행의 위치를 선언
purchase_date_column_index = 4
# 입력 엑셀 파일 열기
with open_workbook(input_file) as workbook:
    # 읽을 시트를 시트 이름으로 열기
    worksheet = workbook.sheet_by_name('january_2013')
    # 데이터 저장을 위한 배열 선언
    data = []
    # 첫 줄 읽기
    header = worksheet.row_values(0)
    # 첫줄을 data 배열에 추가
    data.append(header)
    # 다음 줄부터 계속해서 읽어오기 위한 반복문
    for row_index in range(1, worksheet.nrows):
        # 구매 날짜를 조건의 형태로 변환하기 위한 값 가져오기
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index), workbook.datemode)
        # 날짜 형태로 변환 하기 
        purchase_datetime = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
        # 열의 값을 저장하기 위한 배열 선언
        row_list = []
        # 만약 구맴 날짜가 조건에 있을 경우
        if purchase_datetime in important_dates:
            # 값을 저장하기 위한 행의 갯수만큼 반복
            for column_index in range(worksheet.ncols):
                # 행과 열에 있는 데이터 가져오기
                cell_value = worksheet.cell_value(row_index, column_index)
                # 행과 열에 있는 데이터의 타입 가져오기
                cell_type = worksheet.cell_type(row_index, column_index)
                # 날짜 형태이면 
                if cell_type == 3:
                    #날짜 형태 변환을 위한 값 가져오기
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 날짜 형태를 원하는 형태로 변환
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    # 날짜를 열 데이터 추가
                    row_list.append(date_cell)
                else:
                    # 날짜 데이터가 아닌 값 추가
                    row_list.append(cell_value)
        # 열 데이터 배열에 값이 존재하면
        if row_list:
            # 데이터 배열에 추가
            data.append((row_list))
    # 튜플 형태의 값을 읽어오기 위한 반복문 
    for list_index, output_list in enumerate(data):
        # 튜플 형태의 값을 읽어오기 위한 반복문
        for element_index, element in enumerate(output_list):
            # 값을 쓰기
            output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)