# -*- coding: utf-8 -*-
import csv
import glob
import os
import sys
# 파일의 경로를 첫번쨰 인자로 받는다
input_path = sys.argv[1]
# 출력파일의 이름을 두번째 인자로 받는다
output_file = sys.argv[2]
# 출력파일의 첫 줄을 정의 하기 위한 배열
output_header_list = ['file Name', 'total sales', 'average_sales']
# 출력파일을 append로 연다
csv_output_file = open(output_file, 'at', newline='')
# csv형태로 쓰겠다고 설정하고 파일을 설정한다.
filewriter = csv.writer(csv_output_file, delimiter=',')
# 파일의 목록을 한줄 작성한다.
filewriter.writerow(output_header_list)
# 입력파일의 경로에 있는 특정 패턴의 파일만 반복하기 위한 반복문
for input_file in glob.glob(os.path.join(input_path, 'sales_*.csv')):
    # 입력파일을 csv 파일로 읽기모드로 열기 및 csv_in_file로 변수 선언
    with open(input_file, 'rt', newline='') as csv_in_file:
        # 파일 읽어오는 것에 대한 변수 선언
        filereader = csv.reader(csv_in_file)
        # 파일에 쓰기 위한 데이터를 임시 저장하기 위한 변수 선언
        output_list = []
        # 파일의 이름을 배열에 추가
        output_list.append(os.path.basename(input_file))
        # 첫줄 건너띄기 위한 next 호출
        header = next(filereader)
        # 전체 판매액을 구하기 위한 변수
        total_sales = 0.0
        # 몇명이 판매가 되었는지 확인을 위한 변수
        number_of_sales = 0.0
        # 한줄씩 파일 읽어오기
        for row in filereader:
            # 판매 총액의 위치이 3번째 위치의 값 저장
            sale_amount = row[3]
            # 전체 판매액을 구하기 위한 값 변환 및 더하기
            total_sales += float(str(sale_amount).strip('$').replace(',',''))
            # 판매 수 증가
            number_of_sales += 1.0
        # 평균 소수점 두자리까지 평균 구하기
        average_sales = '{0:2f}'.format(total_sales / number_of_sales)
        # 파일에 전체 판매액을 쓰기 위한 임시 배열 변수에 추가
        output_list.append(total_sales)
        # 파일에 평균 판매액을 쓰기 위한 임시 배열 변수에 추가
        output_list.append(average_sales)
        # 출력 파일에 한 줄 쓰기
        filewriter.writerow(output_list)
# 파일 스트림 닫아주기
csv_output_file.close()