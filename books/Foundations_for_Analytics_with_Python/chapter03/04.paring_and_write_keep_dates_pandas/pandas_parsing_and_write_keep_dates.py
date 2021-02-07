#-*- coding: utf-8 -*-
import sys
import pandas as pd
# 첫번째 인자로 열 파일명이 온다
input_file = sys.argv[1]
# 두번쨰 인자로 파일 생성 이름이 온다
output_file = sys.argv[2]
# 파일을 입력 파일의 january_2013 시트를 연다
date_frame = pd.read_excel(input_file, sheet_name='january_2013')
# 엑셀파일을 쓰기 위한 객체 생성
writer = pd.ExcelWriter(output_file)
# 읽어온 데이터를 엑셀형태로 변환한다 시트의 이름은 jan_13_output으로 설정하여 객체에 전달한다
date_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
# 파일을 저장한다
writer.save()