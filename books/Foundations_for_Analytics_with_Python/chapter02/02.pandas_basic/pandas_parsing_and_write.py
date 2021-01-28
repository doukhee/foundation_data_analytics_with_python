#-*- coding: utf-8 -*-
import sys
import pandas as pd
# 입력파일을 첫번째 인자로 받느다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받느다
output_file = sys.argv[2]
# 파일 읽어오기
data_frame = pd.read_csv(input_file)
# 읽어온 값 확인하기 위한 출력
print(data_frame)
# csv파일 형태로 쓰기
data_frame.to_csv(output_file, index=False)
