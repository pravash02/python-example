"""
When you are using the abstract class in other classes then it becomes a compulsion to add the
abstract class's method (computer's class function - process) inside the the child class
(laptop)

If class is of  abstract type then you can't create object of that class

Also if the child class(Whiteboard) which inherits the abstract class should contain the abstract class's function name
and then only you can create the instance of the child class

example - create APIs, if someone want to use my API's they have to define methods
"""

"Testing for git sync"

from abc import ABCMeta, abstractmethod


class Computer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self):
        pass


class Whiteboard(Computer):
    def write(self):           # since its inheriting abstract class, change the function name to 'process' it will work
        print("write")


# Below class will work(you can create instance) as it contains the abstract class's function name
class Laptop(Computer):
    def process(self):
        print("Its Running")


class Programmer:
    def worker(self, com):
        print("Solving Bugs")
        # com.write()             # change the name to process
        com.process()


# com = Computer()  # This will throw error as it is a abstract class
lap = Laptop()
# wb = Whiteboard()   # This will throw error (sol - change its function name to abstract class's function name)
prgm = Programmer()
prgm.worker(lap)    # This will work
