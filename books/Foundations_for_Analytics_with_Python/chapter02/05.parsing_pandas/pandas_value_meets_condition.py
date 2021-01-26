# -*- coding: utf-8 -*-
import sys
import pandas as pd

# 입력파일 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일 두번째 인자로 받기
output_file = sys.argv[2]

# 데이터 형태가 csv형태인 것을 pandas
data_frame = pd.read_csv(input_file)
# float형태로 Cost값을 저장
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
# 특정 조건에 대해서 찾는 함수인 loc함수를 이용하여 조건에 맞는 값 배열로 저장
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
    .str.contains('Z')) | (data_frame['Cost'] > 600.0), : ]
# 조건에 맞는 값들을 csv파일로 저장
data_frame_value_meets_condition.to_csv(output_file, index=False)
# 값을 확인하기 위한 출력
print(data_frame_value_meets_condition)