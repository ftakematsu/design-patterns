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

    @abstractmethod
    def construirTelhado(self) -> None:
        pass

    @abstractmethod
    def construirPorta(self) -> None:
        pass

    @abstractmethod
    def construirJanela(self, qtd) -> None:
        pass

    @abstractmethod
    def construirPiscina(self) -> None:
        pass


"""
Implementação concreta do Builder,
deve-se implementar os métodos abstratos.
"""
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

    def construirTelhado(self) -> None:
        self._product.add("telhado")
    
    def construirPorta(self) -> None:
        self._product.add("porta")

    def construirJanela(self, qtd) -> None:
        self._product.add(str(qtd) + " janela(s)")

    def construirPiscina(self) -> None:
        self._product.add("piscina")

"""
O principal objeto a ser construido
e customizado.
À medida que novos meios de configuração do objeto
são adicionados, não e necessário mudar a classe Casa.
"""
class Casa():
    # Como seria o construtor sem builder
    # Teria muitos parâmetros
    """
    def __init__(self, temChao, temTeto, temParedes, temTelhado, temPortas, temJanela, qtdJanelas, temPiscina):
        if (self.temChao):
            self.parts.append("chao")
        elif (self.temTelhado):
            self.parts.append("telhado")
        ...
        
    """
    
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def verDetalhes(self) -> None:
        print(f"A casa tem: {', '.join(self.parts)}", end="")

"""
A classe Diretor é responsável por
criar configurações pré-estabelecidas.
A classe diretor define a ordem na qual executar as etapas de construção,
enquanto que o builder provê a implementação dessas etapas.
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
        self.builder.construirTelhado()
        self.builder.construirPorta()
        self.builder.construirJanela(2)

    def construirCasaChique(self) -> None:
        self.construirCasa()
        self.builder.construirPiscina()


if __name__ == "__main__":
    director = Diretor()
    builder = ConstrutorCasa()
    director.builder = builder

    print("Casa diretor: ")
    #director.construirCasa()
    director.construirCasaChique()
    builder.product.verDetalhes()

    print("\n")
    print("Casa personalizada: ")
    builder.construirParedes()
    builder.construirJanela(4)
    builder.construirPorta()
    builder.product.verDetalhes()

