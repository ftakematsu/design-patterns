from __future__ import annotations
from abc import ABC, abstractmethod

"""
O Contexto define a interface de interesse dos clientes. 
Ele também mantém uma referência a uma instância de uma subclasse State, 
que representa o estado atual do Contexto.
"""
class Contexto:
    _state = None

    def __init__(self, state: State) -> None:
        self.transitionTo(state)
    
    """
    Permite a mudança de estado em tempo de execução
    """
    def transitionTo(self, state: State):
        print(f"Contexto: novo Estado -> {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()


"""
A classe base State declara métodos que todo Concrete State deve implementar e também fornece uma referência inversa ao objeto Context, associado ao State. Essa referência anterior pode ser usada pelos Estados para fazer a transição do Contexto para outro Estado.
"""
class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

"""
Classes concretas que implementam comportamentos.
"""
class EstadoConcretoA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transitionTo(EstadoConcretoB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class EstadoConcretoB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transitionTo(EstadoConcretoA())



if __name__ == "__main__":
    print("State Pattern")
    context = Contexto(EstadoConcretoA())
    context.request1()
    context.request2()


