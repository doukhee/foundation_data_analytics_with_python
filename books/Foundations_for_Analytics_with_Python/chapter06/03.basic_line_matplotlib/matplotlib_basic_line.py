#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from numpy.random import randn
import matplotlib.pyplot as plt
# ggplot 스타일 시트를 사용한다는 함수
plt.style.use('ggplot')
# 데이터를 랜덤으로 생성
# cumsum() = cumsum은 배열에서 주어진 축에 따라 누적되는 원소들의 누적 합을 계산하는 함수.
plot_data1 = randn(50).cumsum()
# 데이터를 랜덤으로 생성
# cumsum() = cumsum은 배열에서 주어진 축에 따라 누적되는 원소들의 누적 합을 계산하는 함수.
plot_data2 = randn(50).cumsum()
# 데이터를 랜덤으로 생성
# cumsum() = cumsum은 배열에서 주어진 축에 따라 누적되는 원소들의 누적 합을 계산하는 함수.
plot_data3 = randn(50).cumsum()
# 데이터를 랜덤으로 생성
# cumsum() = cumsum은 배열에서 주어진 축에 따라 누적되는 원소들의 누적 합을 계산하는 함수.
plot_data4 = randn(50).cumsum()
# 빈화면 생성
fig = plt.figure()
# 화면 분할 설정
ax1 = fig.add_subplot(1, 1, 1)
# 첫번째 데이터를 선 그래프 그리기 marker는 동그라미, 색깔은 파란색 라인은 선으로 연결 라벨은 Blue Solid로 설정
ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
# 두번째 데이터를 선 그래프 그리기 marker는 +, 색깔은 빨강색 라인은 대시 대시로 연결 라벨은 Red Dashed로 설정
ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
# 첫번째 데이터를 선 그래프 그리기 marker는 별포, 색깔은 초록색 라인은 대시와점으로 연결 라벨은 Green Dash Dot로 설정
ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
# 첫번째 데이터를 선 그래프 그리기 marker는 사각형, 색깔은 주황색 라인은 :으로 연결 라벨은 Orange Dotted로 설정
ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')
# x축의 라벨 위치를 아래에 위치하게 설정
ax1.xaxis.set_ticks_position('bottom')
# y축의 라벨 위치를 왼쪽에 위치하게 설정
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
# x축의 라벨 이름 설정
plt.xlabel('Draw')
# y축의 라벨 이름 설정
plt.ylabel('Random Number')
# 범례를 최상의 위치에 설정
plt.legend(loc='best')
# 차트를 해상도 400으로 여백은 딱 맞게 설정
plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()