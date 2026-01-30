# List Comprehension
import random

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_list.append(n + 1)

print(new_list)

new_list2 = [number + 1 for number in numbers]
print(new_list2)

name = "Dominik"
new_list3 = [letter for letter in name]
print(new_list3)

# Python sequences:
# - list
# - range
# - string
# - tuple

my_range = range(1, 5)

new_list4 = [n * 2 for n in my_range]
print(new_list4)

# Conditional List Comprehension

names = ["Thomas", "Alex", "Beth", "Eleonor", "Freddie"]

new_list5 = [name for name in names if len(name) <= 4]
print(new_list5)

new_list6 = [name.upper() for name in names if len(name) > 4]
print(new_list6)

# Dictionary Comprehension
# new_dict = { new_key: new:value for (key, value) in dict.items() if test}

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = { student: grade for (student, grade) in students_scores.items() if grade >= 60}
print(passed_students)

print('\n' * 4)

import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

#Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)