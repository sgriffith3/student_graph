#!/usr/bin/env python3


import csv
import json

"""
This script takes a .csv file of Student Names and their ID #'s and outputs a .json file of that information
"""
def class_setup(course_name):
    # host_data = 'http://localhost:5000/'  # Location of json data that is hosted
    course_data = '{}.json'.format(course_name)
    roster = '{}.csv'.format(course_name)  # TODO '{}{}{}.csv'.format(host_data, course_name)

    csvfile = open(roster, 'r')
    jsonfile = open(course_data, 'w')

    field_names = (["student_names"])
    reader = csv.DictReader(csvfile, field_names)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


class_setup('python')

name = ["student_name"]

{"student_name": "sam", "null": ["1"], "labs_completed":  [{"lab_number": 1} ,{"lab_start": "2/14/2019 10:02"}, {"lab_end":  "2/15/2019 11:23"}]}
