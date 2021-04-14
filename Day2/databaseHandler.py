import mysql.connector


def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="XXX",
        password="XXX",
        database="python_day2"
    )
    return db


def disconnect_db(db):
    db.close()


def create_tables_if_not_exists(db):
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS offices(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) UNIQUE
              );       
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS employees(
                id INT PRIMARY KEY,
                full_name VARCHAR(255),
                money INT,
                sleep_mood VARCHAR(20),
                health_rate INT,
                email VARCHAR(255),
                work_mood VARCHAR(20),
                salary INT,
                is_manager TINYINT,
                office_name VARCHAR(255),
                FOREIGN KEY (office_name)
                    REFERENCES offices(name)
                    ON DELETE SET NULL
            );
        """)

    db.commit()


def get_all_employees(db, office_name):
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM employees WHERE office_name = %s;", (office_name,))
    rows = cur.fetchall()
    return rows


def get_employee(db, employee_id):
    cur = db.cursor()
    cur.execute("SELECT * FROM employees WHERE id = %s;", (employee_id,))
    rows = cur.fetchall()
    return rows if len(rows) > 0 else False


def insert_employee(db, emp, office_name):
    cur = db.cursor()
    cur.execute("""
                INSERT INTO employees (id, full_name, money, sleep_mood, health_rate, email, work_mood, salary, is_manager, office_name)
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                );    
            """, (emp.emp_id, emp.full_name, emp.money, emp.sleep_mood, emp.health_rate, emp.email, emp.work_mood, emp.salary, emp.is_manager, office_name,))
    db.commit()


def delete_employee(db, employee_id):
    cur = db.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s;", (employee_id,))
    db.commit()


def update_employee(db, property, new_value, emp_id):
    cur = db.cursor()
    cur.execute("UPDATE employees SET %s=%s WHERE id=%s ;",
                (property, new_value, emp_id))
    db.commit()


def insert_office(db, office_name):
    cur = db.cursor()
    cur.execute("INSERT INTO offices (name) VALUES (%s);", (office_name,))
    db.commit()
