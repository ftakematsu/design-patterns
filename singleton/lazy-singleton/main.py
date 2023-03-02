"""
Classe base para definir uma classe como Singleton
"""
class SingletonMeta(type):
    _instances = {} # Armazena uma lista de instâncias

    def __call__(cls, *args, **kwargs):
        # Caso a classe não esteja na lista, criar uma nova instância
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Se a classe estiver na lista de instâncias, apenas retornar a instância
        return cls._instances[cls]

"""
Exemplo de classe comum (não Singleton)
"""
class NotSingleton():
    def notSingletonMethod(self):
        print("Chamada de um metodo nao singleton!")
        return True

"""
Exemplo de classe no padrão Singleton
"""
class SingletonClass(metaclass=SingletonMeta):
    def singletonMethod(self):
        print("Chamada de um metodo singleton!")
        return True

"""
Chamada de métodos para teste
"""
def ExemploNotSingleton():
    print("Padrao Nao Singleton")
    s1 = NotSingleton()
    s2 = NotSingleton()
    # As duas instâncias são diferentes, apesar de pertencerem à mesma classe
    print("ID s1 = ", id(s1)) 
    print("ID s2 = ", id(s2))

def ExemploSingleton():
    print("Padrao Singleton")
    s1 = SingletonClass()
    s2 = SingletonClass()
    # As duas instâncias são diferentes, apesar de pertencerem à mesma classe
    print("ID s1 = ", id(s1)) 
    print("ID s2 = ", id(s2))


def ExemploThreadSingleton():
    pass

if __name__ == "__main__":
    #ExemploNotSingleton()
    ExemploSingleton()