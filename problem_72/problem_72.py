#7.2 You have a Course entity which has id, course name and teacher name. Create a program where you can

#display all the courses,
#add a new course,
#search and remove a course by id
#display all the courses where there's a specific teacher

from collections import defaultdict
import pprint

courses = {
	111: ["matematica", "domnu trandafir"],
	222: ["chimie", "ana manole"],
	333: ["fizica", "albert einstein"],
	444: ["romana", "unguru bulan"],
	555: ["sport", "donald trump"],
	666: ["religie", "ana manole"],
	777: ["economie", "donald trump"]
}

# Display all the courses
def print_courses():
	print("Available courses: ")
	for c in courses:
		print(f"\t{c}\t{courses[c][0]} \t {courses[c][1]}")

#display all the courses,
print_courses()

#add a new course,
user_input = input("Would you like to add a new course? (y/N): ")
if user_input in ['Y', 'y', 'yes']:
	course_id = int(input("Enter course ID: "))
	while course_id in courses:
		print("Course ID already exists!")
		course_id = int(input("Enter course ID: "))
	course_name = input("Enter course name: ")
	while True:
		exists = False
		for c in courses:
			if course_name == courses[c][0]:
				print("There already exists a course with that name!")
				exists = True
				break
		if exists:
			course_name = input("Enter course name: ")
		else:
			break
	course_teacher = input("Enter teacher's name: ")
	courses[course_id] = [course_name, course_teacher]
else:
	print("Course list remained unchanged.")
	print_courses()

#search and remove a course by id
user_input = input("Would you like to remove a course? (y/N): ")
if user_input in ['Y', 'y', 'yes']:
	n = int(input("What course ID would you like to remove? "))
	if n not in courses:
		print("Course ID does not exist.")
	else:
		courses.pop(n)
	print_courses()
elif user_input == "no":
	print("Course list remained unchanged.")
	print_courses()

#display all the courses where there's a specific teacher
teachers = []
print("Teachers:")
for c in courses:
	teachers.append(courses[c][1])
	print(f"\t{courses[c][1]}")

n = input("What teacher are you interested in? ")
if n != '':
	while n not in teachers:
		n = input("What teacher are you interested in? ")

	print("They teach: ")
	for c in courses:
		if n == courses[c][1]:
			print(f"\t{courses[c][0]}")

print("Goodbye!")
