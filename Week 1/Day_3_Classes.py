class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def studentInfoFunc(self):
        print('Name:', self.name)
        print('Age:', self.age)

s1=Student('Terry', 17)
s1.studentInfoFunc()

class Course:
    def __init__(self, name, number):
        self.name=name
        self.number=number
    
    def courseInfoFunc(self):
        print('Course Name:', self.name)
        print('Course Number:', self.number)

c1=Course('Intro to Artificial Intelligence', '101')
c1.courseInfoFunc()