import sqlite3, random
from models import Employee


def getNewId():
    return random.getrandbits(28)


employees = [
    {

        'fullname': 'John H Doe',
        'firstname': 'John',
        'lastname': 'Doe',
        'middlename': 'Hailey',
        'designation': 'Software Engineer',
        'dateofbirth': '21 June 1998',
        'joiningdate': '10 December 2020',
        'contactdetailsphone': '+1604-409-801',
        'contactdetailsemail': 'john.doe@gmail.com'
    },
    {

        'fullname': 'James D Jason',
        'firstname': 'James',
        'lastname': 'Jason',
        'middlename': 'Doe',
        'designation': 'Software Architect',
        'dateofbirth': '22 June 2008',
        'joiningdate': '10 December 2020',
        'contactdetailsphone': '+1704-409-901',
        'contactdetailsemail': 'james.jason@gmail.com'
    },

]


def connect():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    init_create_table_query = "CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, fullname TEXT,firstname TEXT,lastname TEXT,middlename TEXT,designation TEXT,dateofbirth TEXT,joiningdate TEXT,contactdetailsphone TEXT,contactdetailsemail TEXT)"
    cur.execute(init_create_table_query)
    conn.commit()
    conn.close()
    for i in employees:
        emp = Employee(getNewId(), i['fullname'], i['firstname'], i['lastname'], i['middlename'], i['designation'],
                       i['dateofbirth'], i['joiningdate'], i['contactdetailsphone'], i['contactdetailsemail'])
        insert(emp)


def insert(employee):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    insert_query = "INSERT INTO employees VALUES (?,?,?,?,?,?,?,?,?,?)"
    cur.execute(insert_query, (
        employee.id,
        employee.fullname,
        employee.firstname,
        employee.lastname,
        employee.middlename,
        employee.designation,
        employee.dateofbirth,
        employee.joiningdate,
        employee.contactdetailsphone,
        employee.contactdetailsemail
    ))
    conn.commit()
    conn.close()


def fetchall():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    fetch_all_query = "SELECT * From employees"
    cur.execute(fetch_all_query)
    rows = cur.fetchall()
    employees = []
    for i in rows:
        employee = Employee(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9])
        employees.append(employee)
    conn.close()
    return employees
