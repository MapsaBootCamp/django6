from abc import ABC, abstractmethod
from typing import Optional


class Strategy(ABC):

    @abstractmethod
    def execute(self):
        pass


class RoadStrategy(Strategy):

    def execute(self):
        print("masiri ba mashin")


class WalkingStrategy(Strategy):

    def execute(self):
        print("ba pa")


class PublicStrategy(Strategy):

    def execute(self):
        print("ba bus")


class Context:

    def __init__(self) -> None:
        self._strategy: Optional[Strategy] = None


    @property
    def strategy(self):
        return self._strategy


    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy


    def do_somthing(self):
        self._strategy.execute()



def client(context: Context):

    context.do_somthing()


if __name__ == "__main__":

    Strategy1 = RoadStrategy()
    
    context = Context()
    context.strategy = Strategy1

    client(context)

    Strategy2 = WalkingStrategy()
    
    context = Context()
    context.strategy = Strategy2

    client(context)