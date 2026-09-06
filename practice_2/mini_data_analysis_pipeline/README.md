# Mini Data Analysis Pipeline

You're given a raw dataset: a list of dictionaries, where each dictionary represents one employee with three keys — name, dept, and salary. Your job is to write a program that summarizes this data, the way a very small analytics report would.

## What your program needs to do

1. Start from a given dataset, e.g. a list called `employees`, where each item looks like `{"name": "Wanjiru", "dept": "Sales", "salary": 55000}`.
2. **Total employees**: use `len(employees)` to count how many dictionaries are in the list.
3. **Unique departments**: loop through employees and collect each `dept` value into a `set()` (sets automatically drop duplicates), then convert it to a list if you want to print it neatly.
4. **Average salary per department**: for each unique department, loop through employees again, collect the salaries of people in that department, and compute `sum(salaries) / len(salaries)`. Store the results in a dictionary like `{"Sales": 52000, "IT": 68000}`.
5. **Highest and lowest paid employee overall**: loop through employees once, keeping track of the dictionary with the highest salary seen so far and the one with the lowest (or use `max()`/`min()` with a key function).
6. Print a short summary at the end showing all four results clearly labelled.

## Example test data

\`\`\`python
employees = [
    {"name": "Wanjiru", "dept": "Sales", "salary": 55000},
    {"name": "Otieno",  "dept": "IT",    "salary": 68000},
    {"name": "Achieng", "dept": "Sales", "salary": 49000},
    {"name": "Kiptoo",  "dept": "IT",    "salary": 72000},
    {"name": "Mwangi",  "dept": "HR",    "salary": 45000},
]
\`\`\`

## Stretch goal (optional, still in scope)

These build directly on the same dataset and functions above:

- `department_with_highest_average(employees)` — returns just the name of the top-paying department.
- `headcount_per_department(employees)` — like average salary, but counts people instead of averaging.
- Sort the final department summary alphabetically before printing it.