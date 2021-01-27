#-*- coding: utf-8 -*-

import sys
import pandas as pd
# 입력파일을 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받기
output_file = sys.argv[2]
# 데이터 형태가 csv파일로 파일 읽기
data_frame = pd.read_csv(input_file)
# 특정 조건을 찾기 위한 배열
import_dates = ['1/20/14', '1/30/14']
# 특정 조건이 있는 것을 읽어서 배열 생성
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(import_dates), :]
# csv파일 형태로 파일 쓰기
data_frame_value_in_set.to_csv(output_file, index=False)