class A(object):
    def func(self):
        print "Inside A"


class B(A):
    def func(self):
        print "Inside B"
        self.strb = "variable inside B"


class C(A):
    def func(self):
        print "Inside C"


class D(B, C):
    def func(self):
        B.func(self)  # To call a particular class function
        self.strb
        print "Inside D"


d = D()
d.func()  # o/p: Inside B, Inside D

print D.mro()
