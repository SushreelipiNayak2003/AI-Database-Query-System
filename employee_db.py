
import sqlite3


class SQLDB:
    def DATABASE(self):
        connection = sqlite3.connect("employee.db")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    employee_name VARCHAR(30),
                    employee_role VARCHAR(30),
                    employee_salary FLOAT,
                    UNIQUE(employee_name, employee_role, employee_salary)
                )
            """)

            records = [
                ('Sushree', 'GEN AI Engineer', 75000),
                ('Lipsa', 'GEN AI Developer', 65000),
                ('Sandhya', 'PYTHON Developer', 50000),
                ('Bunny', 'JAVA Developer', 40000),
                ('Sunny', 'Data SCience Engineer', 40000),
                ('Honey', 'Dot Net Developer', 40000),
            ]

            cursor.executemany("""
                INSERT OR IGNORE INTO employee
                (employee_name, employee_role, employee_salary)
                VALUES (?, ?, ?)
            """, records)

            connection.commit()

        finally:
            connection.close()
