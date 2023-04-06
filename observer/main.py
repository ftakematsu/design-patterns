from __future__ import annotations
from abc import ABC, abstractmethod

"""
Verificar sempre a situação da pessoa
"""
class DietaSemObserver:
    def __init__(self, peso):
        self.peso = peso
    
    def getPeso(self):
        return self.peso
    
    def comerCalorias(self, kcal):
        # Cálculo fictício, não tem nava a ver com a realidade
        self.peso += kcal*0.05
        if (self.peso<50):
            print("Vc esta abaixo do peso. Recomendo comer algo.")
        elif (self.peso<100):
            print("Vc esta dentro do limite. Continue mantendo assim.")
        elif (self.peso>=100):
            print("Vc esta acima do peso. Recomendo dieta e exercicios.")

    def exercitar(self, pesoPerdido):
        self.peso -= pesoPerdido
        if (self.peso<50):
            print("Vc esta abaixo do peso. Recomendo comer algo.")
        elif (self.peso<100):
            print("Vc esta dentro do limite. Continue mantendo assim.")
        elif (self.peso>=100):
            print("Vc esta acima do peso. Recomendo dieta e exercicios.")


    def comerComida(self, kg):
        self.peso += kg
        if (self.peso<50):
            print("Vc esta abaixo do peso. Recomendo comer algo.")
        elif (self.peso<100):
            print("Vc esta dentro do limite. Continue mantendo assim.")
        elif (self.peso>=100):
            print("Vc esta acima do peso. Recomendo dieta e exercicios.")

"""
Classe com a implementação do Observer.
"""
class Dieta:
    def __init__(self, peso):
        self.peso = peso
        # Definindo uma lista de Observers
        self._observerList = []

    # Adicionar observadores
    def addObserver(self, obs: Observer):
        self._observerList.append(obs)

    # Notificador (sempre vai notificar o utilizador do objeto nas atualizações)
    # Toda vez que alguma mudança for feita, chamar este notificador
    def notify(self):
        # Percorrer a lista de observadores
        for obs in self._observerList:
            obs.update(self) # Executa a atualização
    
    def getPeso(self):
        return self.peso
    
    def comerComida(self, kg):
        self.peso += kg
        # Chama o notificador
        self.notify()

    def queimarCalorias(self, kg):
        self.peso -= kg
        self.notify()

"""
Classe Observer
"""
class Observer(ABC):
    """
    Método responsável por notificar atualizações.
    """
    @abstractmethod
    def update(self, objeto):
        pass

"""
Implementação da versão concreta da classe Observer
"""
class DietaObserver(Observer):
    """
    objeto: é uma instância da classe Dieta.
    Este vai ser sempre notificado de atualizações.
    """
    def update(self, objeto):
        if (objeto.getPeso()<50):
            print("Vc esta abaixo do peso.")
        elif (objeto.getPeso()<=100):
            print("Vc esta dentro do limite.")
        elif (objeto.getPeso()>100):
            print("Vc esta acima do peso.")

"""
Segundo observador
"""
class Recomendador(Observer):
    def update(self, objeto):
        if (objeto.getPeso()<30):
            print("Recomendo procurar um medico, parece doente")
        elif (objeto.getPeso()<50):
            print("Recomendo comer um pouco mais")
        elif (objeto.getPeso()>200):
            print("Recomendo fazer dieta e procurar um medico")
        elif (objeto.getPeso()>100):
            print("Recomendo fazer dieta e exercicios")


if __name__ == "__main__":
    """
    pessoa = DietaSemObserver(50)
    pessoa.comerComida(20)
    pessoa.comerComida(20)
    pessoa.comerComida(20)
    """
    pessoa = Dieta(50)
    # Adicionando um observador
    pessoa.addObserver(DietaObserver())
    #pessoa.addObserver(Recomendador())
    pessoa.comerComida(20)
    pessoa.comerComida(20)
    pessoa.comerComida(20)
    pessoa.queimarCalorias(70)
    pessoa.queimarCalorias(20)
