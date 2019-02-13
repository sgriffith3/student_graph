import time
import flask


def start_class():
    x = input("Has class started?: ")
    while x.lower() != x.startswith("q"):
        if x.lower().startswith("n"):
            time.sleep(60)
        else:
            print("Alright, lets go!")
            break
    return flask.render_template("student_roster.html", "Student Roster")

start_class()

