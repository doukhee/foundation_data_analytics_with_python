#-*- coding: utf-8 -*-
import sys
# 분석할 파일 첫 인자로 받기
input_file = sys.argv[1]
# 결과 파일 두번째 인자로 받기
output_file = sys.argv[2]
# 파일 읽기 모드로 열고, filereader로 변수 선언 with을 사용 시 loop가 끝날 때 자동으로 파일을 닫아준다.
with open(input_file, 'r', newline='') as filereader:
    # 파일 쓰기 모드로 열곡 filewriter로 변수 선언 with을 사용 시 loop가 끝날 때 자동으로 파일을 닫아준다.
    with open(output_file, 'w', newline='') as filewriter:
        # 파일 한줄일기
        header = filereader.readline()
        # 공백 제거
        header = header.strip()
        # 구분자 쉼표로 배열 만들기
        header_list = header.split(',')
        # 읽은 값 출력
        print(header_list)
        # 파일 쓰기 문자열로 읽어온 값 쉼표를 더해서 생성
        filewriter.write(','.join(map(str, header_list)) + '\n')
        #filewriter.write(','.join(map(str, header_list)))
        # 반복문으로 계속 해서 읽어오기
        for row in filereader:
            # 공백 젝거
            ow = row.strip()
            # 구분자로 나누어서 배열 생성
            row_list = row.split(',')
            # 배열 값 출력
            print(row_list)
            # 파일 쓰기 문자열로 읽어온 값 쉼표를 더해서 생성
            filewriter.write(','.join(map(str, row_list)) + '\n')
            #filewriter.write(','.join(map(str, row_list)))
