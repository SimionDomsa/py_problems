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
    employed = True if (line['employed'])=='True' else False
    return Student(student_id, name, employed)

def display_employed():
    for student in get_employed_students():
        print(student.name)

def get_employed_students():
    for student in get_all_students():
        if student.employed == True:
            return student

def get_all_students():
    return students

def display_all():
    for student in get_all_students():
        print(f'{student.student_id}\t{student.name}\t{student.employed}')

def get_new_student():
    student_id = int(input("What is the ID of the new student? "))
    name = input("What is the name of the new student? ")
    user_input = input("Is the new student employed? (y/N) ")
    employed = True if user_input in ['y','yes','Yes'] else False
    create_new_student_with_input(student_id, name, employed)

def create_new_student_with_input(student_id, name, employed):
    new_student = Student(student_id, name, employed)
    students.append(new_student)

def get_student_update_status():
    user_input = input("What student has a new employment status? ")
    update_status(user_input)

def update_status(user_input):
    for student in students:
        if user_input == student.name:
            student.employed = not student.employed

def delete_unemployed():
    for student in students:
        if student.employed == False:
            students.remove(student)

def delete_student(removed_student):
    for student in students:
        if removed_student == student.name:
            students.remove(student)

def write_students(file_name):
    with open(file_name, 'w', newline='') as fd:
        fieldnames = ['student_id','name','employed']
        csv_writer = csv.DictWriter(fd, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for student in students:
            csv_writer.writerow({'student_id':student.student_id, 'name':student.name, 'employed':student.employed})


# read_students('students.csv')
# print("These are all the students: ")
# display_all()

# user_input = input("Would you like to see only the students that are employed? (y/N) ")
# if user_input in ['y','yes','Yes']:
#     print("These are all the employed students:")
#     display_employed()

# user_input = input("Would you like to add a new student? (y/N) ")
# if user_input in ['y','yes','Yes']:
#     get_new_student()

# user_input = input("Would you like to change the employed status of a student? (y/N) ")
# if user_input in ['y','yes','Yes']:
#     get_student_update_status()

# user_input = input("Would you like to remove unemployed students? (y/N) ")
# if user_input in ['y','yes','Yes']:
#     delete_unemployed()

# user_input = input("Would you like to remove a certain student? (y/N) ")
# if user_input in ['y','yes','Yes']:
#     display_all()
#     removed_student = input("What student would you like to remove? ")
#     delete_student(removed_student)

# write_students('students.csv')
# print("\nGoodbye!")