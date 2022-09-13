from abc import ABC, abstractmethod
#from observer import Observer

class Subject(ABC):
    """
    Interfáz de 'subject' que declara un conjunto de métodos para administrar subscribers
    """
    class Observer():
        pass

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        """
        Método abstracto para agregar un 'observer'
        """
        pass

    @abstractmethod
    def delete_observer(self, observer: Observer) -> None:
        """
        Método abstracto para eliminar un 'observer' de un 'subject'
        """
        pass

    @abstractmethod
    def notify_observer(self) -> None:
        """
        Método abstracto para notificar un cambio de estado de un 'subject' a un 'observer'
        """
        pass