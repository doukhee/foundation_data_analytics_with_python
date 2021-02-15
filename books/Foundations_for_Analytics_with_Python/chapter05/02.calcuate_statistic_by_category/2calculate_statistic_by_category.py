#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import csv
import sys
# 날짜형태를 다루기 위한 module 추가
from datetime import date, datetime
# 날짜의 차를 구하기 위한 함수
def date_diff(data1, data2):
    # 예외 발생 시 처리 하기 위한 구문
    try:
        # 첫번째로 들어온 날짜 인자에 두번째로 들어온 날짜인자의 값을 뺀 값을 저장
        # strptime() = format에 따라 구문 분석된, date_string에 해당하는 datetime를 반환합니다.
        # date_string과 format을 time.strptime()로 구문 분석할 수 없거나, 시간 튜플이 아닌 값을 반환하면 ValueError가 발생합니다.
        diff = str(datetime.strptime(data1, '%m/%d/%Y') - datetime.strptime(data2, '%m/%d/%Y')).split()[0]
    # 예외 발생시 처리하는 구문
    except:
        # diff 값을 0으로 설정
        diff = 0
    # 만약 차이의 값이 0:00:00 일 경우
    if diff == "0:00:00":
        # diff 값을 0으로 설정
        diff = 0
    # diff 값을 반환
    return diff
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 딕셔너리 형태의 빈 값을 선언
packages = {}
# 값이 없을 경우 대체할 값 변수 생성
previous_name = "N/A"
# 값이 없을 경우 대체할 값 변수 생성
previous_package = "N/A"
# 값이 없을 경우 대체할 값 변수 생성
previous_package_date = "N/A"
# 첫번째 행을 알려주기 위한 flag
first_row = True
# 오늘 날짜를 월/일/년도로 저장
today = date.today().strftime("%m/%d/%Y")
# 입력 파일을 읽기 모드로 열기
with open(input_file, mode='r', newline='') as input_csv_file:
    # csv 파일을 읽어오기
    filereader = csv.reader(input_csv_file, delimiter=',')
    # 첫줄 읽어오기
    header = next(filereader)
    # 첫줄을 제외하고 파일의 모든 행만큼 반복
    for row in filereader:
        # 첫번째 값인 고객 이름을 읽어온다
        current_name = row[0]
        # 두번째 값인 카테고리를 읽어온다
        current_package = row[1]
        # 세번째 값인 날짜 값을 읽어온다
        current_package_date = row[3]
        # 고객 이름이 packages의 dictionary에 값이 없을 경우
        if current_name not in packages:
            # dictionary형태에 키 값으로 고객 이름으로 생성
            packages[current_name] = {}
        # 카테고리가 고객이름의 키 값으로 저장이 안되어 있다면
        if current_package not in packages[current_name]:
            # 고객이름의 키값의 값을 dictionary형태로 키값을 카테고리로 설정 및 값을 0으로 설정
            packages[current_name][current_package] = 0
        # 전의 고객 이름이 현재 고객 이름과 같지 않을 경우
        if current_name != previous_name:
            # 첫행이면
            if first_row:
                # 첫행이 아니라는 것을 알려주기 위한 flag 변환
                first_row = False
            # 첫행이 아니면
            else:
                # 날짜의 차이를 구하는 함수로 차이 구하기
                diff = date_diff(today, previous_package_date)
                # 전의 카테고리의 값이 패키지에 고객 명의 키값이 아닐 경우
                if previous_package not in packages[previous_name]:
                    # 고객명의 카테고리 키 값의 값을 날짜의 차이를 저장
                    packages[previous_name][previous_package] = int(diff)
                # 전의 카테고리의 값이 패키지에 고객 명의 키값일 경우
                else:
                    # 패키지의 고객명을 키값으로 가지는 dictionary의 전의 카테고리의 값에 날짜의 차이를 더하기
                    packages[previous_name][previous_package] += int(diff)
        # 전의 고객 이름과 현재 고객 이름이 같을 경우
        else:
            # 현재 카테고리 날짜에서 전의 카테고리 날짜 뺀 값 구하기
            diff = date_diff(current_package_date, previous_package_date)
            # 패키지의 전의 고객 이름의 전의 카테고리의 값에 날짜의 차이의 값을 더하기
            packages[previous_name][previous_package] += int(diff)
        # 전의 고객명을 현재 고객명으로 변경
        previous_name = current_name
        # 전의 카테고리를 현재 카테고리로 변경
        previous_package = current_package
        # 전의 카테고리 날짜를 현재 카테고리 날짜로 변경
        previous_package_date = current_package_date
# 목차를 쓸 값들의 배열
header = ['Customer Name', 'Category', 'Total Time (in Days)']
# 출력 파일을 출력 모드로 열기
with open(output_file, mode='w', newline='') as output_csv_file:
    # 파일을 csv 파일쓰기 위한 객체로 생성
    filewriter = csv.writer(output_csv_file, delimiter=',')
    # 목차를 출력 파일에 쓰기
    filewriter.writerow(header)
    # 패키지의 값을 customer_name의 인덱스로 customer_name_value을 가져오는 반복문
    for customer_name, customer_name_value in packages.items():
        # 패키지의 카테고리를 index로 package_category_value로 가져오는 반복문
        for package_category, package_category_value in packages[customer_name].items():
            # 데이터 저장을 위한 빈 배열
            row_of_output = []
            # 고객명과 카테고리 그리고 카테고리의 값을 확인하기 위한 출력
            print(customer_name, package_category, package_category_value)
            # 데이터 저장을 위한 배열에 고객 명 추가
            row_of_output.append(customer_name)
            # 데이터 저장을 위한 배열에 카테고리 추가
            row_of_output.append(package_category)
            # 데이터 저장을 위한 배열에 카테고리 값 추가
            row_of_output.append(package_category_value)
            # 출력 파일에 데이터 쓰기
            filewriter.writerow(row_of_output)