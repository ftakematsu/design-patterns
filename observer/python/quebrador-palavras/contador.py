from __future__ import annotations
from abc import ABC, abstractmethod

"""
Classe que representa os observadores
"""
class Contador(ABC):
    def __init__(self):
        self.qtd = 0 # Contagem
    
    @abstractmethod
    def getContagem(self) -> int:
        pass
    
    @abstractmethod
    def contar(self, palavra: str) -> None:
        pass


"""
Contador simples - apenas conta todas as palavras.
"""
class ContadorSimples(Contador):
    def getContagem(self) -> int:
        return self.qtd
    
    def contar(self, palavra: str) -> None:
        self.qtd += 1

"""
Contador ce pares - conta apenas palavra de tamanho par
"""
class ContadorPar(Contador):
    def getContagem(self) -> int:
        return self.qtd
    
    def contar(self, palavra: str) -> None:
        if (len(palavra)%2 == 0):
            self.qtd += 1