#!/usr/bin/env python3

# Import Statements
import csv, json, os
from flask import Flask, request, render_template, redirect, abort, jsonify, session
from flask_session import Session
import datetime
import shutil

# Setting up the main program to run
app = Flask(__name__)

here = os.path.dirname(os.path.abspath(__file__))

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(here, "cache", "session")

Session(app)


@app.route('/update/<course_name>', methods=['POST'])
def update_class_info(course_name):
    # Expected input structure:  {"student_id": "1", "lab_id": 2, "action": "start"} # or "end"
    data = request.get_json() or request.form
    """
    This reads "set the variable 'data' to the information from request.get_json(). However, if that turns up null,
    set the variable 'data' to the information from request.form
    """
    student_id = session.get('student_id')
    lab_id = str(data['lab_id'])
    action = data['action']
    course_file = 'courses/{}.json'.format(course_name)

    with open(course_file) as jf:
        student_dict = json.load(jf)
    timestamp = datetime.datetime.now().isoformat()

    if student_id in student_dict:
        if lab_id not in student_dict[student_id]["labs"]:
            if action != 'start':
                return abort(400, ' "To end before starting stinks more than farting" \n Please select "Start"'
                                  ' on the previous page before clicking Submit')
            student_dict[student_id]["labs"][lab_id] = {"start_time": timestamp}
        else:
            if action != 'end':
                return abort(400, "Wait just a dern minute, you already started this lab! \n Please select 'End' "
                                  "on the previous page before clicking Submit")
            student_dict[student_id]["labs"][lab_id]["end_time"] = timestamp
    else:
        redirect('/register/{}'.format(course_name))

    with open(course_file, 'w') as jf:
        json.dump(student_dict, jf, indent=2)

    return redirect('/table/{}'.format(course_name))
# This function accepts json data that is being served from /<course_name/update>


@app.route('/json/<course_name>')
def home(course_name):
    course_file = 'courses/{}.json'.format(course_name)
    with open(course_file) as jf:
        data = json.load(jf)

    return jsonify(data)
# This function displays the json data


@app.route('/table/<course_name>')
def show_table(course_name):
    print(session)
    if session.get('student_id') and session.get('course_name') == course_name:
        return render_template('table.html', Title=course_name)
    else:
        return redirect('/register/{}'.format(course_name))
# This function checks to make sure a user has a valid "student_id" and will either direct them to register or to
# the 'table.html' page.


@app.route('/')
@app.route('/course_directory')
def index():
    return render_template('course_directory.html')
# The Home Page


@app.route('/instructor', methods=["GET"])
def instructor_home():
    course_dir = os.listdir('courses')
    course_list = []
    for file in course_dir:
        course_list.append(file[:-5])
    return render_template('index.html', course_list=course_list)


@app.route('/instructor', methods=["POST"])
def instructor():
    inst_input = request.form.get("new_course")
    course_file = 'courses/{}.json'.format(inst_input)
    student_dict = {}
    course_dir = os.listdir('courses')
    course_list = []
    for file in course_dir:
        course_list.append(file[:-5])
    print(os.path.abspath(course_file))
    with open(course_file, "w") as jff:
        json.dump(student_dict, jff, indent=2)

    return redirect('/instructor')
# The Instructor/Admin Page, used to initiate new classes and clear existing data


@app.route('/register/<course_name>')
def student_home(course_name):
    return render_template('register.html', Title=course_name)
# A landing page for the users to register for the class --- see def register--


@app.route('/student_register/<course_name>', methods=['POST'])
def register(course_name):
    data = request.get_json() or request.form
    student_id = str(data["student_id"])
    session['student_id'] = student_id
    session['course_name'] = course_name
    course_file = 'courses/{}.json'.format(course_name)
    if not os.path.exists(course_file):
        with open(course_file, "w") as f:
            f.write("{}")

    with open(course_file, "r") as jf:
        student_dict = json.load(jf)

    if student_id in student_dict:
        return redirect('/table/{}'.format(course_name))
    else:
        new_dict = {"student_name": data["student_name"].strip(), "labs": {}}
        student_dict[student_id] = new_dict
    with open(course_file, "w") as jff:
        json.dump(student_dict, jff, indent=2)
    return redirect('/table/{}'.format(course_name))
# Allows users to register for the class, and  updates the json data


if __name__ == '__main__':
    app.run(port=5000)
# Initiates the script


# TODO app.run(host="0.0.0.0", port=5000)
# TODO : Create a new course routine
# TODO : Clear the course
# TODO : Logout
# TODO : Abort the aborts
# TODO : Check session for table page to make sure it is the right one (check session for registered course)
