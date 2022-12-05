# 7.5 You have an employee entity with id, name, salary and list of projects.
# A Project entity which has an id, a name, a list of grades and a satisfactory flag.
# The satisfactory flag is true when the average of grades is over 8 and false when the average is lower than 8.
# You should update the satisfactory flag when the list of grades gets updated.
# Initially all projects have a grade of 8.

# Create a program where
#     you can display all employees
#     you can display all projects
#     you can add employees
#     you can add projects
#     you can remove projects based on the id
#     you can search for projects which are satisfactory
#     you can add a grade to a project
#     you can add a project to an employee


from pathlib import Path

class Employee:
    def __init__(self, empl_id, empl_name, salary, projects=[]):
        self.empl_id = empl_id
        self.empl_name = empl_name
        self.salary = salary
        self.projects = projects
    
    def display_employee(self):
        print(f"\t{self.empl_id}\t{self.empl_name}\t{self.salary}\t{self.projects}")

def display_all_employees():
    with open(Path('employees_75.txt'), 'r') as file:
        employees = list()
        lines = [line.rstrip() for line in file]
        for empl in lines:
            empl_id, empl_name, salary, projects = empl.split(" ")
            employees.append(Employee(int(empl_id), empl_name, int(salary), projects.split(',')))
        for i in employees:
            i.display_employee()

def add_employee():
    new_empl_id = int(input("What is the new employee's ID? "))
    new_empl_name = input("What is the new employee's name? ")
    new_empl_salary = int(input("What is the new employee's salary? "))
    new_empl_projects = input("What projects will the new employee be working on? (separate with comma) ")
    new_employee = f"{new_empl_id} {new_empl_name} {new_empl_salary} {new_empl_projects}"

    with open(Path("employees_75.txt"), "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(new_employee)

class Project:
    def __init__(self, proj_id, proj_name, flag, grade = []):
        self.proj_id = proj_id
        self.proj_name = proj_name
        self.grade = grade
        self.flag = flag

    def display_project(self):
        print(f"\t{self.proj_id}\t{self.proj_name}\t{self.grade}\t{self.flag}")

def display_all_projects():  
    with open(Path('projects_75.txt'), 'r') as file:
        lines = [line.rstrip() for line in file]
        projects = list()
        for proj in lines:
            proj_id, proj_name, *grade, flag = proj.split(" ")
            if flag == "True":
                projects.append(Project(proj_id, proj_name, grade, flag))
        for i in projects:
            i.display_project()

def add_new_proj():
    user_input = input("Add new project? (y/N) ")
    if user_input in ['y', 'yes', 'Y']:
        new_proj_id = input("What is the ID of the new project? ")
        new_proj_name = input("What is the name of the new project? ")
        new_proj_grade = 8
        new_proj_flag = "True"
        new_project = f"{new_proj_id} {new_proj_name} {new_proj_grade} {new_proj_flag}"

        with open(Path("projects_75.txt"), "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(new_project)

def delete_proj():
    user_input = input("Delete a project? (y/N) ")
    if user_input in ['y', 'yes', 'Y']:
        new_input = input("What is the ID of the project to be deleted? ")
        with open('projects_75.txt', 'w') as f:
            lines = f.readlines()
            for line in lines:
                if new_input not in line:
                    file.write(line)

def avg_grade(num):
    sum_grades = 0
    for x in num:
        sum_grades = sum_grades + int(x)           
    avg = sum_grades / len(num)
    return avg

def display_satisf_proj():  
    with open(Path('projects_75.txt'), 'r') as file:
        lines = [line.rstrip() for line in file]

        projects = list()
        grades = list()
        for proj in lines:
            proj_id, proj_name, *grade, flag = proj.split(" ")
            y = avg_grade(grade)
            if y >= 8:
                projects.append(proj_name)
                grades.append(y)
        for i in range(len(projects)):
            print(f"{projects[i]} with an average of {grades[i]}")

# def add_grade2proj():
#     with open(Path('projects_75.txt'), 'r+') as file:
#         lines = [line.rstrip() for line in file]

#         projects = list()
#         grades = list()
#         for proj in lines:
#             proj_id, proj_name, *grade, flag = proj.split(" ")
#             projects.append(proj_name)
#             grades.append(grade)
#         print("\nThe projects are: ")
#         for i in range(len(projects)):
#             print(projects[i])
#         user_input = input("Which project receives a new grade? ")
#         while True:
#             if user_input not in projects:
#                 print("Please type a valid project: ")
#             else:
#                 break
#         new_grade = int(input("What is the new grade? "))
#         if new_grade < 0:
#             new_grade = 0
#         elif new_grade > 10:
#             new_grade = 10
#         else:
#             pass
#         grades.append(new_grade)
#         for proj in lines:
#             if user_input not in proj:
#                 file.write(proj)
#             else:
#                 file.write(f"{proj_id} {proj_name} {grades} {flag}")


# display all employees:
print("The employee list is:")
display_all_employees()

# display all projects:
print("This are all the projects:")
display_all_projects()

# add a new employee:
while True:
    user_input = input("Add new employee? (y/N) ")
    if user_input in ['y', 'yes', 'Y']:
        add_employee()
    else:
        break

# add a new project:
while True:
    user_input = input("Add new project? (y/N) ")
    if user_input in ['y', 'yes', 'Y']:
        add_project()
    else:
        break

# search for projects which are satisfactory
user_input = input("Display satisfactory projects? (average grade >=8) (y/N) ")
if user_input in ['y', 'Y', 'yes']:
    display_satisf_proj()

# add a new grade to a project
# user_input = input("Add new grade to a specific project? (y/N) ")
# if user_input in ['y', 'Y', 'yes']:
#     add_grade2proj()

print("\nHave a good day, bye!")