# coding: utf-8 -*-

# 특정 패턴과 일차하는 경로를 찾기 위한 모듈 import
import glob
# 파일의 경로를 입력 받기 위한 모듈 imoort
import os
import sys
import csv
# 입력파일을 첫번째 인자로 받는다
input_path = sys.argv[1]
# 파일의 갯수를 파악 하깅 위한 변수
file_counter = 0
# 특정 패턴이 일차하는 파일을 경로에서 찾기 위한 반복문
for input_file in glob.glob(os.path.join(input_path, 'sales_*.csv')):
    # 행을 세기 위한 변수 
    row_counter = 1
    # 파일 읽기
    with open(input_file, 'rt', newline="") as csv_in_file:
        # 파일 읽기 구분은 쉼표로 한다고 설정
        filereader = csv.reader(csv_in_file, delimiter=",")
        # 파일의 첫 줄 읽기
        header = next(filereader)
        for row in filereader:
            # 행의 숫자 증가
            row_counter += 1
    # 파일의 행과 열을 파악하기 위한 출력 
    print('{0!s}: \t{1:d} rows \t {2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    # 파일의 숫자를 세기 위한 변수 증가
    file_counter += 1
# 파일 갯수를 확인하기 위한 출력
print("Number of files: {0:d}".format(file_counter))