# 7.5 You have an employee entity with id, name, salary and list of projects.
# A Project entity which has an id, a name, a list of grades and a satisfactory flag.
# The satisfactory flag is true when the average of grades is over 8 and false when the average is lower than 8.
# You should update the satisfactory flag when the list of grades gets updated.
# Initially all projects have a grade of 8.

# Create a program where
#     you can display all employees;
#     you can display all projects;
#     you can add employees;
#     you can add projects;
#     you can remove projects based on the id;
#     you can search for projects which are satisfactory;
#     you can add a grade to a project;
#     you can add a project to an employee;

import csv
from pathlib import Path

class Employee:
	def __init__(self, employee_id:int, name:str, salary:int, projects:list):
		self.employee_id = employee_id
		self.name = name
		self.salary = salary
		self.projects = projects

	def __str__(self):
		return f'{self.employee_id}\t{self.name}\t{self.salary}\t{self.projects}'

class Project:
	def __init__(self, project_id:int, project_name:str, grades:list, flag:bool):
		self.project_id = project_id
		self.project_name = project_name
		self.grades = grades
		self.flag = flag
	
	def __str__(self):
		return f'{self.project_id}\t{self.project_name}\t{self.grades}\t{self.flag}'

employees = []
projects = []
satisfactory = []

def read_projects_csv(file_name):
	with open(Path('projects.csv'), 'r') as csv_proj:
		csv_reader = csv.DictReader(csv_proj)
		for line in csv_reader:
			projects.append(create_project(line))
			satisfactory.append(line['project_name'])

def avg_grade(num):
	sum_grades = 0
	for x in num:
		sum_grades += int(x)
	avg = sum_grades / len(num)
	return avg

def create_project(line):
	project_id = line['project_id']
	project_name = line['project_name']
	grades = line['grades'].split(',')
	flag = line['flag']
	return Project(project_id, project_name, grades, flag)

def read_employee_csv(file_name):
	with open(file_name, 'r') as csv_empl:
		csv_reader = csv.DictReader(csv_empl)
		for line in csv_reader:
			employees.append(create_employee(line))

def create_employee(line):
	employee_id = line['employee_id']
	name = line['name']
	salary = line['salary']
	projects = line['projects'].split(',')
	return Employee(employee_id, name, salary, projects)

# display all employees:
def display_all_employees():
	print("These are all the employees: ")
	for employee in employees:
		print(employee)

# add employee:
def add_employee():
	new_empl_id = int(input("What is the ID of the new employee?: "))
	new_name = input("What is the name of the new employee? ")
	new_salary = int(input("What is the salary of the new employee? "))
	new_projects = []
	new_employee = Employee(new_empl_id, new_name, new_salary, new_projects)
	employees.append(new_employee)

def write_employee(file_name):
	with open(file_name, 'w') as csv_file:
		fieldnames = ['employee_id', 'name', 'salary', 'projects']
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()
		for employee in employees:
			csv_writer.writerow({'employee_id':employee.employee_id,'name':employee.name,'salary':employee.salary,'projects':employee.projects})

# display all projects:
def display_all_projects():
	print("\nThese are all the projects: ")
	for project in projects:
		print(project)

# add project:
def add_project():
	new_proj_id = int(input("What is the ID of the new project? "))
	new_proj_name = input("What is the name of the new project? ")
	new_grade = ['8']
	new_flag = True
	new_project = Project(new_proj_id, new_proj_name, new_grade, new_flag)
	projects.append(new_project)

def write_project(file_name):
	with open(file_name, 'w') as csv_file:
		fieldnames = ['project_id', 'project_name', 'grades', 'flag']
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()
		for project in projects:
			csv_writer.writerow({'project_id':project.project_id,'project_name':project.project_name,'grades':project.grades,'flag':project.flag})

# # remove project based on id:
# def remove_project():
# 	del_proj = input("What is the ID of the project you want to remove? ")
# 	with open('projects.csv', 'r') as csv_proj:
# 		csv_reader = csv.DictReader(csv_proj)
# 		with open('projects_test.csv', 'w', newline='') as new_csv:
# 			csv_writer = csv.writer(new_csv, delimiter=',')
# 			for line in csv_reader:
# 				if line['project_id'] != del_proj:
# 					csv_writer.writerow(line)

# show projects that have a satisfactory grade
def display_satisfactory():
	print("\nThe satisfactory projects are: ")
	for x in satisfactory:
		print(x)

# add a new grade to a project
def add_grade():
	user_input = int(input("What is the ID of the project to which you want add a new grade? "))
	for project in projects:
		if user_input == int(project.project_id):
			new_grade = input("What is the new grade? ")
			project.grades.append(new_grade)
			if avg_grade(project.grades) < 8:
				project.flag = False
				if project in satisfactory:
					satisfactory.remove(project)
			else:
				if project not in satisfactory:
					satisfactory.append(project)
		

# add a project to an employee
def add_proj_to_empl():
	user_input = input("What employee receives a new project? ")
	added_proj = input(f"What project is added to {user_input} ? ")
	for employee in employees:
		if employee.name == user_input:
			employee.projects.append(added_proj)

# def write_employees_csv():
# 	with open('employees_test.csv', 'r') as in_file:
# 		csv_reader = csv.DictReader(in_file)
# 		with open('employees.csv', 'w') as out_file:
# 			fieldnames = ['employee_id','name','salary','projects']
# 			csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter=',')
# 			csv_writer.writeheader()
# 			for line in csv_reader:
# 				csv_writer.writerow(line)

# def write_projects_csv():
# 	with open('projects_test.csv', 'r') as in_file:
# 		csv_reader = csv.DictReader(in_file)
# 		with open('projects.csv', 'w') as out_file:
# 			fieldnames = ['project_id','project_name','grades','flag']
# 			csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter=',')
# 			csv_writer.writeheader()
# 			for line in csv_reader:
# 				csv_writer.writerow(line)

read_employee_csv('employees.csv')
read_projects_csv('projects.csv')

display_all_employees()
display_all_projects()

user_input = input("\nWould you like to see the satisfactory projects? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	display_satisfactory()
user_input = input("\nWould you like to add a new employee? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	add_employee()
user_input = input("\nWould you like to add a new project? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	add_project()
user_input = input("\nWould you like to add a new project to a certain employee? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	add_proj_to_empl()
user_input = input("\nWould you like to add a new grade to a certain project? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	add_grade()
user_input = input("\nWould you like to remove a certain project? (y/N) ")
if user_input in ['y', 'yes', 'Yes']:
	remove_project()

write_employee('employees.csv')
write_project('projects.csv')
# write_employees_csv()
# write_projects_csv()

print("\nGoodbye!")