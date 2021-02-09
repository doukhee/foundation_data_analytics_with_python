#-*- coding: utf-8 -*-
import pandas as pd
import sys
# 입력파일을 첫번쨰 인자로 받는다
input_file = sys.argv[1]
# 출력파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 데이터를 읽어오기 
# read_excel(input_file, sheet_name=, index_col=)
# 입력된 파일을 엑셀 형태로 읽어온다.
# sheet_name=은 읽어올 sheet 이름
# index_col=은 인덱스로 사용할 컬럼명을 써준다
data_frame = pd.read_excel(input_file, sheet_name='january_2013',index_col=None)
# 특정한 날짜 조건을 찾기 위한 배열
import_dates = ['01/24/2013','01/31/2013']
# 조건이 읽어온 데이터에 있는지 확인 하기
# isin(list)은 list에 있는 값이 있을 경우만 가져오는 함수
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(import_dates)]
# 파일 쓰기
# datetime_format=은 원하는 형태로 날짜 데이터를 보여주기 위한 설정이다.
writer = pd.ExcelWriter(output_file, datetime_format='dd/mm/yyyy')
# 원하는 값만 거른 것을 엑셀 파일에 쓰기 시트의 이름은 jan_13_output으로 설정 인덱스를 사용하지 않는 것으로 섯ㄹ정
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
# 파일 저장
writer.save()

