#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# 인자를 받기 위한 module 추가
import sys
# 경로를 다루기 위한 module 추가
import os
# 폴더의 경로의 파일을 가져오기 위한 module 추가
import glob
# 날짜형태를 변경하기 위한 module 추가
from datetime import date
# 엑셀 파일의 날짜를 튜플 형태로 가져오고, 엑셀 파일을 읽기 위한 module 추가
from xlrd import xldate_as_tuple, open_workbook
# 엑셀 파일을 쓰기 위한 module 추가
from xlwt import Workbook
# 폴더의 경로를 첫번째 인자로 받는다
input_folder = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력 파일을 엑셀파일로 하기 위한 객체 생성
output_workbook = Workbook()
# 출력 파일에 sheet를 추가
output_worksheet = output_workbook.add_sheet('sums_and_average')
# 모든 데이터를 저장하기 위한 배열
all_data = []
# sales의 index를 변수로 설정
sales_column_index = 3
# 목록을 써주기 위한 배열
header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average', 'workbook_total', 'workbook_average']
# 모든 데이터를 저장할 배열에 목록 배열 추가
all_data.append(header)
# 모든 엑셀 파일 읽기 위한 반복문
for input_file in glob.glob(os.path.join(input_folder, "*.xls*")):
    # 파일 이름을 확인하기 위한 추력
    print("file name : {}".format(os.path.basename(input_file)))
    # 엑셀 파일 열기
    with open_workbook(input_file) as workbook:
        # 통합 문서내의 모든 워크 시트별 총 판매액을 담을 배열
        list_of_total = []
        # 통합 문서의 모든 워크시트별 총 판매 금액을 계산하는데 사용된 판매 금액의 갯수를 담는 배열
        list_of_numbers = []
        # 출력파일에 출력할 모든 리스트를 담는 배열
        workbook_output = []
        # 엑셀 파일의 모든 sheet를 읽기 위한 반복문
        for worksheet in workbook.sheets():
            # 시트 내의 판매액을 구하기 위한 변수 선언 및 초기화
            total_sales = 0
            # 시트 내의 판매액의 갯수를 구하기 위한 변수 선언 및 초기화
            number_of_sales = 0
            # 시트 내의 데이터를 담을 배열 선언
            worksheet_list = []
            # 파일 이름을 worksheet_list에 추가
            worksheet_list.append(os.path.basename(input_file))
            # 시트 이름을 worksheet_list에 추가
            worksheet_list.append(worksheet.name)
            # 시트의 데이터를 읽어오기 위한 반복문
            for row_index in range(1, worksheet.nrows):
                # 오류를 해결 발생시 해결을 위한 try catch문
                try:
                    # 판매액의 값을 float형으로 변화하여 total_sales에 더하기
                    total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',',''))
                    # 판매액의 갯수를 더하기
                    number_of_sales += 1.
                # 오류 발생 시
                except:
                    # 판매액에 0값을 더하기
                    total_sales += 0.
                    # 판매액의 갯수에 0값을 더하기
                    number_of_sales += 0.
            # sheet의 판매액의 평균 값을 구하기
            average_sales = '%.2f' % (total_sales / number_of_sales)
            # 시트 데이터 배열에 전체 판매액 추가
            worksheet_list.append(total_sales)
            # 시트 데이터 배열에 전체 판매액의 평균 값 추가
            worksheet_list.append(float(average_sales))
            # 시트 데이터 배열에 전체 판매액 추가 (엑셀 파일 전체 total을 구하는 배열에 추가?)
            list_of_total.append(total_sales)
            # 시트 데이터 배열에 전체 판매액 추가 (엑셀 파일 전체 total을 구하는 배열에 추가?)
            list_of_numbers.append(float(number_of_sales))
            # 출력을 할 배열에 worksheet_list추가
            workbook_output.append(worksheet_list)
        # 엑셀 파일의 전체 판매액의 합
        workbook_total = sum(list_of_total)
        # 엑셀 파일의 전체 판매액의 평균
        workbook_average = sum(list_of_total)/sum(list_of_numbers)
        # 출력파일에 출력할 모든 리스트를 담는 배열
        for list_element in workbook_output:
            # list_element에 workbook_total 요소 추가
            list_element.append(workbook_total)
            # list_element에 workbook_average 요소 추가
            list_element.append(workbook_average)
        # all_data에 extend - 리스트에 같은 배열로 추가(확장)
        # append를 쓸 경우 3차원의 배열이 되므로 2차원 배열을 유지해야한다?
        all_data.extend(workbook_output)
# 출력파일의 쓸 데이터를 튜플 형태로 읽어오기 위한 반복문
for list_index, output_list in enumerate(all_data):
    # 출력파일의 쓸 데이터를 튜플 형태로 읽어오기 위한 반복문
    for element_index, element in enumerate(output_list):
        # 출력파일의 행과 열에 값을 쓰기
        output_worksheet.write(list_index, element_index, element)
# 파일 저장
output_workbook.save(output_file)