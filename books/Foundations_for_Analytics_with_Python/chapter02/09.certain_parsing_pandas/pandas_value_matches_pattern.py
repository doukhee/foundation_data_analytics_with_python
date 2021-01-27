# -*- coding: utf-8 -*-

import sys
import pandas as pd
# 입력 파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력 파일을 두번쨰 인자로 받는다.
output_file = sys.argv[2]
# 데이터의 형태가 csv파일로 읽어 온다고 설정
data_frame = pd.read_csv(input_file)
# 001-로 시작하는 Invoice Number를 읽어서 data_frame_value_matches_pattern 배열로 저장한다.
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), : ]
# csv파일 형태로 저장을 한다.
data_frame_value_matches_pattern.to_csv(output_file, index=False)