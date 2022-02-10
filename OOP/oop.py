# class method, static method, object method
#  Inheritance, Encapsulation, Metaclass, Mixin
from datetime import datetime

class A:
    count = 0   # class attribute
    summ = 0

    def __init__(self, name) -> None:
        self.name = name
        A.count += 1
        print("hello")


    def show(self):
        print(self.name)
    
    @classmethod   #decorator
    def increment_summ(cls):
        cls.summ = 4

    @staticmethod
    def show_month():
        print(datetime.now().strftime("%B"))


a1 = A("Ashkan")
a2 = A("Babak")


print(A.count)
a1.increment_summ()
print(a2.summ)

print(a1.name)
print(a2.name)

a1.show_month()

