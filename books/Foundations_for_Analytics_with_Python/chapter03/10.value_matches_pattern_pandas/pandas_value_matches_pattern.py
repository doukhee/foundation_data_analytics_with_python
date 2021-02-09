#-*- coding: utf-8 -*-
import pandas as pd
import sys
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 입력파일의 sheet 이름이 january_2013을 인덱스 설정 없이 읽어온다
data_frame = pd.read_excel(input_file, sheet_name="january_2013", index_col=None)
# 고객 이름이 J로 시작하는 값을 읽어서 data_frame_value_matches_pattern으로 저장한다
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]
# 엑셀파일 형태로 쓰기 위한 설정 날짜 형태를 일/달/년도로 설정한다
writer = pd.ExcelWriter(output_file, datetime_format='dd/mm/yyyy')
# 엑셀파일의 jan_13_output의 시트에 쓴다
data_frame_value_matches_pattern.to_excel(writer, sheet_name="jan_13_output", index=False)
# 파일 저장
writer.save()
