from abc import ABCMeta, abstractmethod
from typing import Any, Dict


####### Singleton ba __new__
# class MySingleton:

#     _instance = None


#     @classmethod
#     def __new__(cls, *args, **kwargs):

#         if not cls._instance:
#             cls._instance = super().__new__(*args, **kwargs)
#             return cls._instance

#         else:
#             return cls._instance

####### Singleton ba __call__ MetaClass
class SingletonMeta(type):

    _instance_class: Dict = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in SingletonMeta._instance_class:
            temp = super().__call__(*args, **kwds)
            SingletonMeta._instance_class[self] = temp
            print(SingletonMeta._instance_class)
            return temp
        else:
            return SingletonMeta._instance_class[self]

class MySingletonA(metaclass=SingletonMeta):
    pass


class MySingletonB(metaclass=SingletonMeta):
    pass


a1 = MySingletonA()
a2 = MySingletonA()

b1 = MySingletonB()
b2 = MySingletonB()



print(a1 is a2)
print(b1 is a2)
print(b1 is b2)

    

