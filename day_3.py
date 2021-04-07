class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class CodingBootcamp:
    def __init__(self, course_name, max_students, instructor):
        self.course_name = course_name
        self.max_students = max_students
        self.instructor = instructor
        self.num_of_students = []


    def add_student(self, student):
        if len(self.num_of_students) < self.max_students:
            self.num_of_students.append(student)
            print("true")
            return self
        print("false")
        return self


    def display_students(self):
        for student in self.num_of_students:
            print(f"Student name: {student.name}, Student Grade: {student.grade}")

    def update_grade(self, student, new_grade):
        student.grade = new_grade
        return self


student1 = Student("Bruce Wayne", 21, 90)
print(student1)

student2 = Student("Robin (AKA Tim Drake)", 10, 60)
student3 = Student("Barry Allen", 40, 70)

course1 = CodingBootcamp("Coding Dojo", 2, "Adrien Dion")
print(course1)



course1.add_student(student1).add_student(student2).add_student(student3).display_students()

course1.update_grade(student1, 80).display_students()



