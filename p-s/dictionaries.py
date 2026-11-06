# DICTIONARIES
# A dictionary is a Python data structure that stores information in key-value pairs.

"""Unlike list that uses numerical indexes to access its value,
a Dictionary are accessed using their key"""

# using .get()
"""when a grade is not available and you use "student["grade"], it will raises a keyError
but when you use student.get["grade"], it returns None by default. you can also customize the get message"""

employee = {
    "name": "Sarah",
    "department": "Finance",
    "Salary": 50000
}

employee["Salary"] = 60000
employee["Location"] = "Otukpo"

print(employee["Salary"])
print(employee.get("age", 25))
print(employee["Location"])


book = {
    "title": "Python Basics",
    "author": "John",
    "copies": 10
}

book["copies"] = 15
book["category"] = "programming"

print(book["copies"])
print(book["category"])
print(book.get("author"))


# Drill and Deeper understanding

patient = {
    "name": "Daniel",
    "age": 30,
    "ward": "Medical"
}

patient["age"] = 35
patient["blood_group"] = "O+"

print(len(patient))
print(patient.get("gender", "Unknown"))