select FIRST_NAME, LAST_NAME, SALARY FROM employees
where SALARY > 
(select SALARY from employees WHERE LAST_NAME = "Bull");