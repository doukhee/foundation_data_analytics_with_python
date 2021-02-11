#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pandas as pd
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 전체 sheet의 데이터를 읽어오기
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
# 특정 열에 위치한 값을 저장하기 위한 배열
column_output = []
# 시트의 이름과 데이터를 읽어오기위한 반복문
for worksheet_name, data in data_frame.items():
    # sheet의 이름 출력 
    print("sheet name : {}".format(worksheet_name))
    # 특정 열의 데이터를 찾아서 가져온 후 column_output에 저장
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
# 가져온 값을 위 아래로 합치기
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
# 엑셀 파일을 쓰기 위한 설정
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 합쳐진 값을 엑셀의 selected_columns_all_sheets의 sheet로 만들기
selected_columns.to_excel(writer, sheet_name="selected_columns_all_sheets", index=False)
# 파일 저장
writer.save()
