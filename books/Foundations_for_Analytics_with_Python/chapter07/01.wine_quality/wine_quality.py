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
    # np.random.choice()는 임의의 표본을 추출하는 함수이다
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
# 변수 간의 관계 구하기
reds_sample = take_sample(wine.loc[wine['type'] == 'red', :])
# 변수 간의 관계 구하기
whites_sample = take_sample(wine.loc[wine['type'] == 'white', :])
# 레드와인 샘플 값과 화이트와인 샘플 값 합치기
wine_sample = pd.concat([reds_sample, whites_sample])
# isin() 특정 배열에 값이 있는지 확인을 위한 함수
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
# 구분을 위한 한줄 띄기
print("")
# crosstab() 원본 데이터의 구조가 분석 기법에 맞지 않아서 행과 열의 위치를 바꾼다거나, 특정 요인에 따라 집계를 해서 구조를 바꿔주는 함수
print(pd.crosstab(wine.in_sample, wine.type, margins=True))
# 시본의 차트 타입을 다크로 설정
sns.set_style('dark')
# 산점도 행렬을 그리기 위한 데이터 객체 생성
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci":False, "x_jitter": 0.25, "y_jitter":0.25}, \
    hue='type', diag_kind='hist', diag_kws={"bins":10, "alpha":1.0}, palette=dict(red="red", white="white"), \
        markers=['o', 's'], vars=['quality', 'alcohol', 'residual_sugar'])
# 값 확인을 위한 출력
print(g)
# 차트의 서브 타이틀 설정
plt.suptitle("Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar", fontsize=14, \
    horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
# 차트 보여주기
plt.show()
# Fit a multivariate linear regression model
#wine_standardized = (wine - wine.mean()) / wine.std()
#formula_all = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# R스타일의 회귀식을 작성
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
#formula_all = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
#formula = 'quality ~ residual_sugar + alcohol'
# 최소제곱버 모형을 이용하여 회귀식을 작성
lm = ols(my_formula, data=wine).fit()
# 일반화선형모형을 사용하여 회귀식을 작성
#lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#lm = smf.glm(formula_all, data=wine_standardized, family=sm.families.Gaussian()).fit()
# 회귀식(간략히 표현해 여러 자료들 간의 관계성을 수학적으로 추정, 설명)의 요약을 출력
print(lm.summary())
# dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해줍니다.
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
# 회귀계수를 시리즈형으로 반환하는 것
print("\nCoefficients:\n%s" % lm.params)
# 회귀계수의 표준오차를 시리즈형으로 반환
print("\nCoefficient Std Errors:\n%s" % lm.bse)
# 회귀식의 수정 결정계수를 반환
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
# F 통계량 및 F 통계량의 P값을 반환
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
# 모든 적합값을 표시하는 대신 관측값의 개수와 적합값의 개수를 각각 lm.nobs와 len(lm.fittedvalues)로 출력
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))
