from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

"""
Builder: classe abstrata.
Classe-base de todo builder, com métodos
abstratos.
"""
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def construirChao(self) -> None:
        pass

    @abstractmethod
    def construirParedes(self) -> None:
        pass

    @abstractmethod
    def construirTeto(self) -> None:
        pass


class ConstrutorCasa(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Casa()

    @property
    def product(self) -> Casa:
        product = self._product
        self.reset()
        return product

    def construirChao(self) -> None:
        self._product.add("chao")

    def construirParedes(self) -> None:
        self._product.add("paredes")

    def construirTeto(self) -> None:
        self._product.add("teto")


class Casa():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def verDetalhes(self) -> None:
        print(f"A casa tem: {', '.join(self.parts)}", end="")

"""
A classe Diretor é responsável por
criar configurações pré-estabelecidas.
"""
class Diretor:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construirCasa(self) -> None:
        self.builder.construirChao()
        self.builder.construirParedes()
        self.builder.construirTeto()

    def construirCasaChique(self) -> None:
        pass


if __name__ == "__main__":
    director = Diretor()
    builder = ConstrutorCasa()
    director.builder = builder

    print("Casa basica: ")
    director.construirCasa()
    builder.product.verDetalhes()

    print("\n")
    """
    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
    """
