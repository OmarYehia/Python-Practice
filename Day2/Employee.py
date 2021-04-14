from Person import *
from databaseHandler import *
from datetime import datetime


class Employee(Person):
    def __init__(self, full_name, money, sleep_hours, meals,
                 emp_id, email, work_hours, salary, is_manager):
        Person.__init__(self, full_name, money, sleep_hours, meals)
        self.emp_id = emp_id
        self.email = email
        self.work_mood = ''
        self.sleep_mood = ''
        self.health_rate = 0
        self.sleep(sleep_hours)
        self.work(work_hours)
        self.eat(meals)
        self.salary = salary
        self.is_manager = is_manager

    def work(self, hours):
        if hours > 8:
            self.work_mood = 'tired'
        elif hours == 8:
            self.work_mood = 'happy'
        else:
            self.work_mood = 'lazy'

    @staticmethod
    def send_email(to, subject, body, reciever_name):
        current_time = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
        # file_name = f"mail_to_{to}_{current_time}.txt"
        # print(file_name)
        # with open(file_name, "w") as f:
        with open("NewEmail.txt", "w") as f:
            f.write(f"""
to: {to}
subject: {subject}
body: {body}
reciever: {reciever_name}
            """)

    def sleep(self, hours):
        if hours == 7:
            self.sleep_mood = 'happy'
        elif hours > 7:
            self.sleep_mood = 'lazy'
        else:
            self.sleep_mood = 'tired'

    def eat(self, meals):
        if meals >= 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= len(items) * 10

        db = connect_db()
        update_employee(db, 'money', self.money, self.emp_id)
        disconnect_db(db)
