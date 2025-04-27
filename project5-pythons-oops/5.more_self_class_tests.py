class Test:
    def __init__(self, a):
        self.a = a
        print(a)
        print(self.a)

    def testing(self):
        print(self.a)
        print(self.a)

test1 = Test(123)
test1.testing()