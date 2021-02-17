#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# 차트의 스타일을 ggplot으로 설정
plt.style.use('ggplot')
# numpy 모듈의 arange 함수는 반열린구간 [start, stop) 에서 step 의 크기만큼 일정하게 떨어져 있는 숫자들을 array 형태로 반환해 주는 함수다. step은 값의 차이를 말한다
x = np.arange(start=1., stop=15., step=1.)
# y_liner데이터를 넘파이의 랜덤 함수를 이용해서 생성한다
y_liner = x + 5. * np.random.randn(14)
# y_quadratic데이터를 넘파이의 랜덤 함수를 이용해서 생성한다
y_quadratic = x**2 + 10. * np.random.randn(14)
# poly1d = 1 차원 다항식 클래스. 1차원 함수로 만드는 함수
# polyfit에서 세번쨰 인자는 찾고자 하는 함수의 차수입니다 최소 제곱 다항식 함수로 만들어 주는 함수 deg는 다항식으로 정도를 결정 차수 결정?
fn_linear = np.poly1d(np.polyfit(x, y_liner, deg=1))
# 차수를 데이터 찾기
# poly1d = 1 차원 다항식 클래스. 1차원 함수로 만드는 함수
# polyfit에서 세번쨰 인자는 찾고자 하는 함수의 차수입니다 최소 제곱 다항식 함수로 만들어 주는 함수 deg는 다항식으로 정도를 결정 차수 결정?
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
# 빈화면 생성
fig = plt.figure()
# 화면에서 차트 위치를 설정
ax1 = fig.add_subplot(1, 1, 1)
# 화면에 차트 추가
ax1.plot(x, y_liner, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', fn_quadratic(x), 'g-', linewidth=2)
# x축의 라벨 위치를 아래쪽에 보이게 설정
ax1.xaxis.set_ticks_position('bottom')
# y축의 라벨 위치를 왼쪽에 보이게 설정
ax1.yaxis.set_ticks_position('left')
# 차트 타이틀 설정
ax1.set_title('Scatter Plots with Best Fit Lines')
# x축 라벨 설정
plt.xlabel('x')
# y축 라벨 설정
plt.ylabel('f(x)')
# x축의 범위를 최소값 보다 1 작게 최대 값은 1보다 크게 데이터 기반으로 설정
plt.xlim((min(x)-1., max(x) + 1.))
# y축의 범위를 최소값 보다 10 작게 최대 값은 10보다 크게 데이터 기반으로 설정
plt.ylim((min(y_quadratic) - 10., max(y_quadratic) + 10.))
# 차트 저장 해상도는 400 여백은 좁게 설정
plt.savefig('scatter_plot.png', dpi=400, bbox_inches='tight')
# 차트 보여주기
plt.show()