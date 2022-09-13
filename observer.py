from abc import ABC, abstractmethod
from subject import Subject

class Observer(ABC):
    """
    Intefáz de Observer que declara el método 'update' que usan los 'subjects'
    """

    @abstractmethod
    def update_observer(self, subject: Subject) -> None:
        """
        Recibe una actualización cuando hay un cambio de estado en el 'subject'
        """
        pass


