#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# 차트 스타일을 ggplot으로 설정
plt.style.use('ggplot')
# 샘플링 갯수 정의
N = 500
# random.normal(loc, scale, size) 함수는 정규 (가우스) 분포에서 무작위 표본을 추출합니다.
# loc = 분포의 평균 ( "중심")입니다.
# scale = 분포의 표준 편차 (확산 또는 "폭")입니다. 음수가 아니어야합니다.
# size = 모수화 된 정규 분포에서 추출한 샘플.
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
# radom.lognormal(mean, sigma, size) 함수는 로그 정규 분포에서 표본을 추출합니다.
# mean = 기본 정규 분포의 평균값입니다. 기본값은 0입니다.
# sigma = 기본 정규 분포의 표준 편차입니다. 음수가 아니어야합니다. 기본값은 1입니다.
# size = 출력 모양. 예를 들어 주어진 모양이 이면 샘플이 그려집니다.
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
# radom.random_integers(low, high, size) 함수는 low 와 high 사이의 np.int_ 유형의 임의의 정수입니다 .
# low = 분포에서 가져올 가장 낮은 (부호있는) 정수입니다 
# high = 제공된 경우 분포에서 가져올 가장 큰 (부호있는) 정수입니다 
# size = 출력 모양. 예를 들어 주어진 모양이 이면 샘플이 그려집니다
index_value = np.random.random_integers(low=0, high=N-1, size=N)
# 분포 평균의 index_value에 위치한 값 가져오기
normal_sample = normal[index_value]
# 로그 정규 분포에서 index_value에 위치한 값 가져오기
lognormal_sample = lognormal[index_value]
# 박스 데이터 생성
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample, ]
# 빈화면 생성
fig = plt.figure()
# 빈화면 분활하고 위치 지정
ax1 = fig.add_subplot(1, 1, 1)
# x축의 값 배열 생성
box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']
# 박스 플록으로 불러오기
# notch는 사각형으로 그릴 것인지 설정하는 인자 sym은 표현할 형태를 설정
# vert는 가로 세로 설정 하는 것
# whis는  1 사 분위 및 3 사 분위 이상까지 수염의 범위를 결정
# showmeans는 상자의 전체 폭에 걸쳐 선으로 평균 렌더링 결정 인자
# label은 x축의 값을 설정하는 것
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
# x축 타이틀을 밑에 위치하게 설정
ax1.xaxis.set_ticks_position('bottom')
# y축 타이틀을 왼쪽으로 위치하게 설정
ax1.yaxis.set_ticks_position('left')
# 차트 타이틀 설정
ax1.set_title('Box Plots: Resampling of Two Distributions')
# 차트의 x축의 라벨을 distribution으로 설정
ax1.set_xlabel('Distribution')
# 차트의 y축의 라벨을 value로 설정
ax1.set_ylabel('Value')
# 차트 저장
plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()

