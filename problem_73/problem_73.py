# 7.3 You have a Course entity with id, name, difficulty Create a program where you can

#     display all the courses
#     add a new course
#     search for courses with a difficulty over a number
#     search for courses with difficulty under a number
#     sort the courses based on difficulty


class Course:
    def __init__(self, course_id, name, diff):
        self.course_id = course_id
        self.name = name
        self.diff = diff

    def print_courses(self):
        print(f"\t{self.course_id}\t{self.name}\t{self.diff}")

c1 = Course(111, "algebra", 95)
c2 = Course(222, "analiza", 90)
c3 = Course(333, "geometrie", 85)
c4 = Course(444, "statistica", 80)

lista = []    

#print all courses:

print("Available courses: ")
for i in lista:
    i.print_courses()


#add a new course:

# user_input = input("Would you like to add a new course? (y/N): ")
# if user_input in ['Y', 'y', 'yes']:
#     new_course_id = int(input("Enter course ID: "))
#     new_course_name = input("What is the name of the course? ")
#     new_course_diff = int(input("What is the difficulty of the new course? "))
#     c5 = Course(new_course_id, new_course_name, new_course_diff)
# else:
#     print("The courses list remains unchanged.")

# test.append(c5)
# for i in test:
#     i.print_courses()

print(type(c1))