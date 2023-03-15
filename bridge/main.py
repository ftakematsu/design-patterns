from __future__ import annotations
from abc import ABC, abstractmethod

"""
A Implementação define a interface para todas as classes de implementação. Isto
não precisa corresponder à interface do Abstraction. Na verdade, as duas
as interfaces podem ser totalmente diferentes. Normalmente, a interface de Implementação
fornece apenas operações primitivas, enquanto a Abstração define
operações de nível baseadas nessas primitivas.
"""
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

"""
A Abstração define a interface para a parte de "controle" das duas 
hierarquias de classes. Ele mantém uma referência a um objeto da hierarquia 
de Implementação e delega todo o trabalho real a esse objeto.
"""
class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    def operation(self) -> str:
        return (f" * Circulo  + "
                f"{self.implementation.operation_implementation()}")


"""
Você pode estender a abstração sem alterar as classes de implementação.
"""
class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f" * Quadrado + "
                f"{self.implementation.operation_implementation()}")


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return " Vermelho"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return " Azul"


"""
Exceto na fase de inicialização, onde um objeto Abstraction é vinculado
com um objeto de implementação específico, o código do cliente deve depender apenas de
a classe Abstração. Dessa forma, o código do cliente pode suportar qualquer tipo de abstração.
combinação de implementação.
"""
def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")

if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationA()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
    
    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = Abstraction(implementation)
    client_code(abstraction)
