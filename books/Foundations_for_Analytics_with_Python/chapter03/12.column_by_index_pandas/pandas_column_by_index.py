#-*- coding: utf-8 -*-
import pandas as pd
import sys

# 입력파일을 첫번쨰 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 입력파일의 january_2013 sheet를 index 설정 없이 읽어온다
data_frame = pd.read_excel(input_file, sheet_name="january_2013", index_col=None)
# 1열과 4열의 데이터를 복사하여 저장한다
data_frame_column_by_index = data_frame.iloc[ :, [1, 4]]
# 엑셀파일 형태로 데이터 쓰기 날짜형태는 일/월/년으로 저장한다는 설정
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 데이터를 엑셀파일 형태로 쓰기
data_frame_column_by_index.to_excel(writer, sheet_name="jan_13_output", index=False)
# 파일 저장
writer.save()