from abc import ABC, abstractmethod



class ClientInterface(ABC):
    """
    

    """

    @abstractmethod
    def method(self):
        pass


class Service:

    def stock_data(self):
        print("data XML")
        return "XML"



class Adapter1(ClientInterface, Service):

    def method(self):
        print("get ", self.stock_data(), "data and convert to json")
        return "JSON"


class Adapter2(ClientInterface, Service):

    def method(self):
        print("get ", self.stock_data(), "data and convert to YAML")
        return "YAML"


def client(inteface: ClientInterface):

    print(inteface.method())



if __name__ == "__main__":


    print("data az xml be json tabdil beshe")
    adapter1 = Adapter1()
    client(adapter1)

    print("data az xml be yaml tabdil beshe")
    adapter2 = Adapter2()
    client(adapter2)
