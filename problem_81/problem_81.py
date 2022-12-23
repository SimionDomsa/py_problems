# 8.1 You have a Student entity which has id, name and employed as properties.

# The user shall be able to:

#     display all the students
#     display all the employed students
#     create a new student
#     Update the employed status of a student
#     Delete all the students that are not employed
#     Delete a specific student

import csv

class Student:
    def __init__(self, student_id:int, name:str, employed:bool):
        self.student_id = student_id
        self.name = name
        self.employed = employed

students = []

def read_students(file_name):
    with open(file_name, 'r') as fd:
        csv_reader = csv.DictReader(fd)
        for line in csv_reader:
            students.append(create_student(line))

def create_student(line):
    student_id = int(line['student_id'])
    name = str(line['name'])
    employed = True if (line['employed'])=='TRUE' else False
    return Student(student_id, name, employed)

def display_employed():
    print("These are all the employed students: ")
    for student in students:
        if student.employed == True:
            print(student.name)

def display_all():
    for student in students:
        print(f'{student.student_id}\t{student.name}\t{student.employed}')

def new_student():
    student_id = int(input("What is the ID of the new student? "))
    name = input("What is the name of the new student? ")
    user_input = input("Is the new student employed? (y/N) ")
    employed = True if user_input in ['y','yes','Yes'] else False
    new_student = Student(student_id, name, employed)
    students.append(new_student)

def update_status():
    user_input = input("What student has a new employment status? ")
    for student in students:
        if user_input == student.name:
            print(student.employed)
            student.employed = not student.employed
            print(student.employed)

read_students('students.csv')
print("These are all the students: ")
display_all()

user_input = input("Would you like to see only the students that are employed? (y/N) ")
if user_input in ['y','yes','Yes']:
    display_employed()

user_input = input("Would you like to add a new student? (y/N) ")
if user_input in ['y','yes','Yes']:
    new_student()

user_input = input("Would you like to change the employed status of a student? (y/N) ")
if user_input in ['y','yes','Yes']:
    update_status()