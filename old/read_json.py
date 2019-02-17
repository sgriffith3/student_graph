#!/usr/bin/env python3
import json


'''{"student_name": "sam", "null": ["1"], "labs_completed":  
[{"lab_number": 1} ,{"lab_start": "2/14/2019 10:02"}, {"lab_end":  "2/15/2019 11:23"}]}'''

with open("table_maker.json", "r") as f:
    print(json.load(f))
    f.close()

with open("table_maker.json", "r") as p:
    my_dict = {student = "sally"
    id = "2"
    labs_completed = [1, 2, 3, 4, 6]}

    for x in p:
        p + my_dict



