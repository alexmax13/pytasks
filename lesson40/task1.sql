select employees.first_name, employees.last_name, department.department_name, department.department_id 
from employees 
inner join department 
on employees.department_id::varchar = department.department_id;



select employees.first_name|| ' ' ||employees.last_name as name, department.department_name as department, locations.city, locations.state_province as state 
from employees 
inner join department 
on employees.department_id::varchar = department.department_id 
inner join locations 
on department.location_id::varchar = locations.location_id::varchar;



select employees.first_name|| '' ||employees.last_name as name, department.department_name, department.department_id 
from employees 
inner join department on employees.department_id::varchar = department.department_id 
where employees.department_id = 40 or employees.department_id = 80;



select employees.first_name|| '' ||employees.last_name as name, department.department_name, department.department_id 
from employees 
right outer join department on employees.department_id::varchar = department.department_id;



select e.first_name as "Employee Name", m.first_name as "Manager" 
from employees e 
join employees m 
on m.manager_id = e.employee_id;



select employees.first_name|| ' ' ||employees.last_name as Name, jobs.job_title as "Title", 
max_salary - salary as "Salary difference" 
from employees 
inner join jobs 
on employees.job_id = jobs.job_id;



select jobs.job_title as "Title", round(avg(employees.salary)) as "Average Salary" 
from employees 
inner join jobs 
on employees.job_id = jobs.job_id group by jobs.job_title;



select employees.first_name|| ' ' ||employees.last_name as Name, employees.salary 
from employees 
join departments using (department_id) 
join locations using (location_id) 
where locations.city = 'London';



select department.department_name, count(employees.employee_id) 
from employees inner join department 
on employees.department_id::varchar = department.department_id::varchar 
group by department_name;



