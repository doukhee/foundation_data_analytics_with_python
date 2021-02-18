#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from numpy.random import logistic
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 
sns.set(color_codes=True)
# 
X = np.random.normal(size=1000)
# 히스토그램 생성
sns.distplot(X, bins=20, kde=False, rug=True, label="Histogram w/o Density")
# 
sns.utils.axlabel("value", "Frequency")
# 화면의 타이틀 정의
plt.title("Histogram of a Random Sample from a Normal Distribution")
# 화면의 차트 선 정보 표출
plt.legend()
# 화면 출력
plt.show()
# 회귀선과 일변량 히스토그램을 포함한 산점도
mean, cov = [5, 10], [(1, .5), (.5, 1)]
# 다변량 정규 분포에서 무작위 표본을 추출합니다.
# np.random.multivariate_normal(mean, cov, size)
# mean = N 차원 분포의 평균입니다.
# cov=분포의 공분산 행렬
# size=각 샘플은 N 차원이므로 출력 형태는 (m,n,k,N)입니다
data = np.random.multivariate_normal(mean, cov=cov, size=200)
# pandas 형태의 데이터로 변환 열의 값 정의
data_frame = pd.DataFrame(data, columns=['x', 'y'])
# 회귀선이 있는 산점도와 각 변수의 히스토그램을 만든다
sns.jointplot(x='x', y='y', data=data_frame, kind='reg').set_axis_labels('x', 'y')
# 차트의 서브 타이틀 설정
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")
# 화면 출력
plt.show()
# iris 데이터 가져오기
iris = sns.load_dataset("iris")
# pairplot함수를 사용하여 데이터셋 내 모든 변수쌍에 대해 이변량 산점도
sns.pairplot(iris)
# 화면 출력
plt.show()
# tips 데이터 가져오기
tips = sns.load_dataset("tips")
# FacetGrid에 범주 형 플롯을 그리는 데 사용
# x,y=매개 변수는 데이터의 변수 이름, 긴 형식 데이터를 그리기위한 입력을 사용
# hue=매개 변수는 색상 인코딩을위한 열 이름을 사용
# data= 매개 변수는 플로팅을 위해 DataFrame, 긴 형식 (정리) 데이터 세트를 사용
# box= 플롯의 종류 (범주 형 플로팅 함수의 이름에 해당 {“point”, “bar”, “strip”, “swarm”, “box”, “violin”, or “boxen”}.
sns.factorplot(x='time', y='total_bill', hue='smoker', col='day', data=tips, kind='box', size=4, aspect=.5)
# 화면 출력
plt.show()
# 산점도와 선형 회귀선을 생성
# 부트스트랩 신뢰구간을 포함한 선형희귀모형
sns.lmplot(x="total_bill", data=tips)
# 화면 출력
plt.show()
# 부트스트랩 신뢰 구간을 포함한 로지스틱 희귀모형
tips['big_tip'] = (tips.tip / tips.total_bill) > .15
# 부트스트랩 신뢰 구간을 포함한 로지스틱 희귀모형
sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True, y_jitter=.03).set_axis_labels('Total Bill', "Big Tip")
# 화면의 제목 설정
plt.title("Logistic Regression of Big Tip vs. Total Bill")
# 화면 출력
plt.show()