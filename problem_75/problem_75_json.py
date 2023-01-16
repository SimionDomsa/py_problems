import json
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

employees_list = []
projects_list = []
satisfactory = []

def read_projects_json(file_name):
	with open(Path('projects.json')) as json_proj:
		data1 = json.load(json_proj)
	for project in data1:
		projects_list.append(create_project(project))
		if avg_grade(project['grades'])>=8:
			satisfactory.append(project['project_name'])

def create_project(project):
	project_id = project['project_id']
	project_name = project['project_name']
	grades = project['grades']
	flag = project['flag']
	return Project(project_id, project_name, grades, flag)

def avg_grade(num):
	avg = sum(num)/len(num)
	return avg
# def avg_grade(num):
# 	sum_grades = 0
# 	for x in num:
# 		sum_grades += int(x)
# 	avg = sum_grades / len(num)
# 	return avg

def read_employee_json(file_name):
    with open('employees.json') as json_empl:
        data2 = json.load(json_empl)
    for employee in data2:
        employees_list.append(create_employee(employee))


def create_employee(employee):
    employee_id = employee['employee_id']
    name = employee['name']
    salary = employee['salary']
    projects = employee['projects']
    return Employee(employee_id, name, salary, projects)

# display all employees:
def display_all_employees():
	print('These are all the employees: ')
	for x in employees_list:
		print(x)

# display all projects:
def display_all_projects():
    print('These are all the projects: ')
    for x in projects_list:
        print(x)

# add employee:
def add_employee():
	new_empl_id = int(input("What is the ID of the new employee?: "))
	new_name = input("What is the name of the new employee? ")
	new_salary = int(input("What is the salary of the new employee? "))
	new_projects = []
	new_employee = Employee(new_empl_id, new_name, new_salary, new_projects)
	employees_list.append(new_employee)

# add project:
def add_project():
	new_proj_id = int(input("What is the ID of the new project? "))
	new_proj_name = input("What is the name of the new project? ")
	new_grade = [8]
	new_flag = True
	new_project = Project(new_proj_id, new_proj_name, new_grade, new_flag)
	projects_list.append(new_project)

# remove project based on id:
def remove_project():
    del_proj = input("What is the ID of the project you want to remove? ")
    for project in projects_list:
        if del_proj == project.project_id:
            del project
        else:
            print('There is no project with that ID.')

# show projects that have a satisfactory grade
def display_satisfactory():
	print("\nThe satisfactory projects are: ")
	for x in satisfactory:
		print(x)

# add a new grade to a project
def add_grade():
	user_input = int(input("What is the ID of the project to which you want add a new grade? "))
	for project in projects_list:
		if user_input == int(project.project_id):
			new_grade = int(input("What is the new grade? "))
			project.grades.append(new_grade)
			if avg_grade(project.grades) < 8:
				project.flag = False
				if project in satisfactory:
					satisfactory.remove(project)
			else:
				project.flag = True
				if project not in satisfactory:
					satisfactory.append(project)                

# add a project to an employee
def add_proj_to_empl():
	user_input = input("What employee receives a new project? ")
	added_proj = input(f"What project is added to {user_input} ? ")
	for employee in employees_list:
		if employee.name == user_input:
			employee.projects.append(added_proj)

# transform employees into dictionaries:
def employee_to_dict():
	employees = []
	for employee in employees_list:
		keys = ['employee_id', 'name', 'salary', 'projects']
		values = [employee.employee_id, employee.name, employee.salary, employee.projects]
		employees.append(dict(zip(keys, values)))
	return employees

# transform projects into dictionaries:
def projects_to_dict():
	projects = []
	for project in projects_list:
		keys = ['project_id', 'project_name', 'grades', 'flag']
		values = [project.project_id, project.project_name, project.grades, project.flag]
		projects.append(dict(zip(keys, values)))
	return projects

# write employees:
def write_employees(file_name):
	with open(file_name, 'w') as json_file:
		json.dump(employee_to_dict(), json_file, indent=4)
        
# write projects:
def write_projects(file_name):
    with open(file_name, 'w') as json_file:
        json.dump(projects_to_dict(), json_file, indent=4)

read_employee_json('employees.json')
read_projects_json('projects.json')

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


write_employees('employees.json')
write_projects('projects.json')

print('Goodbye!')