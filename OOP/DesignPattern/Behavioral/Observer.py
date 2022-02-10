from abc import ABC, abstractmethod
from typing import List
import sys


class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass


class Radio(Subscriber):

    def update(self):
        print("man radio update shodam")


class TV(Subscriber):

    def update(self):
        print("man TV update shodam")


class WebSite(Subscriber):

    def update(self):
        print("man WebSite update shodam")


class Publisher:
    subscribers: List[Subscriber] = []

    def register_subscriber(self, s: Subscriber):
        print("subscribe!")
        if s not in self.subscribers:
            self.subscribers.append(s)

    def unregister_subscriber(self, s: Subscriber):
        print("unsubscribe!")
        if s in self.subscribers:
            self.subscribers.remove(s)

        
    def notify_subscribers(self):
        for s in self.subscribers:
            s.update()


if __name__ == "__main__":
    radio = Radio()
    tv = TV()
    web_site = WebSite()


    observer = Publisher()
    observer.register_subscriber(radio)
    observer.register_subscriber(tv)
    observer.register_subscriber(web_site)

    if len(sys.argv) < 2 :
        raise Exception("bayad begi che rokhdadi bude ya kolan begi hichi")
    if sys.argv[1] == "goal":
        observer.notify_subscribers()
    else:
        print("hich eventi rokh nadadeh")