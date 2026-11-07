"""A Nested loops is simply a loop inside another loop"""
days = ["Mon", "Tue"]
sets = [1, 2]

for day in days:
    for s in sets:
        print(f"{day} - Set {s}")


tables = ["Table A", "Table B"]
customers = ["John", "Mary"]

for table in tables:
    for customer in customers:
        print(table, customers)

departments = ["Kitchen", "Reception"]

tasks = ["Cleaning", "Inspection"]
for department in departments:
    for task in tasks:
        print(department, "-", task)


# INDEPENDENT DRILLS (Execution testing)
# imagine a school has three classrooms and three activities.
# How many times will the print execute.

classrooms = ["cluster 1", "cluster 2", "cluster 3"]
activities = ["large stdies", "collaboration", "solo drills"]

for classroom in classrooms:
    for activity in activities:
        print(f"classroom {classroom}, - activity {activities}")


departments = ["Sales", "Finance"]
employees = {
    "Sales": ["John", "Mary", "Peter"],
    "Finance": ["David", "Sarah"]
}

for department in departments:
    for employee in employees[department]:
        print(department, employee)


# Nested loop with an one empty list within a dictionary

departments = ["Sales", "Finance", "IT"]
employees = {
    "Sales": ["John", "Mary"],
    "Finance": [],
    "IT": ["David"]
}

for department in departments:
    for employee in employees[department]:
        print(department, employee)
    
"""From the above so far i have been able to learn the following:
1. Loop execution
2. iteration counts
3. Nested loops with dictionaries
4. Handling empty collections"""

"""3 CORE PRINCIPLE ABOUT LOOPS
1. The outer loop determines how many iterations occur.
2. the inner loop completes its available iterations for each iteration.
3. An empty innere collection means zero inner iterations, not termination of the outer loop."""