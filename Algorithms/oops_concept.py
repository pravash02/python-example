"""
you can have a infinite amount of instances of this class without having to change

line 66 = Calling parent class in python 2.7
          (use 'super().__init__(name, age)' for python 3)
line 111 = This will call the parent class method as there in no 'speak function' defined inside the 'Fish function'
line 109 = This will override the the parent class's function 'show'

line 89 = class variable that is same across all instances
          Only accessed and modified using class name
line 98 = Use 'cls' as parameter for class method

"""

'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, students):
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print "I AM " + self.name + " and I am " + str(self.age) + "yrs old"

    def speak(self):
        print "I can't speak"


class Cat(Pet):
    def __init__(self, name, age, color):
        Pet.__init__(self, name, age)
        self.color = color

    def speak(self):
        print "MEOW"

    def show(self):
        print "I AM " + self.name + " and I am " + str(self.age) + "yrs old" + " and I am " + self.color


class Dog(Pet):
    def speak(self):
        print "BARK"


class Fish(Pet):
    pass


class Person:
    number_of_people = 0    # Only accessed by class name

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def return_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @staticmethod
    def add(x):
        return x + 1
'''

if __name__ == '__main__':
    pass
    '''
    # simple class
    d = Dog("tim", 25)
    print d.get_name()
    d.set_age(36)
    print d.get_age()
    
    # Dealing with more number of instances 
    s1 = Student("TIM", 19, 95)
    s2 = Student("BILL", 19, 75)
    s3 = Student("JILL", 19, 65)
    course = Course("Science", 2)
    course.add_student(s1)
    course.add_student(s2)
    print course.get_average_grade()

    # simple inheritance example
    p = Pet("TIM", 19)
    c = Cat("CAT", 20, "brown")
    c.show()    # I AM CAT and I am 20yrs old and I am brown
    d = Dog("DOG", 30)
    f = Fish("FISH", 35)
    f.speak()  # (I can't speak) since there i no speak method defined inside child class(Fish))

    # class variable and classmethod and staticmethod example
    p1 = Person("TIM")
    p2 = Person("JILL")
    print Person.return_people()
    print(p1.add(1))
    '''
