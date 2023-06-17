class A:
    def __init__(self, ss1, ss2):
        self.ss1 = ss1
        self.ss2 = ss2

    def metod1(self):
        print("Metod 1 of class A")

    def metod2(self):
        print("Metod 2 of class A")

    def metod3(self):
        print("Metod 3 of class A")


class B(A):
    def __init__(self, ss1, ss2, ss3):
        super().__init__(ss1, ss2)
        self.ss3 = ss3

    def metod3(self):
        print("Metod 3 of class B")


class C(A):
    def __init__(self, ss1="default_ss1", ss2="default_ss2"):
        super().__init__(ss1, ss2)

    def metod4(self):
        print("Metod 4 of class C")

    def metod5(self):
        print("Metod 5 of class C")


a = A("ss1_value", "ss2_value")
b = B("ss1_value", "ss2_value", "ss3_value")
c = C()

a.metod1()
a.metod2()
a.metod3()

b.metod1()
b.metod2()
b.metod3()

c.metod1()
c.metod2()
c.metod3()
c.metod4()
c.metod5()