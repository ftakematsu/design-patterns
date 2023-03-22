class TomadaDoisPinos:
    def __init__(self):
        self._entradas=2
    def getEntradas(self):
        return self._entradas
    def ligar(self):
        print("Ligado na Tomada de Dois Pinos")

class TomadaTresPinos:
    def __init__(self):
        self._entradas=3
    def getEntradas(self):
        return self._entradas
    def ligar(self):
        print("Ligado na Tomada de Tres Pinos")

class PlugDoisPinos:
    def ligarNaTomada(self, tomada):
        if (tomada.getEntradas()>=2):
            tomada.ligar()
        else:
            print("Nao foi possivel conectar")

class PlugTresPinos:
    def ligarNaTomada(self, tomada):
        if (tomada.getEntradas()>=3):
            tomada.ligar()
        else:
            print("Nao foi possivel conectar")

"""
Classe adaptadora
"""
class AdaptadorTomada(TomadaDoisPinos):
    """
    Inicializa (pluga) a tomada de 3 pinos no adaptador
    """
    def __init__(self, tomada: TomadaTresPinos):
        self._entradas = 3
        self.tomada = tomada
    def ligar(self):
        self.tomada.ligar()

if __name__ == "__main__":
    plug2 = PlugDoisPinos()
    plug2.ligarNaTomada(TomadaDoisPinos())
    plug3 = PlugTresPinos()
    plug3.ligarNaTomada(TomadaTresPinos())
    # Tentando uma conexão de 3 pinos para 2 entradas
    print("\n * Conectando 3 pinos para 2 entradas")
    plug3.ligarNaTomada(TomadaDoisPinos())
    # Com adaptador
    print("\n * Conectando 3 pinos para 2 entradas com adaptador 3-2")
    plug3.ligarNaTomada(AdaptadorTomada(TomadaDoisPinos()))