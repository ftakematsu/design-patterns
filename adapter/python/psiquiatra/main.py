from animal import *
from abc import ABC, abstractmethod

class Temperamento(ABC):
    @abstractmethod
    def humor(self) -> str:
        pass
    def comoSeSente(self) -> None:
        print("Home eu me sinto " + self.humor())

class Feliz(Temperamento):
    def humor(self) -> str:
        return "feliz"
    def rir(self) -> str:
        return "kkkkkkkkkkkkkk"

class Psiquiatra:
    def __init__(self, paciente: Temperamento):
        self.paciente = paciente
    def examina(self):
        print(" - Psiquiatra: \nOla meu querido paciente, como se sente hoje? ")
        print(" - Paciente: ")
        self.paciente.comoSeSente()
        print(" - Psiquiatra: \nPercebi que voce esta " + self.paciente.humor())

class Triste(Temperamento):
    def humor(self) -> str:
        return "triste"
    def chorar(self) -> str:
        return "buaaaaaaaaaaaaaa"

class AnimalAdapter(Temperamento):
    pass

if __name__ == "__main__":
    psiquiatra = Psiquiatra(Feliz())
    psiquiatra.examina()
    # Tentando fazer um paciente atender um Animal (não é possível)
    psiquiatra = Psiquiatra(Cachorro())
    psiquiatra.examina()
