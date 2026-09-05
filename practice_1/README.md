# Data Structures Practice

*Lists • Tuples • Dictionaries*

## Lists

**Q1.** You have a list of daily bus fares collected: `[150, 200, 150, 300, 250, 200, 150]`. Use `append()` to add today's fare of `180`, then print the total number of fares recorded.

**Q2.** A teacher has a list of students: `['Amos', 'Faith', 'Brian', 'Wanjiku']`. A new student, `'Grace'`, joins and should be second on the register. Use `insert()` to add her, then print the updated list.

**Q3.** Given a list of scores `[45, 78, 92, 33, 67, 88, 21]`, use a list comprehension to create a new list containing only the scores that are `50` or above (a pass).

**Q4.** You have a list of product names: `['Sugar', 'Rice', 'Beans', 'Maize', 'Salt']`. Sort the list alphabetically using `sort()`, then use `sorted()` on the original unsorted order to sort it in reverse - and print both results to show the difference between the two.

**Q5. CHALLENGE:** A shop has a stock list: `['Sugar', 'Rice', 'Beans', 'Maize']`. Make a backup copy of it before removing `'Beans'` (out of stock) from the live list. Print both lists at the end to prove the backup was unaffected.

## Tuples

**Q6.** Create a tuple called `location` containing a town name and its coordinates: `('Kericho', -0.3676, 35.2831)`. Print each element using indexing (not a loop).

**Q7.** Given the tuple `dimensions = (12, 8)`, unpack it into two variables `length` and `width` in one line, then print the area (`length * width`).

**Q8.** Try to change the second item of the tuple `fruits = ('Mango', 'Banana', 'Orange')` to `'Pineapple'` using indexing (e.g. `fruits[1] = 'Pineapple'`). Run it, note the error you get, and explain in one sentence why it happens.

**Q9.** You have a tuple of exam scores: `(67, 89, 45, 92, 78)`. Without converting it to a list, find and print the highest score, the lowest score, and how many scores there are.

**Q10. CHALLENGE:** A list contains three tuples, each representing a student's name and score: `[('Amos', 78), ('Faith', 92), ('Brian', 65)]`. Loop through the list and print each student's name and score in the format `'Amos scored 78'`. *(Hint: unpack each tuple directly in the `for` line.)*

## Dictionaries

**Q11.** Create a dictionary called `student` with keys `name`, `age`, and `class`, holding your own made-up values. Print the student's name using key access.

**Q12.** Given `prices = {'Sugar': 150, 'Rice': 120, 'Beans': 180}`, add a new item `'Maize': 90` to the dictionary, then update `'Sugar'` to `160`. Print the final dictionary.

**Q13.** Loop through this dictionary and print each item in the format `'Sugar costs Ksh 150'`: `prices = {'Sugar': 150, 'Rice': 120, 'Beans': 180}`. *(Hint: use `.items()`.)*

**Q14.** Given `stock = {'Sugar': 40, 'Rice': 0, 'Beans': 15, 'Maize': 0}`, use a loop to print only the products that are out of stock (value is `0`).

**Q15. CHALLENGE:** You have sales data for a week:

```python
sales = {
    'Mon': 4200,
    'Tue': 3800,
    'Wed': 5100,
    'Thu': 4700,
    'Fri': 6200
}