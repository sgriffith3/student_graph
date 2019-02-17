#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for
from class_setup import class_setup
from class_refresh import class_refresh


app = Flask(__name__)


@app.route('/courses/<course_name>')
def get_course_data(course_name):
    if not '{}.csv'.format(course_name):
        return "Class Already Set Up"
    else:
        class_setup(course_name)
        class_refresh(course_name)
        return render_template('class_chart.html')









if __name__ == '__main__':
    app.run(port=8080, debug=True)
