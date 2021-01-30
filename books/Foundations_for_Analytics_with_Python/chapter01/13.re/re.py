# -*- coding: utf-8 -*-
from math import exp, log, sqrt
import re

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
# re.compile 텍스트 기반의 패턴을 정규표현식으로 컴파일한다.
# re.I패턴이 대소문자 구분 없이 해당사항을 찾는다.
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    # pattern.search() 일치하는 패턴을 찾는다.
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))