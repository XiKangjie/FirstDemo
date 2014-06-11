class A:
    count = 0
    def __init__(self):
        A.count += 1
        self.PrintA()
    def PrintA(self):
        print("I am A!")
        print(A.count)

global_A = A()

class B:
    pass
