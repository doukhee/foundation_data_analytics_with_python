#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# ggplot 스타일 시트를 사용한다는 함수
# plt.style.use()는 차트의 스타일 변경하는 함수
plt.style.use('ggplot')
# 레이블 생성(x데이터)
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
# 레이블의 인덱스 생성
customers_index = range(len(customers))
# 판매액을 생성(y데이터)
sale_amounts = [127, 90, 201, 111, 232]
# plt.figure()는 새로운 화면을 생성해준다.
fig = plt.figure()
# 화면을 행렬로 분활하여 위치에 빈화면 생성
# fig.add_subplot(row, column, position)는 row, column으로 화면을 분환한다. position은 선택할 화면의 위치를 말한다
ax1 = fig.add_subplot(1, 1, 1)
# 막대 그래프를 생성한다
# ax1.bar(x, y, align='', color='') x 데이터 배열, y 데이터 배열 align은 x축에 막대를 위치를 정의한다
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
# x축의 눈금 위치를 아래쪽에 위치한다
ax1.xaxis.set_ticks_position('bottom')
# y축의 눈금 위치를 왼쪽에 위치한다
ax1.yaxis.set_ticks_position('left')
# 막대의 눈금을 레이블을 인덱스에서 실제 이름으로 변경한다
plt.xticks(customers_index, customers, rotation=0, fontsize='small')
# x축의 이름을 정의
plt.xlabel('Customer Name')
# y축의 이름을 정의
plt.ylabel('Sale Amount')
# 차트의 이름을 정의
plt.title('Sale Amount per Customer')
# 차트를 저장
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()

