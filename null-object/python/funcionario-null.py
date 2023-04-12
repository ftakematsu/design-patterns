# Objeto da classe Funcionario
class Funcionario:
    def __init__(self, nome):
        self._nome = nome
    def getNome(self):
        return self._nome
    def printNome(self):
        print("Nome: " + self.getNome())

# Criando um objeto que representa a versão nula do mesmo
# Esta será utilizada toda vez que alguma referência nula
# ao objeto for feita.
class FuncionarioNull(Funcionario):
    def getNome(self):
        return ""
    def printNome(self):
        print("nome invalido")


class GerenciadorFuncionario:
    def criar(self, nome: str) -> Funcionario:
        # Validador de nome
        if (len(nome)>=2):
            return Funcionario(nome)
        else: # Se o nome for inválido, retornar nulo
            #return None
            return FuncionarioNull(nome)


def testeSimples():
    func1 = Funcionario("Fulano")
    print("Nome: " + func1.getNome())
    funcNulo = Funcionario("Nulo")
    funcNulo = None
    #print("Nome: " + funcNulo.getNome())

def testeGerenciador():
    gerenciador = GerenciadorFuncionario()
    f1 = gerenciador.criar("Fulano")
    f2 = gerenciador.criar("Beltrano")
    f3 = gerenciador.criar("Ciclano")
    f4 = gerenciador.criar("") # Inválido
    f1.printNome()
    f2.printNome()
    f3.printNome()
    f4.printNome()
    """
    if(f1!=None):
        f1.printNome()
    if(f2!=None):
        f2.printNome()
    if(f3!=None):
        f3.printNome()
    if(f4!=None):
        f4.printNome()
    """
    

#testeSimples()
testeGerenciador()





