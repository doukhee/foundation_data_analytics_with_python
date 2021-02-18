#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm
# 데이터를 pandas 형식으로 읽어오기 구분자는 ',' 0번째 줄이 목록 값을 나타낸다고 알려주기
wine = pd.read_csv('../../database/wine/winequality-both.csv', sep=',', header=0)
# 열 헤더의 공백을 언더바로 변경
wine.columns = wine.columns.str.replace(' ', '_')
# 열헤대와 간략하게 5줄 보여주는 출력
print(wine.head())
# 구분을 위한 한줄 띄기
print("")
# 수치형 변수들에 대한 요약 통계 출력
print(wine.describe())
# 구분을 위한 한줄 띄기
print("")
# quality열의 유일 값을 오름차순으로 정령하여 리스트 출력
print(sorted(wine.quality.unique()))
# 구분을 위한 한줄 띄기
print("")
# quality 열에서 유일 값 별 관측 값 개수를 내림차순으로 정렬하여 출력
print(wine.quality.value_counts())
# 구분을 위한 한줄 띄기
print("")
# 와인 종류에 따라 기술통계를 출력하기
print(wine.groupby('type')[['quality']].describe().unstack('type'))
# 구분을 위한 한줄 띄기
print("")
# 특정 사분위수 계산하기
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# 구분을 위한 한줄 띄기
print("")
# 구분을 위한 한줄 띄기
print("")
# 와인 데이터에서 타입 값이 red인경우 quality 값을 가져온다
red_wine = wine.loc[wine['type'] == 'red', 'quality']
# 와인 데이터에서 타입 값이 white인경우 quality 값을 가져온다
white_wine = wine.loc[wine['type'] == 'white', 'quality']
# 차트 색상 정의
sns.set_style('dark')
# 레드와인 히스토그램 생성
print(sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label="Red Wine"))
# 화이트와인 히스토그램 생성
print(sns.distplot(white_wine, norm_hist=True, kde=False, color="white", label="White Wine"))
# 축 라벨 설정
sns.utils.axlabel("Quality Score", "Density")
# 하면의 타이틀 생성
plt.title("Distribution of Quality by Wine Type")
# 레전드 추가 
plt.legend()
# 화면(차트) 보이기
plt.show()
# 그룹별 품질의 평균과 표준 편차 구하기
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
# 와인 종류에 따라 품질의 차이 검정
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# 구분을 위한 한줄 띄기
print("")
# 확인을 위한 출력
print("tstat: %.3f pvalue: %.4f" %(tstat, pvalue))
# 구분을 위한 한줄 띄기
print("")
# 모든 변수 쌍 사이의 상관계수 구하기
print(wine.corr())

# 변수간에 관계 살펴보기
def take_sample(data_frame, replace=False, n=200):
    # 
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
# 변수 간의 관계 구하기
reds_sample = take_sample(wine.loc[wine['type'] == 'red', :])
# 변수 간의 관계 구하기
whites_sample = take_sample(wine.loc[wine['type'] == 'white', :])
# 레드와인 샘플 값과 화이트와인 샘플 값 합치기
wine_sample = pd.concat([reds_sample, whites_sample])
# 
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
# 구분을 위한 한줄 띄기
print("")
# 
print(pd.crosstab(wine.in_sample, wine.type, margins=True))
