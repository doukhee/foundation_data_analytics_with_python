# -*- coding: utf-8 -*-
import csv
import sys

input_file = sys.argv[1]
outputt_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(outputt_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=",")
        filewriter = csv.writer(csv_out_file, delimiter=",")
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)