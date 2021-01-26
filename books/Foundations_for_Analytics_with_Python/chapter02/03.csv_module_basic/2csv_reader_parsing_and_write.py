#-*- coding: utf-8 -*-
import csv
import sys

# 첫번째 인자를 입력파일로 받는다.
input_file = sys.argv[1]
# 두번쨰 인자를 출력파일로 받는다.
output_file = sys.argv[2]
# 일기모드로 파일을 열고 csv_in_file로 변수 설정
with open(input_file, 'r', newline='') as csv_in_file:
    # 쓰기모드로 파일을 열고 csv_out_file로 변수 설정
    with open(output_file, 'w', newline='') as csv_out_file:
        # 입력파일을 csv 모듈로 쉼표를 구분자로 사용한닥고 설정
        filereader = csv.reader(csv_in_file, delimiter=',')
        # 출력파일을 csv 모듈로 쉼표로 구분자를 사용한다고 설정
        filewriter = csv.writer(csv_out_file, delimiter=',')
        # 파일을 읽기 반복문
        for row_list in filereader:
            # 한행씩 파일에 쓰기
            filewriter.writerow(row_list)
            # 확인을 위한 출력
            print(row_list)