# 1 test creare student
# 2 test update employee status
# 3 test return students
# 4 test return employed students
# 5
# 6
# 7
# 8
# 9
# 10

from problem_81 import create_student


def test_create_student():
    # setup: introducem un dictionar cu valori
    user_input = {'student_id': '555', 'name': 'Mihai', 'employed': 'True'}
    # assertion: dictionarul sa fie transformat in student si toate campurile sa fie ca cele din dictionar
    student_nou = create_student(user_input)
    assert student_nou.student_id == 555
    assert student_nou.name == 'Mihai'
    assert student_nou.employed == True

    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_update_status():
    # setup: cream un student cu statusul true
    user_input = {'student_id': '555', 'name': 'Mihai', 'employed': 'True'}
    student_nou = create_student(user_input)
    # assertion: modificam statusul si verificam ca statusul a fost modificat
    assert student_nou.employed == True
    student_nou.employed = False
    assert student_nou.employed == False

    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_return_students():
    # setup: introducem o lista de dictionare cu valori
    user_input = [{'student_id': '666', 'name': 'Cezar', 'employed': 'True'},
    {'student_id': '777', 'name': 'Pompei', 'employed': 'False'},
    {'student_id': '888', 'name': 'Nero', 'employed': 'False'}]
    # assertion: elementele listei de dictionare sa fie transformate in studenti
    # si toate campurile sa coincida cu campurile celor din dictionarul introdus
    student1 = create_student(user_input[0])
    student2 = create_student(user_input[1])
    student3 = create_student(user_input[2])
    assert student1.student_id == 666
    assert student1.name == 'Cezar'
    assert student1.employed == True
    assert student2.student_id == 777
    assert student2.name == 'Pompei'
    assert student2.employed == False
    assert student3.student_id == 888
    assert student3.name == 'Nero'
    assert student3.employed == False

    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_return_employed_students():
    # setup: introducem o lista de dictionare cu minim doua valori, cu statusul de employed distinct si
    # elementele listei de dictionare sa fie transformate in studenti
    user_input = [{'student_id': '666', 'name': 'Cezar', 'employed': 'True'},
    {'student_id': '777', 'name': 'Pompei', 'employed': 'False'},
    {'student_id': '888', 'name': 'Nero', 'employed': 'False'}]
    student1 = create_student(user_input[0])
    student2 = create_student(user_input[1])
    student3 = create_student(user_input[2])
    # assertion: campurile elementelor cu valoarea 'True' a statusului employed a studentilor
    # sa coincida cu campurile 'True' din lista de dictionare introdusa 
    assert student1.student_id == 666
    assert student1.name == 'Cezar'
    assert student1.employed == True

    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_create_new_student_with_input():
    # setup: cream o lista goala, cream un dictionar pe care il transformam in student si il adaugam listei
    student_list = []
    user_input = {'student_id': '999', 'name': 'Aurelius', 'employed': 'True'}
    new_student = create_student(user_input)
    student_list.append(new_student)
    # assertion: verificam sa coincida campurile introduse cu cele din dictionar si ca studentul a fost adaugat in lista
    assert new_student.student_id == 999
    assert new_student.name == 'Aurelius'
    assert new_student.employed == True
    assert new_student in student_list
    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_delete_unemployed():
    # setup: cream o lista de dictionare pe care le transformam in studenti, macar unul din ei sa aiba status employed False
    user_input = [{'student_id': '666', 'name': 'Cezar', 'employed': 'True'},
    {'student_id': '777', 'name': 'Pompei', 'employed': 'False'},
    {'student_id': '888', 'name': 'Nero', 'employed': 'False'}]
    students = list(create_student(student) for student in user_input)
    # assertion: inlaturam elementele cu campul employed False si verificam ca au fost inlaturate din lista initiala de dictionare
    students = [student for student in students if student.employed == True]
    for student in students:
        assert student.employed == True
    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

def test_delete_student():
    # setup: cream o lista de dictionare pe care le transformam in studenti
    user_input = [{'student_id': '666', 'name': 'Cezar', 'employed': 'True'},
    {'student_id': '777', 'name': 'Pompei', 'employed': 'False'},
    {'student_id': '888', 'name': 'Nero', 'employed': 'False'}]
    students = list(create_student(student) for student in user_input)
    # assertion: inlaturam un element cu campul "name" specific si verificam ca s-a sters din lista
    students = [student for student in students if student.name != 'Nero']
    assert {'student_id': '888', 'name': 'Nero', 'employed': 'False'} not in students
    print('test passed')
    # teardown: nu e nevoie, nu modifica starea sistemului

test_create_student()
test_update_status()
test_return_students()
test_return_employed_students()
test_create_new_student_with_input()
test_delete_unemployed()
test_delete_student()