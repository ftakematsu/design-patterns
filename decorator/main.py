from __future__ import annotations
from abc import ABC, abstractmethod

"""
Classe abstrata principal, que vai representar a lista de bebidas
"""
class Bebida(ABC):
    def __init__(self, desc) -> None:
        self.descricao = desc

    @abstractmethod
    def custo(self) -> float:
        pass

"""
Classe que representa uma instancia concreta de uma bebida
"""
class Cafe(Bebida):
    def __init__(self, desc) -> None:
        self.descricao = desc
    
    def custo(self) -> float:
        return 2.50

"""
Definição abstrata de um condimento adicional na bebida (Cafe)
"""
class Condimento(Bebida):
    def __init__(self, desc) -> None:
        self.descricao = desc

"""
Uma instância concreta de um condimento a ser adicionado
"""
class Leite(Condimento):
    def __init__(self, desc, bebida: Bebida) -> None:
        self.descricao = desc
        self.bebida = bebida
    def custo(self) -> float:
        return self.bebida.custo() + 3.00

if __name__ == "__main__":
    bebida = Cafe("cafe")
    # Adicionando um condimento (cafe com leite)
    bebida = Leite("cafe com leite", bebida)
    # Custo final sempre atualizado
    print("Custo total: ")
    print(bebida.custo())