employees = []
salaries = []
for _ in range(4):
    name = input("enter the employee's name: ")
    employees.append(name)
    employee_salaries = []
    for month in range (1, 4):
        salary = float(input(f"enter {name}'s salary for {month}st/nd/rd month: "))
        employee_salaries.append(salary)
    salaries.append(sum(employee_salaries))
print("total salaries of each employee: ")
for i in range(4):
    print(f"{employees[i]}: {salaries[i]}")
total_paid = sum(salaries)
print(f"Total amount paid to all employees: {total_paid}")
max_salary_index = salaries.index(max(salaries))
print(f"the employee with the highest income is {employees[max_salary_index]} with {salaries[max_salary_index]}")