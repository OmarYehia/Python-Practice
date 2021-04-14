class Person:
    def __init__(self, full_name, money, sleep_mood, health_rate):
        self.full_name = full_name
        self.money == money
        self.sleep_mood = sleep_mood
        self.health_rate = health_rate

    def sleep():
        pass

    def eat():
        pass

    def buy():
        pass


class Employee(Person):
    def __init__(self, full_name, money, sleep_mood, health_rate,
                 emp_id, email, work_mood, salary, is_manager):
        Person.__init__(self, full_name, money, sleep_mood, health_rate)
        self.emp_id = emp_id
        self.email = email
        self.work_mood = work_mood
        self.salary = salary
        self.is_manager = is_manager

    def work():
        pass

    def send_email():
        pass


class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return {
                    employee_id: employee.employee_id,
                    name: employee.full_name,
                    email: employee.email,
                    sleep_mood: employee.sleep_mood,
                    work_mood: employee.work_mood,
                    health_rate: employee.health_rate,
                    salary: "Confidential" if employee.is_manager else employee.salary,
                    is_manager: employee.is_manager
                }
            else:
                return "Employee not found"

    def hire(self, employee):
        self.employees.append(employee)
        return "Employee added successfully"

    def fire(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return "Employee deleted successfully "
            else:
                return "Employee not found"
