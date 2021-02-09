#-*- coding: utf-8 -*-
import sys
import pandas as pd
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 입력파일의 january_2013 sheet를 인덱스 설정 없이 읽어온다
data_frame = pd.read_excel(input_file, sheet_name="january_2013", index_col=None)
# 원하는 값을 찾아서 저장을 한다 
# loc[] = 문자열을 이용해서 찾는 경우
# iloc[] = 인덱스를 이용해서 찾을 경우
data_frame_column_by_name = data_frame.loc[:, ["Customer ID", "Purchase Date"]]
# 파일쓰기 위한 객체 생성
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 찾은 데이터를 출력파일에 jan_13_output이라는 sheet로 쓴다
data_frame_column_by_name.to_excel(writer, sheet_name="jan_13_output", index=False)
# 파일 저장
writer.save()