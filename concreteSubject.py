from subject import Subject
from typing import List
from observer import Observer
from random import randrange

class ConcreteSubject(Subject):

    _ticket_number: int = None
    _observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        print("Subject: Added an observer.")
        self._observers.append(observer)

    def delete_observer(self, observer: Observer) -> None:
        print(f"Subject: Observer {observer._name} deleted.")
        self._observers.remove(observer)

    def notify_observer(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update_observer(self)

    def select_winning_number(self) -> None:

        print("\nSubject: Selecting the winning number!!.")
        self._ticket_number = randrange(0, 10)

        print(f"Subject: The winning number is: {self._ticket_number}")
        self.notify_observer()