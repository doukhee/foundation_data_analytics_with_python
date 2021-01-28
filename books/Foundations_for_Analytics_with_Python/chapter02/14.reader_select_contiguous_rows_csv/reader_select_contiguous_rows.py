# -*- coding: utf-8 -*-
import sys
import csv
# 입력파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력파일을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 제거할 행을 확인하기 위한 변수 선언
row_counter = 0
# 파일을 읽기 모드로 열고, csv_in_file이라는 변수 선언
with open(input_file, "rt", newline="") as csv_in_file:
    # 파일을 쓰기 모드로 열고, csv_out_file이라는 변수 선언
    with open(output_file, "wt", newline='') as csv_out_file:
        # 파일 읽어오기 구분자는 쉼표라는 것을 알려준다.
        filereader = csv.reader(csv_in_file, delimiter=",")
        # 파일 쓰기 위한 정의 구분자는 쉼표로 설정한다.
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 파일을 끝까지 읽어오기
        for row in filereader:
            # 3번쨍 전까지 15행 이전의 행까지 선택한다는 조건
            if row_counter >= 3 and row_counter <= 15:
                # 파일을 쓰기
                filewriter.writerow([value.strip() for value in row])
                # 팡ㄹ에 쓰이는 데이터 확인 용도의 출력
                print("{}".format([value.strip() for value in row]))
                # 팡ㄹ에 쓰이는 데이터 확인 용도의 출력
                print("row value is {}".format(row))
            # 한줄을 읽었을 시 1의 수를 증가 해준다.
            row_counter += 1