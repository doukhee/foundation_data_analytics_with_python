#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import pandas as pd
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받는다
output_file = sys.argv[2]
# 특정 시트만 가져오기 위한 인덱스 배열
my_sheets = [0,1]
# 특정 값만 가져오기 위한 조건 변순
threshold = 1900.0
# 특정 시트만 읽어서 데이터 가져오기
data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)
# 특정 값만 저장할 배열
row_list = []
# 읽어온 파일의 sheet를 읽어오기
for worksheet_name, data in data_frame.items():
    # 특정 조건에 만족하는 값만 row_list에 추가
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
# 특정 조건을 만족하는 배열을 위 아래로 합치기
filter_rows = pd.concat(row_list, axis=0, ignore_index=True)
# 엑셀형태로 저장하기 위한 객체 생성
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 엑셀 파일로 쓰기
filter_rows.to_excel(writer, sheet_name="set_of_worksheets", index=False)
# 파일 저장
writer.save()
