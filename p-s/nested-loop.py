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
# How many times will the print execute

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
