class A:
    def __init__(self):
        self.db = self.Inner()  # creating object for inner class

    def display(self):
        print('In Parent Class')

    class Inner:
        def display1(self):
            print('Inner Of Parent Class')


class B(A):
    def __init__(self):
        super().__init__()

    class Inner(A.Inner):
        def display2(self):
            print('Inner Of Child Class')


p = B()
p.display()  # calling parent's class function
print(p.db.display1())  # calling parent's inner class's function
print(p.db.display2())  # calling child's inner class function

# x = p.db
# x.display1()
# x.display2()
