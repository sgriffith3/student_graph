#!/usr/bin/env python3
import json, requests, datetime, sys


def class_refresh(course_name):
    # student_data = 'http://localhost:5000/'  # Location of json data that is hosted # TODO This is going to need updated
    course_data = '{}.json'.format(course_name)
    # If students update, update json
    # format data


    r = requests.get(course_data)
    metadata = r.json()
    print(metadata)

""" for x in metadata['students']:
    start = ""
    end = ""

    student_labs = {'labs_complete': [{"lab_number": lab_number, 'start_time': start, 'end_time': end}]}

    x.update(student_labs)
labs = []

lab_number = sys.argv[1]
lab_time = datetime.datetime.now('%H%M')
lab_begin = datetime.datetime.now('%H%M') # TODO Make this at the command line entry time
for student in range(r):
    if lab_time != lab_begin:
        labs.append(lab_number, lab_begin, lab_time)
    else:
        labs.append(lab_number, lab_begin)
print("Registering lab %s completed" % lab_number)
"""

class_refresh('table_maker')