#!/usr/bin/env python3

# Import Statements
import csv
import json
from flask import Flask, request, render_template, redirect, abort, jsonify
import datetime



# Setting up the main prorgram to run
app = Flask(__name__)



"""

This script takes a .csv file of Student Names and their ID #'s and outputs a .json file of that information. This
is an important step to make sure that students who do not have registered student ID numbers are able to be a part
of this class list.

"""

@app.route('/<course_name>/setup', methods=['POST'])
def class_setup(course_name):
    course_data = '{}.json'.format(course_name)
    roster = '{}.csv'.format(course_name)  # TODO '{}{}{}.csv'.format(host_data, course_name)

    csvfile = open(roster, 'r')
    jsonfile = open(course_data, 'w')

    field_names = ("student_name", "student_id")
    reader = csv.DictReader(csvfile, field_names)
    student_dict = {}
    for row in reader:
        new_dict = {"student_name": row["student_name"].strip(), "labs": {}}
        student_dict[row["student_id"].strip()] = new_dict

    json.dump(student_dict, jsonfile, indent=2)
    print("You Dit id!")
    return redirect('/table/{}'.format(course_name))


"""
This function accepts json data that is being served from /<course_name/update>
"""

@app.route('/<course_name>/update', methods=['POST'])
def update_class_info(course_name):
    # Expected input structure:  {"student_id": "1", "lab_id": 2, "action": "start"} # or "end"
    data = request.get_json() or request.form
    """
    This reads "set the variable 'data' to the information from request.get_json(). However, if that turns up null,
    set the variable 'data' to the information from request.form
    """
    student_id = str(data['student_id'])
    lab_id = str(data['lab_id'])
    action = data['action']
    course_file = '{}.json'.format(course_name)

    with open(course_file) as jf:
        student_dict = json.load(jf)
    timestamp = datetime.datetime.now().isoformat()

    if student_id in student_dict:
        if lab_id not in student_dict[student_id]["labs"]:
            if action != 'start':
                return abort(400, "Witty messsage")
            student_dict[student_id]["labs"][lab_id] = {"start_time": timestamp}
        else:
            if action != 'end':
                return abort(400, "now wait just a dern minute, you already started this lab")
            student_dict[student_id]["labs"][lab_id]["end_time"] = timestamp
    else:
        abort(400, "who are you?")

    with open(course_file, 'w') as jf:
        json.dump(student_dict, jf, indent=2)

    return redirect('/table/{}'.format(course_name))


@app.route('/json/<course_name>')
def home(course_name):
    course_file = '{}.json'.format(course_name)
    with open(course_file) as jf:
        data = json.load(jf)

    return jsonify(data)


@app.route('/roster/<course_name>')
def upload_course_roster(course_name):
    roster = request.form
    

"""This function renders the course template and reads the data from the json file in order
to produce the dynamic html table"""
"""@app.route('/course/<course_name>')
def course(course_name):
    return render_template('{}.html'.format(course_name))
"""

@app.route('/table/<course_name>')
def show_table(course_name):
    return render_template('table.html', Title=course_name)


@app.route('/')
@app.route('/course_directory')
def index():
    return render_template('course_directory.html')

if __name__ == '__main__':
    app.run(port=5000)