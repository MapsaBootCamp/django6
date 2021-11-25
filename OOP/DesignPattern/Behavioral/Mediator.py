from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def start_midiation(self):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, component1, component2) -> None:
        self._component1 = component1
        component1.mediator = self
        self._component2 = component2
        component2.mediator = self

    def start_midiation(self):
        self._component1.operation("PARVAZ")


    def notify(self, sender, event):
        if event == "FINISH" and isinstance(sender, ComponentA):
            self._component2.operation("PARVAZ")
        elif event == "FINISH" and isinstance(sender, ComponentB):
            print("payan amaliat parvaz")

class AbstractComponent(ABC):

    def __init__(self) -> None:
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def operation(self, event):
        pass


class ComponentA(AbstractComponent):

    def operation(self, event):
        if event == "PARVAZ":
            print("sal am man A hastam va daram parvaz mikonam")
            self.mediator.notify(self, "FINISH")


class ComponentB(AbstractComponent):

    def operation(self, event):
        if event == "PARVAZ":
            print("salam man B hastam va daram parvaz mikonam")
            self.mediator.notify(self, "FINISH")


if __name__ == "__main__":
    component1 = ComponentA()
    component2 = ComponentB()

    mediator = ConcreteMediator(component1, component2)

    mediator.start_midiation()