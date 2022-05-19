from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Countries(Base):
    __tablename__ = "countries"

    country_id = Column(Integer, primary_key=True, nullable=False)
    country_name = Column(String)
    region_id = Column(Integer)


class Locations(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True)
    street_address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    state_province = Column(String)
    country_id = Column(String)


class Department(Base):
    __tablename__ = "department"
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)
    manager_id = Column(Integer)
    location_id = Column(Integer)


class Jobs(Base):
    __tablename__ = "jobs"
    job_id = Column(String, primary_key=True)
    job_title = Column(String)
    min_salary = Column(Integer)
    max_salary = Column(Integer)


class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    hire_date = Column(Date)
    job_id = Column(String)
    salary = Column(Integer)
    commission_pct = Column(Integer)
    manager_id = Column(Integer)
    department_id = Column(Integer)
