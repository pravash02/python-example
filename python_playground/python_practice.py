# Overloading---------------------------------------------------------#
import email


def add(a, b, c=None):
    if c is None:
        return a + b
    else:
        return a + b + c


print(add(1, 2))


# Overriding---------------------------------------------------------#

class Parent():
    def __init__(self):
        self.value = 1000

    def debit(self):
        print(self.value)


class Child(Parent):
    def __init__(self):
        self.value = 2000

    def debit(self):
        print(self.value)


p = Parent()
c = Child()
p.debit()  # o/p = 1000
c.debit()  # o/p = 2000

# Pass By Reference---------------------------------------------------------#

dic = {1: 'a', 2: 'b'}


def updatedic(dic):
    new = {3: 'c'}
    dic.update(new)
    print("Inside: ", dic)  # o/p = Inside: {1:'a', 2:'b', 3:'c'}
    return  # you can return/don't return the value


updatedic(dic)
print("Outside: ", dic)  # o/p = Outside: {1:'a', 2:'b', 3:'c'}

dic = {1: 'a', 2: 'b'}


# Pass By Value---------------------------------------------------------#

def updatedic(dic):
    dic = {3: 'c'}  # created a new dic object
    print("Inside: ", dic)  # o/p = Inside: {3:'c'}
    return


updatedic(dic)
print("Outside: ", dic)  # o/p = Outside: {1:'a', 2:'b', 3:'c'}


# Singleton---------------------------------------------------------#


class Parent:
    _instance = {}

    def __init__(self):
        self.__dict__ = self._instance
        print(self.__dict__, self._instance)


class Child(Parent):
    def __init__(self, arg):
        Parent.__init__(self)
        self.child_val = arg

    def __str__(self):
        return self.child_val


obj1 = Child("value1")
print(obj1)

obj2 = Child("value2")
print(obj2)

print(obj1)


class MySingleton(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance


x = MySingleton()
print(x.y)

x.y = 20

y = MySingleton()
print(x.y)


def singleton(MyClass):
    _instance = {}

    def get_instance(*args, **kwargs):
        if MyClass not in _instance:
            _instance[MyClass] = MyClass(*args, **kwargs)
        return _instance[MyClass]

    return get_instance


@singleton
class TestClass(object):
    pass


x = TestClass

# Shallow Copy---------------------------------------------------------#

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

new_list = copy.copy(old_list)
old_list[1][1] = 'AA'  # changes in old list affect new list

print("Old list:", old_list)  # o/p = ('Old list:', [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]])

print("New list:", new_list)  # o/p = ('New list:', [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]])

# Deep Copy---------------------------------------------------------#

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'  # changes in old list not affect new list
print("Old list:", old_list)  # o/p = ('Old list:', [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]])

print("New list:", new_list)  # o/p = ('New list:', [[1, 1, 1], [2, 2, 2], [3, 3, 3]])


# Args, Kwargs---------------------------------------------------------#

def alist(*args, **kwargs):
    print(args, kwargs)


alist(lst=[], tup=(), dic={})  # o/p = () {'tup': (), 'lst': [], 'dic': {}}

alist([1, 2], (3, 4), {5, 6})  # o/p = ([1, 2], (3, 4), set ([5, 6])) {}


def foo(a, b=3, *args, **kwargs):
    pass


foo('x')  # o/p: a=x, b=3, args=(), kwargs={}
foo('x', 'y')  # o/p: a=x, b=y, args=(), kwargs={}
foo('x', b='y')  # o/p: a=x, b=y, args=(), kwargs={}
foo('x', 'y', 'z', 'k')  # o/p: a=x, b=y, args=(z, k), kwargs={}
foo('x', c='y', d='y')  # o/p: a=x, b=3, args=(), kwargs={'c': 'y', 'd': 'k'}

foo('x', c='y', b='z', d='k')  # o/p: a=x, b=z, args=(), kwargs={'c': y, 'd': k}


# foo('x', 'e', c='y', b='z', d='k')  # TypeError: foo() got multiple values for keyword argument 'b'


# class---------------------------------------------------------#

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


class Car:
    maxspeed = 0
    name = ""

    def __init__(self, p):
        self.maxspeed = p
        self.name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.maxspeed))

    def changespeed(self, speed):
        self.maxspeed = speed

    @classmethod  # to change class variable
    def change(cls, v):
        cls.maxspeed = v


