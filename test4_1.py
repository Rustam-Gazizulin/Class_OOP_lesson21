class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

    @name.setter
    def new_name(self, name):
        self._name = name

    @course.setter
    def course(self, value):
        self._course = value


student1 = Student('Jhon', 3)
name = student1.name
course = student1.course
print(name, course)
student1.new_name = 'Artur'
print(student1.name)
student1.course = 1
print(student1.course)
