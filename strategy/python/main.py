from __future__ import annotations
from typing import List
# ABC: Abstract Base Class
from abc import ABC, abstractmethod

class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def metodoPrincipal(self) -> None:
        print("Ordenando dados de acordo com o padrao Strategy")
        result = self._strategy.executa(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    """
    Aqui é necessário declarar as operações em comum para os algoritmos.
    O que deve variar é apenas o comportamento.
    O contexto que usar esta interface deve chamar este algoritmo.
    """
    @abstractmethod
    def executa(self, data: List):
        pass


"""
Implementação de classes concretas, que herdam da classe
geral Strategy, todos devem implementar o comportamento
"""
class ClasseConcretaA(Strategy):
    # Método concreto implementado
    def executa(self, data: List) -> List:
        return sorted(data)

class ClasseConcretaB(Strategy):
    # Método concreto implementado
    def executa(self, data: List) -> List:
        return reversed(sorted(data))

"""
Método principal
"""
if __name__ == "__main__":
    context = Context(ClasseConcretaA())
    print("Cliente: ordena normalmente")
    context.metodoPrincipal()
    print()

    print("Cliente: ordena de modo reverso.")
    context.strategy = ClasseConcretaB()
    context.metodoPrincipal()



