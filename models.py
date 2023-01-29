class Employee:
    def __init__(self, id, fullname, firstname, lastname, middlename, designation, dateofbirth, joiningdate,
                 contactdetailsphone, contactdetailsemail):
        self.id = id
        self.fullname = fullname
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.designation = designation
        self.dateofbirth = dateofbirth
        self.joiningdate = joiningdate
        self.contactdetailsphone = contactdetailsphone
        self.contactdetailsemail = contactdetailsemail

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'middlename': self.middlename,
            'designation': self.designation,
            'dateofbirth': self.dateofbirth,
            'joiningdate': self.joiningdate,
            'contactdetailsphone': self.contactdetailsphone,
            'contactdetailsemail': self.contactdetailsemail
        }
