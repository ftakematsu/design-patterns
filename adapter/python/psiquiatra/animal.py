from __future__ import annotations
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitirSom(self) -> str:
        pass

class Cachorro(Animal):
    def emitirSom(self) -> str:
        return "au au"

class Gato(Animal):
    def emitirSom(self) -> str:
        return "miau"

