#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys

# 입력 파일을 첫번째 인자로 받는다
input_file = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 특정 날짜에 발생하는 로그 메시지 및 빈도를 담기 위한 dictionary
messages = {}
# 모든 로그를 담기 위한 배열
notes = []
# 입력 파일을 읽기 모드로 열기
with open(input_file, mode='r', newline='') as text_file:
    # 행 만큼 반복
    for row in text_file:
        # 만약 행에 [Note]가 있을 경우
        if '[Note]' in row:
            # 행의 공백을 4번 짜르기
            row_list = row.split(' ', 4)
            # 자른 값의 첫번째 값의 공백 제거 및 day 변수로 저장
            day = row_list[0].strip()
            # 자른 값의 4번째 값을 한줄 띄기로 짜르고 공백 제거
            note = row_list[4].strip('\n').strip()
            # 만약 4번째 값이 로그를 담기 위한 배열에 없을 경우
            if note not in notes:
                # 4번째 값을 로그를 담기 위한 배열에 추가
                notes.append(note)
            # 로그 메세지에 날짜가 없을 경우
            if day not in messages:
                # 메세지의 날짜의 카 값의 dictionary 생성
                messages[day] = {}
            # 로그가 메세지의 날짜의 카값에 없을 경우
            if note not in messages[day]:
                # 메세지의 날짜 키 값의 로그 키 값을 1로 설정
                messages[day][note] = 1
            # 로그가 메세지의 날짜의 키값에 있을 경우
            else:
                # 메세지의 날짜 키 값의 로그 키 값을 1을 더하기
                messages[day][note] += 1
# 파일을 쓰기 위한 객체 생성 및 파일 열기
filewriter = open(output_file, mode='w', newline='')
# 목록에 담을 배열 선언
header = ['Date']
# 목록에 담을 배열 확장(추가)
header.extend(notes)
# 하나의 긴 문자열로 변환하기
# map() = header의 각 원소를 문자열 형태로 변경한다
# join() = header의 모든 원소 사이에 쉼표를 입력하여 csv형식에 맞게 긴 문자열을 하나 만든다
# str = 문자열 형태로 만들기 위한 함수
header = ",".join(map(str, header)) + "\n"
# 목록을 확인하기 위한 출력
print(header)
# 출력 파일에 목록 쓰기
filewriter.write(header)
# 메세지의 아이템 만큼 반복하기 위한 반복문
for day, day_value in messages.items():
    # 쓸 데이터를 담기 위한 배열
    row_of_output = []
    # 날짜를 담기
    row_of_output.append(day)
    # 전체 로그를 가져오기 위한 반복문
    for index in range(len(notes)):
        # 메세지의 키값이 로그의 값과 같을 경우
        if notes[index] in day_value.keys():
            # 파일에 쓰기 위한 값에 값을 추가
            row_of_output.append(day_value[notes[index]])
        # 메세지의 키값이 로그의 값이 다른 경우
        else:
            # 파일에 쓰기 위한 값을 0으로 추가
            row_of_output.append(0)
    # csv형식에 맞게 문자열을 만들기
    output = ",".join(map(str, row_of_output)) + "\n"
    # 확인을 위한 출력
    print(output)
    # 파일에 쓰기
    filewriter.write(output)
# 파일을 닫기
filewriter.close()