#!/usr/bin/env python3
import pandas as pd
# 경로를 가져오기 위한 module 추가
import glob
# 경로에 특정 조건을 패턴을 찾기 위한 module 추가
import os
# 인자를 받기 위한 module 추가
import sys
# 폴더의 경로를 첫번째 인자로 받기
input_folder = sys.argv[1]
# 출력 파일의 이름을 두번째 인자로 받기
output_file = sys.argv[2]
# 모든 엑셀 파일을 찾아서 all_workbooks으로 저장
all_workbooks = glob.glob(os.path.join(input_folder, "*.xls*"))
# 데이터를 저장하기 위한 배열 선언
data_frames = []
# 모든 엑셀 파일을 읽어오기 위한 반복문
for workbook in all_workbooks:
    # 엑셀 파일의 모든 시트를 읽기
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    # 시트 안에 있는 데이터 가져오기 위한 반복문
    for worksheet, data in all_worksheets.items():
        # 안에 있는 모든 데이터를 data_frames에 저장
        data_frames.append(data)
# 모든 데이터를 위아래로 합치기
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
# 엑셀 파일을 만들기 위한 객체 생성
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 모든 데이터를 엑셀 파일에 쓰기
all_data_concatenated.to_excel(writer, sheet_name="all_data_all_workbooks", index=False)
# 파일 저장
writer.save()