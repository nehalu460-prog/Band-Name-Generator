#1
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
     'Harry': "Exceeds Expectations",
    'Ron': "Acceptable",
    'Hermione': "Outstanding",
    'Draco': "Acceptable",
    'Neville': "Fail"
}
print(student_grades)

#2 nested list
students = {
    "student1": {
        "name": "Saksham",
        "age": 20
    },
    "student2": {
        "name": "SAS",
        "age": 20
    }
}

print(students)
print(students["student1"]["name"])
# print(students["student1"]["name"]["student2"]["name"]) gives error 
print(students["student2"]["age"])