# create a people class with a name and age attribute
# create a student class that inherits from people  and has a grade attribute

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

class Student(People):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# create a teacher class that inherits from people and has a salary attribute

class Teacher(People):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

# create a class called school that has a list of students and a list of teachers

class School:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers

# create a function that prints out all the students and their grades

def print_students(students):
    for student in students:
        print(student.name, student.grade)

# create a function that prints out all the teachers and their salaries

def print_teachers(teachers):
    for teacher in teachers:
        print(teacher.name, teacher.salary)

# create a function that prints out all the students and their grades and all the teachers and their salaries

def print_school(school):
    print_students(school.students)
    print_teachers(school.teachers)

# generate a school with 10 students and 3 teachers

students = [Student("student" + str(i), 18, i) for i in range(10)]
teachers = [Teacher("teacher" + str(i), 30, i) for i in range(3)]
school = School(students, teachers)

# print out the school  using the function you created  above

#print_school(school)
print_teachers(school.teachers)