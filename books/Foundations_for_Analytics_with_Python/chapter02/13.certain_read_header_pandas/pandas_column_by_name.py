# -*- coding: utf-8 -*-
import sys
import pandas as pd
# 읽을 파일을 첫번쨰 인자로 받느다.
input_file = sys.argv[1]
# 출력 파일을 두번째 인자로 받는다.
output_file = sys.argv[2]
# csv파일을 읽어온다고 알려주고 읽어오기
data_frame = pd.read_csv(input_file)
# 특정 열의 값을 찾아서 읽고, 배열에 저장
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
# 파일 쓰기
data_frame_column_by_name.to_csv(output_file, index=False)
# 확인을 위한 출력
print(data_frame_column_by_name)