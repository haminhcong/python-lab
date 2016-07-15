class A():
    x1 = 10
    x2 = 8

    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    def show(self):
        return self.a + self.b

    def rep(self):
        return self.a*self.b

class B(A):
    def __init__(self,a1,b1,c1,d1):
        super().__init__(a1,b1)
        self.c=c1
        self.d=d1
    def show(self):
        x=super().show()
        return x+self.c+self.d
a1 =A(5,6)
b1 =B(1,2,3,4)
print(b1.show())
print(a1.show())
print(b1.rep())