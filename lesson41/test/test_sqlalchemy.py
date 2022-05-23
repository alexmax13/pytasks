from lesson39 import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestSqlAlchemy:
    def setup(self):
        self.engine = create_engine("postgresql://san:san5065@104.248.80.229:5432/task_2_san", echo=False)
        self.session = sessionmaker(bind=self.engine)()
        self.l39 = Lesson39(self.session)
        self.l40 = Lesson40(self.session)

    def test_39task1(self):
        result = []
        query = self.session.execute("select first_name, last_name from employees;")
        for item in query:
            result.append(f"{item.first_name} {item.last_name}")

        res = self.l39.task1()
        assert result == res

    def test_39task2(self):
        result = []
        query = self.session.execute("SELECT first_name, last_name, round(salary/12) FROM employees;")
        for item in query:
            result.append(
                f"{item[0]} {item[1]} has {item[2]} monthly salary")

        res = self.l39.task6()
        assert result == res

    def test_40task1(self):
        result = []
        query = self.session.execute(
            "select employees.first_name, employees.last_name,\
             department.department_name, department.department_id\
              from employees inner join department on\
               employees.department_id::varchar = department.department_id;"
        )
        for item in query:
            result.append(item)

        res = self.l40.task1()
        assert result == res

    def test_40task6(self):
        result = []
        query = self.session.execute(
            "select employees.first_name|| ' ' ||employees.last_name as Name,\
             jobs.job_title as Title, max_salary - salary as Salary_dif \
              from employees inner join jobs on employees.job_id = jobs.job_id;"
        )
        for item in query:
            result.append(
                f"{item[0]}: {item[1]}"
                f" | dif_salary: {item[2]}"
            )

        res = self.l40.task6()
        assert result == res

    def test_40task9(self):
        result = []
        query = self.session.execute(
            "select department.department_name, count(employees.employee_id)\
             from employees inner join department\
              on employees.department_id::varchar = department.department_id::varchar group by department_name;"
        )
        for item in query:
            result.append(f"{item[0]} has {item[1]} employees")

        res = self.l40.task9()

        assert result == res
