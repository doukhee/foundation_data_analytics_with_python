# -*- coding: utf-8 -*-

import re
import sys
import csv
# 입력파일을 첫번째 인자로 받기
input_file = sys.argv[1]
# 출력파일을 두번쨰 인자로 받기
output_file = sys.argv[2]

# 정규표현식으로 패턴을 생성 특정 조건을 찾기 위한 것 re.I는 대소문자 구분 안한다고 알려주는 것
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
# 파일 일기모드로 입력파일 열고, csv_in_file로 변수 선언
with open(input_file, 'r', newline='') as csv_in_file:
    # 파일 쓰기모드로 출력파일 열고, csv_out_file로 변수 선언
    with open(output_file, 'w', newline='') as csv_out_file:
        # 파일 읽기
        filereader = csv.reader(csv_in_file)
        # 파일 쓰기 
        filewriter = csv.writer(csv_out_file)
        # 첫줄 읽어오기
        header = next(filereader)
        # 파일 첫줄 출력파일에 쓰기
        filewriter.writerow(header)
        # 파일을 반복문으로 읽어오기
        for row_list in filereader:
            # 읽어온 줄의 두번째 배열 값 변수 선언
            invoice_number = row_list[1]
            # 정규표현식에 맞으
            if pattern.search(invoice_number):
                # 파일에 한줄 쓰기
                filewriter.writerow(row_list)
                # 확인을 위한 출력
                print(row_list)