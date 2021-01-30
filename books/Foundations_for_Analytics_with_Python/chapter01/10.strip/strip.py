# -*- coding: utf-8 -*-
string3 = " Remove unwanted characters from this string.\t\t \n"
print("Output #26: string3: {0:s}".format(string3))
# 문자열 왼쪽 제거. chars지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
string3_lstrip = string3.lstrip();
print("Output #27: {0:s}".format(string3_lstrip))
# 문자열 오른쪽 제거. chars지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
string3_rstrip = string3.rstrip();
print("Output #28: {0:s}".format(string3_rstrip))
# 문자열 제거. chars지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
string3_strip = string3.strip();
print("Output #29: {0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__--++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__--++"
string4_strip = string4.strip("$_-+")
print("Output #31: {0:s}".format(string4_strip))