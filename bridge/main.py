from __future__ import annotations
from abc import ABC, abstractmethod

"""
A Implementação define a interface para todas as classes de implementação. Isto
não precisa corresponder à interface do Abstraction. Na verdade, as duas
as interfaces podem ser totalmente diferentes. Normalmente, a interface de Implementação
fornece apenas operações primitivas, enquanto a Abstração define
operações de nível baseadas nessas primitivas.
"""
class Cor(ABC):
    @abstractmethod
    def pintar(self) -> str:
        pass

"""
A Abstração define a interface para a parte de "controle" das duas 
hierarquias de classes. Ele mantém uma referência a um objeto da hierarquia 
de Implementação e delega todo o trabalho real a esse objeto.
"""
class Figura(ABC):
    def __init__(self, cor: Cor) -> None:
        self.cor = cor
    @abstractmethod
    def gerar(self) -> str:
        pass


"""
Você pode estender a abstração sem alterar as classes de implementação.
"""
class Circulo(Figura):
    def gerar(self) -> str:
        return (f" * Circulo {self.cor.pintar()}")

class Quadrado(Figura):
    def gerar(self) -> str:
        return (f" * Quadrado {self.cor.pintar()}")

class Triangulo(Figura):
    def gerar(self) -> str:
        return (f" * Triangulo {self.cor.pintar()}")

"""
Definindo as implementações
"""
class Azul(Cor):
    def pintar(self) -> str:
        return "Azul"

class Vermelho(Cor):
    def pintar(self) -> str:
        return "Vermelho"

class Verde(Cor):
    def pintar(self) -> str:
        return "Verde"

"""
Exceto na fase de inicialização, onde um objeto abstração Figura é vinculado
com um objeto de implementação específico, o código do cliente deve depender apenas de
a classe Abstração. Dessa forma, o código do cliente pode suportar qualquer tipo de abstração.
combinação de implementação.
"""
def client_code(figura: Figura) -> None:
    print(figura.gerar(), end="")


if __name__ == "__main__":
    # Criando um Circulo Azul
    figura = Circulo(Azul())
    client_code(figura)
    print("\n")
    # Criando um Quadrado Vermelho
    figura = Quadrado(Vermelho())
    client_code(figura)
    print("\n")
    # Criando um Circulo Verde
    figura = Circulo(Verde())
    client_code(figura)
