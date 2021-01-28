# -*- coding: utf-8 -*-

import sys
import csv
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번째 인자로 받는다
output_file = sys.argv[2]
# 입렫된 파일을 읽기 모드로 열고, csv_in_file 변수로 선언
with open(input_file, "rt", newline="") as csv_in_file:
    # 출력파일을 쓰기 모드로 열고, csv_out_file 변수로 선언
    with open(output_file, "wt", newline="") as csv_out_file:
        # 파일의 구분자를 쉼표로 하고 파일을 읽어오는 변수 선언
        filereader = csv.reader(csv_in_file, delimiter=",")
        # 파일의 구분자를 쉼표로 하고 파일을 쓰는 변수 선언
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 첫번째 행에 표시하기 위한 변수 배열 선언
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        # 파일의 첫번째 행에 header_list를 쓴다
        filewriter.writerow(header_list)
        # 파일을 읽어오기 위한 반복문
        for row in filereader:
            # 읽어온 값을 파일에 쓴다.
            filewriter.writerow(row)
            # 확인을 위한 출력
            print("{}".format(row))