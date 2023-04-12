class Aranha:
    def mover(self):
        print("O objeto esta movendo")
    def fazerTeia(self):
        print("O objeto esta fazendo teia")

"""
Para reaproveitar o método mover(), faz-se
uma herança com uma outra classe que tenha
o método implementado, mesmo que este não
tenha relação de hierarquia nenhuma.
"""
class Grilo(Aranha):
    def pular(self):
        print("O objeto esta pulando")
    """
    Possível solução: deixar o método fazerTeia()
    vazio.
    """
    def fazerTeia(self):
        pass

"""
Execução dos testes
"""
grilo = Grilo() # Instanciando o objeto
grilo.pular()
# O grilo não faz teia, embora esteja sendo permitido
grilo.fazerTeia()

# Outra situação: uma instância de Aranha
# pode ser substituída por uma instância de Grilo
aranha = Aranha()
aranha = grilo # substituindo a instância pela outra
aranha.mover()
aranha.fazerTeia()




