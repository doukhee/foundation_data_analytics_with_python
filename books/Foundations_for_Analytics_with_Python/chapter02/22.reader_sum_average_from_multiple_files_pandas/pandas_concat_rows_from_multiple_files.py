# -*- coding: utf-8 -*-
import pandas as pd
import glob
import os
import sys
# 입력 파일 경로를 첫번쨰 인자로 받는다
input_path = sys.argv[1]
# 출력파일의 이름을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 입려경로에 있는 파일의 특정 패턴 있는 파일만으로 거른다
all_files = glob.glob(os.path.join(input_path, "sales_*.csv"))
# 데이터를 모두 저장할 배열
all_data_frames = []
# 모든 파일을 반복문으로 하면서 하나하나 파일 명 가져오기
for input_file in all_files:
    # 파일 읽어오기
    data_frame = pd.read_csv(input_file, index_col=None)
    # 모든 판매 액에 위치한 값을 더한 값
    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    # 모든 판매 액을 평균을 내기
    average_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data_frame.loc[:, 'Sale Amount']]).mean()
    # 데이터 형태를 객체 형태로 저장(json type)
    data = {'file Name': os.path.basename(input_file),'total Sales':total_sales, 'average Sales':average_sales}
    # 모든 데이터 형태를 pandas의 data형태로 저장
    all_data_frames.append(pd.DataFrame(data, columns=['file Name', 'total Sales', 'average Sales']))
# 데이터를 연결 시켜서 하나의 배열로 만든다
data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
# 만들어진 데이터 쓰기
data_frames_concat.to_csv(output_file, index=False)