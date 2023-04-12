from __future__ import annotations
from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def inicio():
        pass
    @abstractmethod
    def proximo():
        pass
    @abstractmethod
    def fim():
        pass
    @abstractmethod
    def atual():
        pass