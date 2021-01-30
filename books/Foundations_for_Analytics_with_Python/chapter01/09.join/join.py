# -*- coding: utf-8 -*-
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: First piece :{0}, second piece : {1} Third piece : {2}".format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(",")
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}.".format(string2_list[0], string2_list[1], string2_list[5], \
    string2_list[-1]))
print("Output #25: {0}".format(",".join(string2_list)))