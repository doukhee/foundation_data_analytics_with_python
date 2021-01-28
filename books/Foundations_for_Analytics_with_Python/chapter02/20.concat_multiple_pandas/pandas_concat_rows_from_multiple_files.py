# -*- coding: utf-8 -*-

import sys
import glob
import os
import pandas as pd
# 읽어올 파일을 첫번쨰 인자로 받는다
input_path = sys.argv[1]
# 출력파일명을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 파일을 읽어올 경로와 특정 패턴을 가진 파일을 가져온다
all_files = glob.glob(os.path.join(input_path, 'sales_*.csv'))
# 전체 데이터를 저장할 배열 변수
all_data_frames = []
# 파일을 읽어오기 위한 반복문
for file in all_files:
    # 인덱스를 설정하는 열이 없다고 설정하여 파일 읽어오기
    # index_col=None은 default 특정 행을 설정을 하고 싶을 경우 index_col=로 설정해준다.
    data_frame = pd.read_csv(file, index_col=None)
    # 전체 데이터를 저장할 배열에 추가하여 읽어온 데이터를 추가한다
    all_data_frames.append(data_frame)
# 데이터를 이어 붙이기 위한 함수는 concat()이다. ignore_index=True을 줘서 인덱스를 재배열 할 수 있다. axis=0는 행결합을 의미 axis=1은 열결합을 의미한다
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
# 합쳐진 데이터를 파일에 쓴다
data_frame_concat.to_csv(output_file, index=False)
print("{}".format(data_frame_concat))