from databaseHandler import *
from Employee import *


class Office:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_all(office_name):
        db = connect_db()
        employees = get_all_employees(db, office_name)
        disconnect_db(db)
        return employees

    @staticmethod
    def get_emp(employee_id):
        db = connect_db()
        employee = get_employee(db, employee_id)
        disconnect_db(db)
        return employee

    @staticmethod
    def hire(office_name, employee):
        db = connect_db()
        insert_employee(db, employee, office_name)
        disconnect_db(db)

    @staticmethod
    def fire(employee_id):
        db = connect_db()
        delete_employee(db, employee_id)
        disconnect_db(db)
