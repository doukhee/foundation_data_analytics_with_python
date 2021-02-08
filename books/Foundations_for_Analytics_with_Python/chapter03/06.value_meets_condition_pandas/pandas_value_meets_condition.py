#-*- coding: utf-8 -*-
import sys
import pandas as pd

# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 엑셀 시트의 january_2013시트를 읽어오기
data_frame = pd.read_excel(input_file, sheet_name='january_2013', index_col=None)
# 읽어온 데이터에서 Sale Amount의 값이 float형이면서 1400.0 이상인 값을 저장
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
# 엑셀형태의 값을 쓰기 위한 객체 생성
writer = pd.ExcelWriter(output_file)
# 데이터 형태를 엑셀형태로 변환하여 쓰기 시트 이름을 jan_13_output으로 설정
data_frame_value_meets_condition.to_excel(writer, sheet_name="jan_13_output", index=False)
# 파일 자장
writer.save()