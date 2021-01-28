# -*- coding: utf-8 -*-

import csv
import sys
import glob
import os
# 파일의 경로를 첫번쨰 인자로 받는다
input_path = sys.argv[1]
# 출력 파일의 이름을 두번쨰 인자로 받는다
output_file = sys.argv[2]
# 첫번째 파일인지 확인하기 위한 Boolean 타입의 값
first_file = True
# 경로에 있는 파일을 읽어오기
for input_file in glob.glob(os.path.join(input_path, 'sales_*.csv')):
    # 읽어오는 파일의 이름을 확인하기 위한 출력
    print(os.path.basename(input_file))
    # 파일 읽어오기
    with open(input_file, "r", newline="") as csv_in_file:
        # 파일 쓰기(with을 사용하면 파일을 닫아주는 것이 loop가 끝날 때, 자동으로 닫아준다.)
        with open(output_file, 'a', newline='') as csv_out_file:
            # 파일을 csv 형태인 것을 알려주고, 구분자가 쉼표라는 것을  알려준다 파일 읽어오기
            filereader = csv.reader(csv_in_file, delimiter=",")
            # 파일을 csv 형태인 것을 알려주고, 구분자가 쉼표라는 것을  알려준다 파일 쓰기
            filewriter = csv.writer(csv_out_file, delimiter=",")
            # 첫번쨰 파일이 맞으면
            if first_file:
                # 파일 전체를 쓰기 위한 반복문
                for row in filereader:
                    # 파일 한줄씩 쓰기
                    filewriter.writerow(row)
                # 첫번째 파일이 이제 아니라는 변경
                first_file = False
            # 첫번쨰 파일이 아니면
            else:
                # 첫번쨰 행은 삭제하기 위한 이동
                header = next(filereader)
                # 파일을 전체를 읽어오기
                for row in filereader:
                    # 파일에 쓰기
                    filewriter.writerow(row)