#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas.core.groupby import grouper
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
# 데이터 프레임으로 가져오기
churn = pd.read_csv('../../database/wine/churn.csv', sep=',', header=0)
# 열헤더를 수정
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ','_').str.replace("\'", "").str.strip("?")]
# 새로운 열을 생성 및 where함수를 사용하여 churn 열의 값을 기반으로 churn01 열을 1 또는 0으로 채운다
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
# 값을 5줄만 열 헤더와 함께 출력
print(churn.head())
# groupby() = 같은 값을 하나로 묶어 통계 또는 집계 결과를 얻기 위해 사용하는 것이 groupby입니다.
# agg()는 적용하고 싶은 함수를 입력하여 적용된 값을 얻는 것이다
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))
# 확인을 위한 한 줄 띄기
print("")
# groupby() = 같은 값을 하나로 묶어 통계 또는 집계 결과를 얻기 위해 사용하는 것이 groupby입니다.
# agg()는 적용하고 싶은 함수를 입력하여 적용된 값을 얻는 것이다
print(churn.groupby(['churn']).agg({'day_charge': ['mean', 'std'],
                                "eve_charge": ['mean', 'std'],
                                'night_charge':['mean', 'std'],
                                'intl_charge':['mean', 'std'],
                                'account_length':['count', 'min', 'max'],
                                'custserv_calls':['count', 'min', 'max']}))
# 전체 데이터를 구하기 위한 합
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']
# cut() 동일한 길이로 나누어 주는 함수
# 이 함수는 연속 변수에서 범주 형 변수로 이동할 때도 유용합니다. 예를 들어 컷 은 연령을 연령 범위 그룹으로 변환 할 수 있습니다. 동일한 수의 빈 또는 미리 지정된 빈 배열로의 비닝을 지원합니다.
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
# 배열의 값을 구하는 함수
def get_stats(group):
    return {'min': group.min(), 'max' : group.max(),
    'count' : group.count(), 'mean': group.mean(),
    'std': group.std()}
# 전화한 회수를 같은 값 하나로 묶어 통계 또는 집계 결과를 얻기
grouped = churn.custserv_calls.groupby(factor_cut)
# 확인을 위한 한 줄 띄기
print("")
# unstack() = 가장 안쪽 수준이 피벗 된 인덱스 레이블로 구성된 새 수준의 열 레이블이있는 DataFrame을 반환합니다.
# 데이터를 재구조화 하는 함수
print(grouped.apply(get_stats).unstack())
# qcut() = 순위 또는 샘플 분위수를 기반으로 변수를 동일한 크기의 버킷으로 이산화합니다.
# 변위치를 기반으로 이산화 수행
# account_length 열의 사분위수를 기준으로 분활한 뒤, 그룹별 통계량 구하기
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
# groupby() = 같은 값을 하나로 묶어 통계 또는 집계 결과를 얻기 위해 사용하는 것이 groupby입니다.
grouped = churn.custserv_calls.groupby(factor_qcut)
# 확인을 위한 한 줄 띄기
print("")
# 내가 만든 커스텀 함수(custom function)를 DataFrame에 적용하기 위한 함수는 apply()
print(grouped.apply(get_stats).unstack())
# intl_plan와 vmail_plan 열에 대한 이진형 지시변수를 만들고,
# churn 열과 병합하여 새로운 데이터 만들기
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
# 더미 데이터 만들기
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
# 데이터 병합하기
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
# 확인을 위한 출력 열의 헤더와 5줄 출력
print(churn_with_dummies.head())
# 확인을 위한 한 줄 띄기
print("")
# total_charges를 사분위수로 분활하고, 이진형 지시변수를 만들고, 새로운 더미변수를 churn 데이터 프레임에 추가하기
# 사분위수로 분활할 값의 라벨 이름 배열
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
# 사분위수로 분활하기
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
# 이진형 지시변수로 변환
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
# churn 데이터 프레임에 추가하기
churn_with_dummies = churn.join(dummies)
# 확인을 위한 열 헤더와 5줄 출력
print(churn_with_dummies.head())
# 확인을 위한 한 줄 띄기
print("")
# 테이블의 요약된 정보 출력
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
# 확인을 위한 한 줄 띄기
print("")
# 테이블의 요약된 정보 출력
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
# 확인을 위한 한 줄 띄기
print("")
# 테이블의 요약된 정보 출력
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))
# 독립 변수 만들기
dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
# 상수항 결합하기
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
# 로지스틱 모델로 학습하기?
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
# 확인을 위한 한 줄 띄기
print("")
# 로지스틱 모델의 값을 요약해서보여주기
print(logit_model.summary())
print("\r\nQuantities you can extract from the result : \r\n%s" % dir(logit_model))
print("\r\nCoefficients:\r\n%s" %logit_model.params)
print("\r\nCoefficient Std Error : \r\n%s " % logit_model.bse)

# 선형회귀모형의 연속형 예측값을 0과 1 사이의 확률로 변환하는 함수
def inverse_logit(model_formula):
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula)))

# 모든 독립변수를 평규능로 설정했을 때의 예측 값을 추정한다
at_means = float(logit_model.params[0]) + \
    float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
        float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
            float(logit_model.params[3]) * float(churn['total_charges'].mean())
# 확인을 위한 한 줄 띄기
print("")
# 요소의 평균 값을 구한다
print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("P of churn when ind. vars are their mean: %.3f" % inverse_logit(at_means))

cust_serv_mean = float(logit_model.params[0]) + \
    float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
    float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
    float(logit_model.params[3]) * float(churn['total_charges'].mean())

cust_serv_mean_minus_one = float(logit_model.params[0]) + \
    float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
    float(logit_model.params[2]) * float(churn['custserv_calls'].mean() - 1.0) + \
    float(logit_model.params[3]) * float(churn['total_charges'].mean())

# 확인을 위한 한 줄 띄기
print("")
print(cust_serv_mean)
print(churn['custserv_calls'].mean() - 1.0)
print(cust_serv_mean_minus_one)
print("Probability of churn when account length changes by 1 : %.3f" % (inverse_logit(cust_serv_mean) - inverse_logit(cust_serv_mean_minus_one)))
# 확인을 위한 한 줄 띄기
print("")
# 기존 데이터 셋의 첫 10개 값을 가지고 새로운 관측 값 데이터 셋을 만든다
new_observations = churn.loc[churn.index.isin(range(10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
# 예측 하기
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
# 예측 값 출력
print(y_predicted_rounded)