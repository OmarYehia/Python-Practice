from Employee import *
from Office import *
from databaseHandler import insert_office
import re


def print_menu():
    print("""
    +-------------------------------+
    |      Employee Manager         |
    +-------------------------------+
    | 1- Add employee               |
    | 2- Add office                 |
    | 3- Send email                 |
    | 4- Get all employees          |
    | 5- Get employee               |
    | 6- Fire employee              |
    | q- quit                       |
    +-------------------------------+
    \n""")


def app():
    flag = True
    print_menu()
    db = connect_db()
    create_tables_if_not_exists(db)
    disconnect_db(db)

    while flag:
        user_input = input("Please choose an operation: \n")
        print()

        if user_input == '1':
            valid_email = False
            valid_salary = False

            name = input("Please enter full name: \n")
            money = int(input("How much money he has: \n"))
            sleep_hours = int(input("How many hours he slept: \n"))
            meals = int(input("How many meals he ate: \n"))
            emp_id = int(input("Enter id: \n"))
            while not valid_email:
                email = input("Enter email: \n")
                if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
                    valid_email = True
                else:
                    print("Enter a valid email address")
            work_hours = int(input("How many hours he works: \n"))
            while not valid_salary:
                salary = int(input("Enter salary: \n"))
                if salary >= 1000:
                    valid_salary = True
                else:
                    print("Salary must be larger than 1000")
            is_manager = input("Is he a manager (y/n)? \n")
            if is_manager == 'y':
                is_manager = True
            else:
                is_manager = False
            office_name = input("Type name of office he's in: \n")

            emp = Employee(name, money, sleep_hours, meals,
                           emp_id, email, work_hours, salary, is_manager)
            Office.hire(office_name, emp)
            print("Employee inserted successfully")
        elif user_input == '2':
            office_name = input("Choose office name: \n")
            db = connect_db()
            insert_office(db, office_name)
            disconnect_db(db)
            print("Office inserted successfully")
        elif user_input == '3':
            to = input("to: ")
            subject = input("subject: ")
            body = input("body: ")
            reciever_name = input("reciever_name: ")
            Employee.send_email(to, subject, body, reciever_name)
        elif user_input == '4':
            office_name = input("What office would you like to see: \n")
            employees = Office.get_all(office_name)
            for emp in employees:
                print(emp)
        elif user_input == '5':
            emp_id = int(input("Please enter employee id: \n"))
            emp = Office.get_emp(emp_id)
            if emp:
                print(emp)
            else:
                print("Employee not found")
        elif user_input == '6':
            emp_id = int(input("Please enter employee id: \n"))
            Office.fire(emp_id)
        elif user_input == 'q':
            flag = False
            print("Thank you for using the app")


app()
