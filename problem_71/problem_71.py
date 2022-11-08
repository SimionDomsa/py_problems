student = {}

n = input("How many students do you want to add? ")

while len(student) < int(n):
    name = input("Enter student's name: ")
    id1 = input("Enter student's id: ")

    student[name] = int(id1)

print(student)

user_input = input("Would you like to remove a student from the system? (yes/no) ")

if user_input == "yes":
    new_input = input("What is the id of the student who will be removed? ")
    student = {key:val for key, val in student.items() if val != int(new_input)}
    print("The new list is:\n", student)
elif user_input == "no":
    print("The student list remains unchanged.\n", student)
