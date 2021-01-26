#-*- coding: utf-8 -*-
import sys
import csv
# 입력파일을 첫번째 인자로 받는다.
input_file = sys.argv[1]
# 출력파일을 두번쨰 인자로 받는다.
output_file = sys.argv[2]
#입력파일을 읽기 모드로 열고, csv_in_file을 변수로 만든다.
with open(input_file, 'r', newline='') as csv_in_file:
    #출력파일을 쓰기모드로 열고 csv_out_file로 변수를 만든다.
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0].strip())
            # float형태로 변환화기 위한 쉼표 제거 0 세개 표시 시 , 붙는 경우가 있기 때문이다.
            cost = str(row_list[3]).strip('$').replace(',','')
            # Supplier Z 와 cost가 600.0이 조건을 거르기 위한 if문
            if(supplier == 'Supplier Z' or float(cost) > 600.0):
                # 조건에 만족하는 값을 파일에 쓰기
                filewriter.writerow(row_list)
                # 확인을 위한 출력
                print(row_list)