from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.sql.expression import func, cast
from tables import *

engine = create_engine("postgresql://san:san5065@104.248.80.229:5432/task_2_san", echo=False)
Session = sessionmaker(bind=engine)


class Lesson39:
    def __init__(self, session: Session):
        self.session = session

    # write a query to display the names (first_name, last_name)
    # using alias name "First Name", "Last Name" from the table of employees;
    def task1(self):
        result = []
        for employee in self.session.query(Employees):
            result.append(f"{employee.first_name} {employee.last_name}")
        return result

    # write a query to get the unique department ID from the employee table
    def task2(self):
        result = []
        for department_id in self.session.query(Employees.department_id).distinct():
            result.append(department_id)
        return result

    # write a query to get all employee details from the employee table ordered by first name, descending
    def task3(self):
        result = []
        for employee in self.session.query(Employees).order_by(Employees.first_name.desc()):
            result.append(f"{employee.first_name} {employee.last_name}, {employee.email}, {employee.phone_number}")
        return result

    # write a query to get the names (first_name, last_name), salary,
    # PF of all the employees (PF is calculated as 12% of salary)
    def task4(self):
        result = []
        for employee in self.session.query(Employees):
            result.append(f"{employee.first_name} {employee.last_name} | Salary:{employee.salary}"
                          f"| PF: {float(employee.salary) * 0.12}")
        return result

    # write a query to get the maximum and minimum salary from the employees table
    def task5(self):
        result = []
        for salary in self.session.query(cast(Employees.salary, Integer)):
            result.append(salary[0])
        print(f" Max salary: {max(result)} | Min salary: {min(result)}")
        return max(result, min(result))

        # max_salary = self.session.query(cast(func.max(Employees.salary), Integer)).first()[0]
        # min_salary = self.session.query(cast(func.min(Employees.salary), Integer)).first()[0]
        # return f" Max salary: {max_salary} | Min salary: {min_salary}"

    # write a query to get a monthly salary (round 2 decimal places) of each and every employee
    def task6(self):
        res = []
        for employee in self.session.query(Employees):
            res.append(
                f"{employee.first_name} {employee.last_name} has {round(employee.salary / 12, 2)} monthly salary")
        return res


class Lesson40:
    def __init__(self, session):
        self.session = session

    # write a query in SQL to display the first name, last name,
    # department number, and department name for each employee
    def task1(self):
        result = []
        for data in self.session.query(
                Employees.first_name, Employees.last_name,
                Department.department_name, Department.department_id) \
                .join(Department, Department.department_id == cast(Employees.department_id, String)):
            result.append(data)
        return result

    # write a query in SQL to display the first and last name, department, city, and state province for each employee
    def task2(self):
        result = []
        for data in self.session.query(
                Employees.first_name, Employees.last_name, Department.department_name,
                Locations.city, Locations.state_province
        ).join(Department, cast(Employees.department_id, String) == Department.department_id
               ).join(Locations, cast(Department.location_id, Integer) == Locations.location_id):
            result.append(data)
        return result

    # write a query in SQL to display the first name, last name, department number,
    # and department name, for all employees for departments 80 or 40
    def task3(self):
        result = []
        for data in self.session.query(
                Employees.first_name, Employees.last_name,
                Department.department_name, Department.department_id
        ).join(Department, cast(Employees.department_id, String) == Department.department_id
               ).where(or_(Employees.department_id == 80, Employees.department_id == 40)):
            result.append(data)
        return result

    # write a query in SQL to display all departments including those where does not have any employee
    def task4(self):
        result = []
        for department in self.session.query(
                Employees.first_name, Employees.last_name,
                Department.department_name, Department.department_id
        ).outerjoin(Employees, cast(Employees.department_id, String) == Department.department_id,
                    ):
            result.append(department)
        return result

    # write a query in SQL to display the first name of all employees including the first name of their manager
    def task5(self):
        result = []
        managers = aliased(Employees)
        for data in self.session.query(Employees.first_name, managers.first_name
                                       ).join(managers, Employees.manager_id == managers.employee_id):
            result.append(data)
        return result

    # write a query in SQL to display the job title, full name (first and last name )
    # of the employee, and the difference between the maximum salary for the job and the salary of the employee
    def task6(self):
        result = []
        for data in self.session.query(
                Employees.first_name, Employees.last_name, Employees.salary, Jobs.job_title, Jobs.max_salary
        ).join(Jobs, Employees.job_id == Jobs.job_id):
            result.append(f"{data.first_name} {data.last_name}: {data.job_title}"
                          f" | dif_salary: {data.max_salary - data.salary}")
        return result

    # write a query in SQL to display the job title and the average salary of employees
    def task7(self):
        result = []
        for data in self.session.query(Jobs.job_title, cast(func.avg(Employees.salary), Integer)
                                       ).join(Employees, Employees.job_id == Jobs.job_id
                                              ).group_by(Jobs.job_title):
            result.append(f"{data.job_title}'s has average salary: {data[1]}")
        return result

    # write a query in SQL to display the full name (first and last name),
    # and salary of those employees who work in any department located in London
    def task8(self):
        result = []
        for data in self.session.query(
                Employees.first_name, Employees.last_name, Employees.salary
        ).join(Department, cast(Employees.department_id, String) == cast(Department.department_id, String)
               ).join(Locations, cast(Department.location_id, String) == cast(Locations.location_id, String)
                      ).where(Locations.city == 'London'):
            result.append(f"{data.first_name} {data.last_name} has {data.salary} salary")
        return result

    # write a query in SQL to display the department name and the number of employees in each department
    def task9(self):
        result = []
        for data in self.session.query(
                Department.department_name, func.count(Employees.employee_id)
                ).join(Employees, cast(Department.department_id, Integer) == cast(Employees.department_id, Integer)
                       ).group_by(Department.department_name):
            result.append(f"{data.department_name} has {data[1]} employees")
        return result


if __name__ == '__main__':
    with Session() as sess:
        l39 = Lesson39(sess)
        l40 = Lesson40(sess)

        print(*l40.task9(), sep='\n')
