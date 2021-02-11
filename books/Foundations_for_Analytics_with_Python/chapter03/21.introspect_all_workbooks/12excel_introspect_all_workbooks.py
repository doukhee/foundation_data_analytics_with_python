#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 경로를 가져오기 위한 module 추가
import glob
# 파일이름만 가져오기 위한 module 추가
import os
# 폴더 경로를 입력 받기 위한 module 추가
import sys
# 엑셀 파일을 열기 위한 module 추가
from xlrd import open_workbook
# 폴더의 경로를 첫번쨰 인자로 받는ㄷ
input_directory = sys.argv[1]
# 전체 엑셀 파일의 숫자를 세기 위한 변수
workbook_counter = 0
# 입력된 폴더의 경오레 특정 패턴이 맞는 파일 이 있을경우 그 파일을 열기 위한 반복문
for input_file in glob.glob(os.path.join(input_directory, "*.xls*")):
    # 엑셀 파일 열기
    workbook = open_workbook(input_file)
    # 엑셀 파일의 이름을 출력한다
    print("workbook : {}".format(os.path.basename(input_file)))
    # 엑셀 파일의 sheet수를 출력한다
    print("Number of worksheets : {}".format(workbook.nsheets))#
    # 엑셀파일의 시트의 수만큼 반복
    for worksheet in workbook.sheets():
        # sheet의 이름과, sheet의 행과 열을 출력
        print("Worksheet name : ", worksheet.name, "\tRows: ", worksheet.nrows, "\tColumns: ", worksheet.ncols)
    # 파일 하나를 다읽고 파일의 숫자를 하나 증가
    workbook_counter += 1
# 총 엑셀파일의 수를 출력
print("Number of excel workbooks: {}".format(workbook_counter))