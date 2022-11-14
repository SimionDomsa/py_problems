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

c1 = Course(111, "algebra liniara", 95)
c2 = Course(222, "analiza matematica", 90)
c3 = Course(333, "geometrie analitica", 85)
c4 = Course(444, "statistica", 80)

test = [c1, c2, c3, c4]    

#print all courses:

print("Available courses: ")
for i in test:
    i.print_courses()


#add a new course:
