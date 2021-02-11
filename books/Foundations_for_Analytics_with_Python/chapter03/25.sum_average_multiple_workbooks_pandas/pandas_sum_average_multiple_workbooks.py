#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pandas as pd
# 경로를 읽어오기 위한 module 추가
import glob
# 경로의 값을 비교하기 위한 module 추가
import os
# 안지를 받기 위한 module 추가
import sys
# 입력 폴더를 첫번째 인자로 받는다
input_path = sys.argv[1]
# 출력 파일명을 두번째 인자로 받는다
output_file = sys.argv[2]
# 입력된 폴더의 경로 안에 있는 모든 엑셀 파일을 읽어온다
all_workbooks = glob.glob(os.path.join(input_path, "*.xls*"))
# 데이터를 저장하기 위한 빈 배열 선언
data_frames = []
# 모든 엑셀 파일을 열기 위한 반복문
for workbook in all_workbooks:
    # 엑셀 파일의 모든 sheet를 읽어온 데이터를 저장
    alL_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    # 전체 판매액을 담기 위한 배열
    workbook_total_sales = []
    # 전체 판매 갯수를 담기 위한 배열
    workbook_number_of_sales = []
    # 시트의 데이터를 저장하기 위한 배열
    worksheet_data_frames = []
    # 시트의 데이터를 저장하기 위한 배열
    worksheets_data_frame = None
    # 엑셀 파일의 데이터를 저장하기 위한 배열
    workbook_data_frame = None
    # 시트의 이름과 시트의 데이터를 가져오기 위한 반복문
    for worksheet_name, data in alL_worksheets.items():
        # 엑셀 시트의 전체 판매액의 합을 가져와서 저장
        total_sales = pd.DataFrame([float(str(value).strip("$").replace(",",'')) for value in data.loc[:, "Sale Amount"]]).sum()
        # 엑셀 시트의 전체 판매액을 확인하기 위한 출력
        print("total sales : {}".format(total_sales.get(0)))
        # 엑셀 시트의 판매된 횟수를 가져와서 저장
        number_of_sales = len(data.loc[:, "Sale Amount"])
        # 엑셀 시트의 판매된 횟수를 확인하기 위한 출력
        print("number_of_sales : {}".format(number_of_sales))
        # 엑셀 시트의 판매액의 평균을 구해서 저장
        # pandas.DataFrame()은 Dictionary 타입이므로 나눈 값이 Dictionary 타입이여야한다
        average_sales = pd.DataFrame(total_sales / number_of_sales)
        # 엑셀 시트의 판매액의 평균 값을 확인하기 위한 출력
        print("average_sales : {}".format(average_sales.get(0).get(0)))
        # 엑셀 파일의 판매액 배열에 추가
        workbook_total_sales.append(total_sales)
        # 엑셀 파일의 판매액 갯수 배열에 추가
        workbook_number_of_sales.append(number_of_sales)
        # 출력 파일에 쓰기 위한 Dictionary 타입으로 변경해서 저장
        data = {
            "workbook":os.path.basename(workbook), 
            "worksheet":worksheet_name,
            # 배열 형태이므로 총액을 가져오기 위한 배열 접근
            "worksheet_total":total_sales[0],
            # 이중 배열이므로 평균 값을 가져오기 위한 이차원 배열 접근
            "worksheet_average":average_sales[0][0]
        }
        # dat의 값을 확인하기 위한 출력
        print("data is {}".format(data))
        # 엑셀 파일의 데이터를 저장하기 위한 배열에 헤더 추가
        # DataFrame(columns=, index=,)
        # 행에 해당하는 기준(첫번째 기준)인 인덱스를 index 라는 인수로 전달하며, 열에 해당하는 기준(두번째 기준)인 컬럼을 columns 이라는 인수로 전달합니다
        worksheet_data_frames.append(pd.DataFrame(data, columns=["workbook", "worksheet", "worksheet_total", "worksheet_average"], index=[0]))
    # 엑셀 파일의 데이터에 위 아래로 추가하기
    worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=False)
    # 엑셀 파일의 전체 판매액을 구하고 저장
    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    # 엑셀 파일의 전체 판매액 확인을 위한 출력
    print("workbook_total : {}".format(workbook_total))
    # 엑셀 파일의 전체 판매 횟수를 구하고 저장
    workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
    # 엑셀 파일의 전체 판매 횟수를 확인을 위한 출력
    print("workbook_total_number_of_sales : {}".format(workbook_total_number_of_sales))
    # 엑셀 파일의 전체 판매액의 평균 구하기
    # 엑셀 파일의 전체 판매 횟수는 Dictionary 타입이므로 값에 대해나 접근을 [0]로 한다
    workbook_average = pd.DataFrame(workbook_total / workbook_total_number_of_sales[0])
    # 엑셀 파일의 전체 판매액의 평균 확인을 윟나 출력
    print("workbook_average : {}".format(workbook_average))
    # 출력파일에 쓰기위한 Dictionary 타입으로 변경해서 저장
    workbook_stats = {
        # 엑셀파일의 이름 저장
        "workbook":os.path.basename(workbook), 
        # 엑셀파일 내에 써있는 전체 판매액 접근(Dictionary 타입이라 index를 이용한 접근)
        "workbook_total":workbook_total[0],
        # 엑셀파일 내에 써있는 전체 판매액의 평균 접근(Dictionary 타입이라 index를 이용한 접근)
        "workbook_average":workbook_average[0][0]
    }
    # 확인을 위한 출력
    print("workbook_stats : {}".format(workbook_stats))
    # pandas의 배열 형태로 만들기
    workbook_stats  = pd.DataFrame(workbook_stats, columns=["workbook", 'workbook_total', 'workbook_average'], index=[0])
    # 만들어진 pandas의 DataFrame을 확인하기 위한 출력
    print("workbook_stats : {}".format(workbook_stats))
    # merge를 사용하기 전에 worksheets_data_frame을 확인하기 위한 출력
    print("merge before : {}".format(worksheets_data_frame))
    # merge()함수는 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할때 사용한다.
    # 조인은 열 또는 인덱스에서 수행됩니다. 열의 열을 결합하는 경우 DataFrame 인덱스 는 무시 됩니다. 그렇지 않으면 인덱스의 인덱스 또는 열의 인덱스를 조인하면 인덱스가 전달됩니다. 교차 병합을 수행 할 때 병합 할 열 사양이 허용되지 않습니다.
    # pd.merge(df_left, df_right, how='inner', on=None)이 default이다.
    # on= 합치는 위치의 기준을 알려주는 것이다 how=
    # left : SQL 왼쪽 외부 조인과 유사하게 왼쪽 프레임의 키만 사용합니다. 키 순서를 유지합니다.
    # right : SQL 오른쪽 외부 조인과 유사하게 오른쪽 프레임의 키만 사용합니다. 키 순서를 유지합니다.
    # outer : SQL 완전 외부 조인과 유사하게 두 프레임의 키 통합을 사용합니다. 사전 순으로 키를 정렬합니다.
    # inner : SQL 내부 조인과 유사하게 두 프레임의 키 교차를 사용합니다. 왼쪽 키의 순서를 유지합니다.
    # cross : 두 프레임에서 데카르트 곱을 만들고 왼쪽 키의 순서를 유지합니다. 버전 1.2.0의 새로운 기능.
    # sort : 결과 DataFrame에서 조인 키를 사전 순으로 정렬합니다. False 인 경우 조인 키의 순서는 조인 유형 (how 키워드)에 따라 다릅니다.
    # suffixes : 각 요소가 선택적으로 왼쪽 과 오른쪽의 겹치는 열 이름에 추가 할 접미사를 나타내는 문자열 인 길이 -2 시퀀스 입니다.
    #  문자열 대신 None 값을 전달 하여 왼쪽 또는 오른쪽 의 열 이름 이 접미사없이 그대로 남아 있어야 함 을 나타냅니다 . 값 중 하나 이상은 없음이 아니어야합니다.
    workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on='workbook', how='left')
    # 합쳐진 값을 확인 하기위한 출력
    print("merge after : {}".format(workbook_data_frame))
    # 데이터 형태의 배열에 합쳐진 데이터 추가
    data_frames.append(workbook_data_frame)
# 모든 엑셀파일의 데이터를 위아래로 합치기
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
# 엑셀 파일을 쓰기 위한 설정
writer = pd.ExcelWriter(output_file, datetime_format="dd/mm/yyyy")
# 연결된 모든 데이터를 출력 엑셀 파일에 쓰기
all_data_concatenated.to_excel(writer, sheet_name="sums_and_averages", index=False)
# 파일 저장
writer.save()