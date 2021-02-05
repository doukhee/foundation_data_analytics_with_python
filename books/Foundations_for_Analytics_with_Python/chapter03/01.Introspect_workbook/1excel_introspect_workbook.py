#-*- coding: utf-8 -*-
import sys
# 현재 1.2.0버전에서만 가능하다. 새로운 모듈인 openpyxl을 사용하는 것을 권한다.
from xlrd import open_workbook
# 입력파일의 경로를 첫번째 인자로 받는다.
input_file = sys.argv[1]
# 파일 열기
workbook = open_workbook(input_file)
# 파일 안에 있는 시트 수 가져오기
print("Number of worksheets:", workbook.nsheets)
# 시트마다의 행과 열의 수를 가져오고, 시트의 이름을 가져온다.
for worksheet in workbook.sheets():
    # 확인을 위한 출력
    print("Worksheet name: ", worksheet.name, '\tRows:', worksheet.nrows, "\tColumns:", worksheet.ncols)