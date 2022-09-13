from concreteObserver import *
from concreteSubject import ConcreteSubject

subject = ConcreteSubject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.add_observer(observer_a)
subject.add_observer(observer_b)

subject.select_winning_number()
subject.select_winning_number()

subject.delete_observer(observer_a)

subject.select_winning_number()