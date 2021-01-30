# -*- coding: utf-8 -*-
import re

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39: ")
for word in string_list:
    if pattern.search(word):
        # 위에 <match_word>로 묶은 동일한 패턴을 표출하는 것 그룹 함수로 저장되어 있는 것을 프린트한다.
        print("{:s}".format(pattern.search(word).group("match_word")))
        
        
string1 = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
# 발견된 The를 대소문자 상관 없이 치환한다.
print("Output #40: {:s}".format(pattern.sub("a", string1)))