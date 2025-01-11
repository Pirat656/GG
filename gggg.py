class Student:
    def __init__(self, name=None, height=190):
        self.name = name
        self.height = height

    def __str__(self):
        return f'I am a student and my name is {self.name}'

    def __bool__(self):
        return self.name != None

    def __len__(self):
        return self.height

    def __del__(self):
        print("I am deleted")


first_student = Student(name="Nick")
print(first_student.__len__())
print(first_student.__bool__())
print(first_student)