from threading import Lock, Thread

"""
Implementação do Singleton Thread-safe
"""
class SingletonMeta(type):
    _instances = {}
    # Agora temos um objeto de bloqueio que será usado para sincronizar threads durante o primeiro acesso ao Singleton.
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

"""
Criação da classe Singleton Thread-safe
"""
class Singleton(metaclass=SingletonMeta):
    value: str = None # Atributo para verificar o valor de cada objeto

    def __init__(self, value: str) -> None:
        self.value = value

    def metodoSingletonThread(self):
        print("Chamada do metodo singleton em thread")

def testSingletonThread(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

# Código principal
if __name__ == "__main__":
    # Inicializa as múltiplas threads
    process1 = Thread(target=testSingletonThread, args=("FOO",))
    process2 = Thread(target=testSingletonThread, args=("BAR",))
    process1.start()
    process2.start()

