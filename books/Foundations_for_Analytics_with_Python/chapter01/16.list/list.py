# -*- coding: utf-8 -*-
# 리스트를 만들기 위해 대괄호를 사용한다.
# len() 함수를 통해 리스트 내 원소의 수를 센다.
# max() 함수와 min() 함수는 최대/최소 값을 찾느다.
# count() 함수는 리스트 내 특정 값이 등정한 횟수를 센다.
a_list = [1, 2, 3];
print("Output #58: {}".format(a_list));
# 리스트 내의 원소를 구하여 표출
print("Output #59: a_list has {} element".format(len(a_list)));
print("Output #60: the maximum value in a_list is {}".format(max(a_list)));
print("Output #61: the minmum value in a_list is {}".format(min(a_list)));
another_list = ['printer', 5, ['str', 'circle', 9]];
print("Output #62: {}".format(another_list));
print("Output #63: another_list also has {} elements.".format(len(another_list)));
print("Output #64: 5 is another_list {} time".format(another_list.count(5)));