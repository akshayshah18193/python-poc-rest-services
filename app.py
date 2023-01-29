# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# author akshay shah
from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Employee

app = Flask(__name__)
# create the database and table. Insert 10 test books into db
# Do this only once to avoid inserting the test books into
# the db multiple times
if not os.path.isfile('employees.db'):
    db.connect()


@app.route('/')
def index():
    return render_template("index.html")


def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return True


@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()

    fullname = req_data['fullname']
    firstname = req_data['firstname']
    lastname = req_data['lastname']
    middlename = req_data['middlename']
    designation = req_data['designation']
    dateofbirth = req_data['dateofbirth']
    joiningdate = req_data['joiningdate']
    contactdetailsphone = req_data['contactdetailsphone']
    contactdetailsemail = req_data['contactdetailsemail']
    employees = [e.serialize() for e in db.fetchall()]
    for e in employees:
        if e['contactdetailsemail'] == contactdetailsemail:
            return jsonify({
                # 'error': '',
                'res': f'Error ⛔❌! Employee with email {contactdetailsemail} is already in System',
                'status': '404'
            })
    emp = Employee(db.getNewId(), fullname, firstname, lastname, middlename, designation, dateofbirth, joiningdate, contactdetailsphone, contactdetailsemail)
    print('new Employee: ', emp.serialize())
    db.insert(emp)
    new_emps = [e.serialize() for e in db.fetchall()]
    print('Employees in System:', new_emps)
    return jsonify({
        'res': emp.serialize(),
        'status': '200',
        'msg': 'Success adding new employee in system'
    })


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
