from abc import ABCMeta, ABC, abstractmethod



class AbstractFactoryMachine(metaclass=ABCMeta):

    @abstractmethod
    def sedan(self):
        pass

    @abstractmethod
    def crossover(self):
        pass


    @abstractmethod
    def motorcycle(self):
        pass


class ConcreteFactoryClassic(AbstractFactoryMachine):

    def sedan(self):
        return ProductSedanClassic()

    def crossover(self):
        return ProductCrossOverClassic()
    
    def motorcycle(self):
        return ProductMotorClassic()


class ConcreteFactoryModern(AbstractFactoryMachine):

    def sedan(self):
        return ProductSedanModern()

    def crossover(self):
        return ProductCrossOverModern()

    def motorcycle(self):
        return ProductMotorClassic()



class AbstractProductSedan(ABC):

    @abstractmethod
    def sandogh(self):
        pass


class AbstractProductCrossOver(ABC):

    @abstractmethod
    def shasi_boland(self):
        pass


class ProductSedanClassic(AbstractProductSedan):


    def sandogh(self):
        print("sandogh classic hastam")


class ProductSedanModern(AbstractProductSedan):


    def sandogh(self):
        print("sandogh modern hastam")


class ProductCrossOverClassic(AbstractProductCrossOver):


    def shasi_boland(self):
        print("shasi_boland classic hastam")


class ProductCrossOverModern(AbstractProductCrossOver):


    def shasi_boland(self):
        print("shasi_boland modern hastam")

class AbstractProductMotor(ABC):

    @abstractmethod
    def hendel(self):
        pass


class ProductMotorClassic(AbstractProductMotor):

    def hendel(self):
        print("hendel classic")


class ProductMotorModern(AbstractProductMotor):

    def hendel(self):
        print("hendel modern")



def client_code(factory: AbstractFactoryMachine) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.sedan()
    product_b = factory.crossover()

    product_a.sandogh()
    product_b.shasi_boland()

if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type(classic):")
    client_code(ConcreteFactoryClassic())

    print("\n")

    print("Client: Testing the same client code with the second factory type(modern):")
    client_code(ConcreteFactoryModern())