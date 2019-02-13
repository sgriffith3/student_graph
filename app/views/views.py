#!/usr/bin/env python3

from app.app import app
from flask import Blueprint, Flask, render_template, request

blueprint = Blueprint('templated', __name__, template_folder='templates')

"""
This program is designed to assist instructors in tracking the student's
progress in labs throughout the lessons
"""

"""
Logic:
    If student marks lab(x) complete, update student graph on website


time.sleep(60)
"""


@blueprint.route("/student_roster", methods=['GET', 'POST'])
def student_roster():
    return render_template("student_roster.html", name="Student Roster")


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index.html', methods=['GET', 'POST'])
@blueprint.route('/course_roster.html', methods=['GET', 'POST'])
def course_roster():
    if request.method == 'POST':
        if request.form['submit_button'] == 'start':
            return render_template("student_roster.html", name='Student Roster')
        elif request.form['submit_button'] == 'end':
            pass
            # return request.form('index.html', 'index')
    else:
        return render_template("course_roster.html", name="Course Roster")

