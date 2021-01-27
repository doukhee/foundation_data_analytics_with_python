# -*- coding: utf-8 -*-
import csv
import sys
# 입력파일을 첫번째 인자로 받는다.
input_file = sys.argv[1]
# 출력파일을 두번째인자로 받는다.
outputt_file = sys.argv[2]
# 특정 열 값만 가져오기 위한 행렬
my_columns = [0, 3]
# 읽기모드로 입력파일 열고, csv_in_file로 변수 선언
with open(input_file, 'r', newline='') as csv_in_file:
    # 출력파일을 쓰기 모드로 열고, csv_out_file 변수로 선언
    with open(outputt_file, 'w', newline='') as csv_out_file:
        # 파일을 읽고, 구분자를 쉼표로 설정
        filereader = csv.reader(csv_in_file, delimiter=",")
        # 파일을 쓰기 위해 설정하고, 구분자로 쉼표 설정
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 파일을 다 읽어올때까지 반복문
        for row_list in filereader:
            # 출력할 행을 저장하기 위한 변수 선언
            row_list_output = []
            # 열을 자르기 위한 함수의 위치에 있을 경우
            for index_value in my_columns:
                # 값을 출력할 배열에 추가
                row_list_output.append(row_list[index_value])
            # 파일 쓰기
            filewriter.writerow(row_list_output)
            # 확인을 위한 출력
            print(row_list_output)