# -*- coding: utf-8 -*-
import sys
import pandas as pd
# 입력파일을 첫번째 인자로 입력 받느다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 입력 받는다
output_file = sys.argv[2]
# 첫행에 쓰기 위한 목록 배열 변수
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
# 파일을 읽어온다 이때, header는 목록이 없다는 의미의 None 목록의 이름을 설정하기 위한 names=에 목록 배열을 써준다.
data_frame = pd.read_csv(input_file, header=None, names=header_list)
# csv파일로 만드는 함수 
data_frame.to_csv(output_file, index=False)
# 확인을 위한 출력
print("{}".format(data_frame))