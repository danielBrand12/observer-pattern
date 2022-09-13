from observer import Observer
from subject import Subject


class ConcreteObserverA(Observer):

    _name: str = "Alice"
    _chosen_number: int = 3

    def update_observer(self, subject: Subject) -> None:
        if subject._ticket_number == self._chosen_number:
            print(f"ConcreteObserverA: {self._name} won!!!")
        else:
            print(f"Bad luck {self._name} :(")


class ConcreteObserverB(Observer):

    _name: str = "Bob"
    _chosen_number: int = 5

    def update_observer(self, subject: Subject) -> None:
        if subject._ticket_number == self._chosen_number:
            print(f"ConcreteObserverA: {self._name} won!!!")
        else:
            print(f"Bad luck {self._name} :(")