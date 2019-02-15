#!/usr/bin/env python3
from flask import Flask, render_template
import requests
import json
import sys
import datetime


def pull_data(course_data):  # Function to pull json data from the host
    r = requests.get(course_data)
    return r.json()


"""
def push_data(course_name):
    with open('student_progress.json') as progress:
        for i in progress:
            update_json =
"""


metadata_url = 'http://169.254.169.254/openstack/2015-10-15/meta_data.json'  #TODO This is going to need updated
r = requests.get(metadata_url)
if r.status_code != 200:
    print("Failed to connect to metadataservice.  Please notify your instructor.")
    sys.exit(1)

# format data
metadata = r.json()
student_name = metadata['meta']['student_name']
student_number = metadata['meta']['student_number']
class_name = metadata['meta']['class']

if (len(sys.argv)) != 2:
    print("Failed to provide the appropriate number of arguments (1 argument required, the lab number completed)")
    sys.exit(1)
lab_number = sys.argv[1]

print("Registering lab %s completed" % lab_number)
now = datetime.datetime.now().replace(microsecond=0).isoformat(' ')
if 'lab_start':
    lab_end = datetime.datetime.now()


json_data_struct = { 'table' : class_name, 'students':
                {'name': student_name, 'student_id' : student_number,
              'labs_done': {lab_number: {'lab_start' :  datetime.datetime.now(), 'lab_end': lab_end}}}}











