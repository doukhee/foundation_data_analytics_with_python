#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 차트 스타일을 ggplot 형태로 설정
plt.style.use('ggplot')
# 일행 2열로 화면 나누기
fig, axes = plt.subplots(nrows=1, ncols=2)
# 상위 그래프와 하위 그래프로 나누어서 변수 지정
# ravel() 분배해주는 함수?
ax1, ax2 = axes.ravel()
# 데이터 생성
data_frame = pd.DataFrame(np.random.rand(5, 3), index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'], columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metics'))
# pandas의 dataFrame 형태의 데이터를 막대 그래프로 변경
data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')
# 차트의 라벨 속성 변경
# setp()는 차트의 속성을 변경하는 함수이다
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
# 차트의 라벨 속성 변경
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
# x축의 라벨 설정
ax1.set_xlabel('Customer')
# y축의 라벨 설정
ax1.set_ylabel('Value')
# x축의 라벨의 위치를 아래로 설정
ax1.xaxis.set_ticks_position('bottom')
# y축의 라벨의 위치를 왼쪽으로 설정
ax1.yaxis.set_ticks_position('left')
# 색상을 dictionary 타입으로 생성
colors = dict(boxes='DarkBlue', whiskers='Gray', medians="Red", caps='Black')
# pandas의 dataFrame 형태의 데이터를 박스 그래프로 변경
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')
# 차트의 라벨 속성 변경
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
# 차트의 라벨 속성 변경
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
# x축의 라벨 설정
ax2.set_xlabel('Metric')
# y축의 라벨 설정
ax2.set_ylabel('Value')
# x축의 라벨의 위치를 아래로 설정
ax2.xaxis.set_ticks_position('bottom')
# y축의 라벨의 위치를 왼쪽으로 설정
ax2.yaxis.set_ticks_position('left')
# 차트 저장 해상도 400 여백을 타이트하게 설정하여 저장
plt.savefig('pandas_plots.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()