red1 = Car(100)  # initializes the instance variable to 100 for that instance (red1) respectively

red2 = Car(150)  # initializes the instance variable to 100 for that instance (red2) respectively

red1.drive()  # o/p: driving. maxspeed 100
red1.changespeed(200)  # changes the instance(red1) value to 200
red1.drive()  # o/p: driving. maxspeed 200
red2.drive()  # o/p: driving. maxspeed 150

Car.maxspeed  # accessing the class variable o/p: 0
red1.change(50)  # changed the class variable o/p: 50
red1.drive()  # o/p: driving. maxspeed 200 (instance(red1) value is 200)
Car.maxspeed  # accessing the class variable o/p: 50


# class B:
#     def __init__(self, my_int):
#         self.my_int = my_int
#
#     def my_int_and_4(self):
#         print(_adder(self.my_int, 4))
#
#
# ''' Make it private by adding prefix "_" so that it can only be accessed by class '''
#
#
# @staticmethod
# def _adder(a, b):
#     return a + b
#
#
# b = B(1)
# b.my_int_and_4()  # 5


class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(Person):
    def __init__(self, name, eid):
        ''' In Python 3.0+, "super().__init__(name)" also works'''
        super(Employee, self).__init__(
            name)  # Person.__init__(self, name), super is useful when you have only 1 base class for that child class.
        self.empID = eid

    def getID(self):
        return self.empID


emp = Employee("Geek1", "E101")
print(emp.getName(), emp.getID())  # o/p: ('Geek1', 'E101')


# Inheritance---------------------------------------------------------#

class Base1(object):
    def __init__(self):
        self.str1 = "base1"


class Base2(object):
    def __init__(self):
        self.str2 = "base2"


class MultiDerived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)  # Can’t use "super" in multiple inheritance
        Base2.__init__(self)

    def printStrs(self):
        print(self.str1, self.str2)


ob = MultiDerived()
ob.printStrs()  # o/p: ('base1', 'base2')


class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Derived1):
    pass


# MRO---------------------------------------------------------#

class A(object):
    def func(self):
        print("Inside A")


class B(A):
    def func(self):
        print("Inside B")
        self.strb = "variable inside B"


class C(A):
    def func(self):
        print("Inside C")


class D(B, C):
    def func(self):
        B.func(self)  # To call a particular class function
        self.strb
        print("Inside D")


d = D()
d.func()  # o/p: Inside B, Inside D

D.mro()  # Need to pass “object” as argument to the base class A


# o/p: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]

def outer_function(msg):
    message = msg

    def inner():
        print(msg)

    return inner


hi_func = outer_function("Hi")
hello_func = outer_function("Hello")

hi_func()
hello_func()

# class Employee:
#     def __ini__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @email.setter
#     def email(self, name):
#         first, last = name.split(" ")
#         self.first = first
#         self.last = last
#
#     @email.deleter
#     def email(self):
#         self.first = None
#         self.last = None
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# Emp1 = Employee('pravash', 'panigrahi')
# Emp1.email('pra.pani@email.com')
# Emp1.fullname  # instead of Emp1.fullname()
# del Emp1.email


py_string = 'Python'
slice_obj = slice(3)
print(py_string[slice_obj])  # o/p = Pyt

slice_obj2 = slice(1, 6, 2)
print(py_string[slice_obj2])  # o/p = yhn

py_string = 'Python'

# contains indices 0, 1 and 2
print(py_string[0:3])  # Pyt

# contains indices 1 and 3
print(py_string[1:5:2])  # yh


# Decorators---------------------------------------------------------#


def deco(add):
    def wrap(args, kwargs):
        print("*********")
        print(args, kwargs)
        sum1 = add(args, kwargs)
        print("inside", sum1)
        return sum1

    return wrap


@deco
def add(x, y):
    print("sum", x + y)


add(5, 6)
add(5, 5)
