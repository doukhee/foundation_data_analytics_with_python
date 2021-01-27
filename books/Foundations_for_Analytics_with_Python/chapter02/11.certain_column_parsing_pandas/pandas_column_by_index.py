# -*- coding: utf-8 -*-

import pandas as pd
import sys
# 입력파일을 첫번쨰 인자로 받는다.
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받는다.
output_file = sys.argv[2]
# pandas의 csv파일을 읽어오는 함수를 이용하여 읽어온다.
data_frame = pd.read_csv(input_file)
# 첫번쨰 인자와 세번째 인자의 열을 읽어와서 배열로 저장한다.
data_frame_column_by_index = data_frame.iloc[:, [0,3]]
# csv파일로 저장한다.
data_frame_column_by_index.to_csv(output_file, index=False)