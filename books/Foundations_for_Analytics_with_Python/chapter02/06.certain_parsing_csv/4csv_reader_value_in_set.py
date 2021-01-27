#-*- coding: utf-8 -*-

import csv
import sys
# 입력파일을 첫번째인자로 받기
input_file = sys.argv[1]
# 출려파일을 두번째 인자로 받기
output_file = sys.argv[2]
# 특정 날짜 조건을 찾기 위한 배열
important_dates = ['1/20/14', '1/30/14']
# 입력파일을 열고, csv_in_file로 변수선언
with open(input_file, 'r', newline='') as csv_in_file:
    # 출력파일을 열고, csv_out_file로 변수선언
    with open(output_file, 'w', newline='') as csv_out_file:
        # 파일 읽기 구분자는 쉼표인 것을 알려주기
        filereader = csv.reader(csv_in_file, delimiter=',')
        # 파일 쓰기 구분자는 쉼표로 구성할 것을 알려주기
        filewriter = csv.writer(csv_out_file, delimiter=',')
        # 첫줄 읽기
        header = next(filereader)
        # 읽은 첫 줄을 파일에 쓰기
        filewriter.writerow(header)
        # 파일을 읽기
        for row_list in filereader:
            # 날짜는 4번쨰 위치에 존재하는 것을 알려주기 위한 변수 선언
            a_date = row_list[4]
            # 조건에 맞을 경우
            if a_date in important_dates:
                # 파일 쓰기
                filewriter.writerow(row_list)
                # 확인을 위한 출력
                print(row_list)