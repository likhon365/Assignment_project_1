class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_info(self):
        print("Teacher Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


# Example usage:
student1 = Student("Alice", 16, 11)
student1.display_info()

print()

teacher1 = Teacher("Mr. Smith", 35, "Math")
teacher1.display_info()