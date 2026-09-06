employees = [
    {"name": "Wanjiru", "dept": "Sales", "salary": 55000},
    {"name": "Otieno",  "dept": "IT",    "salary": 68000},
    {"name": "Achieng", "dept": "Sales", "salary": 49000},
    {"name": "Kiptoo",  "dept": "IT",    "salary": 72000},
    {"name": "Mwangi",  "dept": "HR",    "salary": 45000},
]

# counting total employees
total_employees = len(employees)


# using set to filter unique departments

dept_set = set()
for employee in employees:
    dept_set.add(employee["dept"])

# converting dept set to dept list
dept_list = list(dept_set)


# Average salary per department

# finding unique departments
departments = set()

for employee in employees:
    departments.add(employee["dept"])

# creating empty dict for avg salary
avg_salary = {}

for department in departments:
    # creating empty list for salaries
    salaries = []

    # looping through employees to add salaries to list based on unique depts
    for employee in employees:
        if employee["dept"] == department:
            salaries.append(employee["salary"])

    # finding avg
    avg = sum(salaries) / len(salaries)

    # storing avg salary to avg salary dict
    avg_salary[department] = avg


# highest and lowest paid employees

highest_paid = employees[0]
lowest_paid = employees[0]

for employee in employees:
    if employee["salary"] > highest_paid["salary"]:
        highest_paid = employee

    if employee["salary"] < lowest_paid["salary"]:
            lowest_paid = employee




print("=" * 30)
print()
print(f"Total employees : {total_employees}")
print("=" * 30)

print()
print("Departments")
print()
for dept in dept_list:
    print(dept)
print("=" * 30)
print()

print("Average salary per dept:")
print()
for department,avg in avg_salary.items():
    print(f"{department} : {avg}")
print("=" * 30)
print()

print("Highest paid employee :")
print()
for key, value in highest_paid.items():
    print(f"{key} : {value}")
print("=" * 30)
print()

print("Lowest paid employee :")
print()
for key, value in lowest_paid.items():
    print(f"{key} : {value}")


