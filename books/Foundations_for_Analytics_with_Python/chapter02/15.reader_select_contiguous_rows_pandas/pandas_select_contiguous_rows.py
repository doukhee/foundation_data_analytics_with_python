# -*- coding: utf-8 -*-

import pandas as pd
import sys
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받는다
output_file = sys.argv[2]
# 한줄 자체를 문자열로 읽어서 pandas의 배열 형태로 만든다.
# sep는 구분자 의미 header=None은 첫 줄이 항목을 나타내는 것이 아니라는 것에 대해서 알려주는 것이다.
# data_frame = pd.read_csv(input_file, header=None, sep=";")
# 데이터를 읽어온다. skiprows는 특정행의 데이터를 읽어오지 않을 때 사용한다.
data_frame = pd.read_csv(input_file, header=None, skiprows=[0,1,2,16,17,18])
# 특정행을 삭제할 때 사용이 되는 drop함수이다. 
# data_frame = data_frame.drop([0,1,20,16,17,18])
# 첫번쨰 행의 값을 추가 
# iloc 속성은 행번호를 통해 행 데이터를 가져옵니다. 
data_frame.columns = data_frame.iloc[0]
# 인덱스를 다시 설정하기 위한 함수 
# reindex함수는 재 색인을 하는 함수이다. 현재 데이터의 index 0번을 삭제하고 재 색인 진행
data_frame = data_frame.reindex(data_frame.index.drop(0))
# 가공된 데이터를 엑셀파일 써서 저장
data_frame.to_csv(output_file, index=False)
# 출력 확인을 위한 함수
print("{}".format(data_frame))