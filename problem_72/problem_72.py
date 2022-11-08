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

pprint.pprint(courses)
user_input = input("Would you like to add a new course? (yes/no): ")
if user_input == "yes":
    id_course = int(input("Enter course's id: "))
    name_course = input("Enter course: ")
    teach_name = input("Enter teacher's name: ")
    courses[id_course] = [name_course, teach_name]
    print("The new courses list is:\n")
    pprint.pprint(courses)
elif user_input == "no":
	print("The courses list remains unchanged.\n")
	pprint.pprint(courses)

user_input = input("Would you like to remove a course? (yes/no): ")
if user_input == "yes":
	n = input("What course id would you like removed?: ")
	courses = {key:val for key, val in courses.items() if key != int(n)}
	print("The new courses list is:\n")
	pprint.pprint(courses)
elif user_input == "no":
    print("The courses list remains unchanged.\n")
    pprint.pprint(courses)



new_list = list(courses.values())

list1 = []
list2 = []
for i in range(len(new_list)):
	list1.append(new_list[i][0])
	list2.append(new_list[i][1])
#print(list1)
#print(list2)

teach_set = set((list2))
print(teach_set)
n = input("What teacher are you interested in?: ")
txt = n.lower()
t_subject = []
for i in range(len(list1)):
	if txt == list2[i]:
		t_subject.append(list1[i])
	else:
		pass
	i=i+1
print("They teach: ", t_subject)