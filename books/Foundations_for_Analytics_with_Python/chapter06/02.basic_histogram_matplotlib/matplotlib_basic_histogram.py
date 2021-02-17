#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# ggplot 스타일 시트를 사용한다는 함수
# plt.style.use()는 차트의 스타일 변경하는 함수
plt.style.use('ggplot')
# 데이터 생성을 위한 기본 값 설정
mu1, mu2, sigma = 100, 130, 15
# 데이터 생성 np.random.randn는 numpy 형식으로 랜덤으로 데이터를 생성
x1 = mu1 + sigma * np.random.randn(10000)
# 데이터 생성 np.random.randn는 numpy 형식으로 랜덤으로 데이터를 생성
x2 = mu2 + sigma * np.random.randn(10000)
# 화면 생성
fig = plt.figure()
# 화면을 분활하기
ax1 = fig.add_subplot(1, 1, 1)
# 히스토그램 생성 bins=빈도를 정하는 것 density는 확률 밀도가 아닌 빈도를 표시한다는 의미
n, bins, patches = ax1.hist(x1, bins=50, density=False, color='darkgreen')
# 히스토그램 생성
n, bins, patches = ax1.hist(x2, bins=50, density=False, color='orange', alpha=0.5)
# x축의 라벨을 아래쪽에 위치
ax1.xaxis.set_ticks_position('bottom')
# y축의 라벨을 왼쪽에 위치
ax1.yaxis.set_ticks_position('left')
# x축 라벨 값 설정
plt.xlabel('Bins')
# y축 라벨 값 설정
plt.ylabel('Number of Values in Bin')
# pyplot.suptitle()은 모든 서브 플롯의 메인 타이틀을 추가합니다
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
# 차트의 타이틀 설정
ax1.set_title('Two Frequency Distributions')
# 차트를 저장 해상도를 400으로 여백을 제거하여 저장한다
plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()