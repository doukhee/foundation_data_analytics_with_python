#-*- coding: utf-8 -*-
import pandas as pd
import sys
# 입력 파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 입력한 파일의 전체 시트를 인덱스 없이 읽어오기
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
# 조건에 맞는 데이터를 저장하기 위한 배열 선언
row_output = []
# 데이터의 값을 모두 읽어오기 위한 반복문
# DataFrame 열을 반복하여 열 이름과 내용이있는 튜플을 Series로 반환합니다.
for worksheet_name, data in data_frame.items():
    # Sale Amount의 값을 float형으로 변환하여 조건을 검색해서 저장을 한다
    row_output.append(data[data['Sale Amount'].replace('$','').replace(',','').astype(float) > 2000.0])
# 걸러진 데이터를 위아래로 합치기 인덱스는 설정하지 않는다
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
# 엑셀 파일로 만들기
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 데이터를 엑셀 파일의 sale_amount_gt2000이라는 sheet로 생성
filtered_rows.to_excel(writer, index=False, sheet_name="sale_amount_gt2000")
# 파일 저장
writer.save()