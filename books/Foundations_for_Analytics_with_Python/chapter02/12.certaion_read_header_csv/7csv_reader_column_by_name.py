# -*- coding: utf-8 -*-

import csv
import sys
# 입력 파일을 첫번째 인자로 받는다.
input_file = sys.argv[1]
# 출력 파일을 두번쨰 인자로 받는다.
output_file = sys.argv[2]
# 특정한 값을 추출하기 위한 값들의 배열
my_columns = ["Invoice Number", "Purchase Date"]
# 특정한 값의 위치를 추출하기 위한 index 배열
my_column_index = []
# 입력파일을 읽기 모드로 열고, csv_in_file로 변수 선언
with open(input_file, 'rt', newline='') as csv_in_file:
    # 출력파일을 쓰기 모드로 열고, csv_out_file로 변수 선언
    with open(output_file, 'wt', newline='') as csv_out_file:
        # 파일을 csv형태인 것을 알려주고, 구분자는 쉼표로 설정하여 읽어온다고 설정
        filereader = csv.reader(csv_in_file, delimiter=",")
        # 파일을 csv형태인 것을 알려주고, 구분자는 쉼표로 설정하여 쓴다고 설정
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 첫줄을 읽어오기
        header = next(filereader)
        # 첫줄의 구분자로 나누어진 배열 요소만큼 반복
        for index_value in range(len(header)):
            # 특정값이 정해져 있는 배열의 값이 첫줄에 있으면
            if header[index_value] in my_columns:
                # my_column_index에 값을 추가
                my_column_index.append(index_value)
        # 파일 첫 한줄을 특정값을 쓰기
        filewriter.writerow(my_columns)
        # 파일을 다 읽을 때까지 반복
        for row_list in filereader:
            # 특정 값을 추출하기 위한 배열
            row_list_output = []
            # 파일의 한줄에 원하는 특정 값 요소가 있을 경우
            # (if문을 안 쓰는 이유 반복을 하면서 특정값을 증가 시켜서 조건이 맞는지 확인을 해야하지만, 이와 같은 형태로 할 경우 자동으로 된다?)
            for index_value in my_column_index:
                # 특정 조건에 해당되는 값을 row_list_output이라는 배열에 추가한다.
                row_list_output.append(row_list[index_value])
            # 파일에 출력할 값을 쓴다.
            filewriter.writerow(row_list_output)
            # 확인을 위한 출력
            print(row_list_output)