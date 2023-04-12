from contador import *

class QuebradorPalavras:
    def __init__(self):
        # Lista de contadores (dicionário de observadores)
        self.contadores = dict()
    
    def adicionaContador(self, nome: str, contador: Contador):
        self.contadores[nome] = contador
    
    def getContagem(self, nome: str):
        return self.contadores[nome].getContagem()
    
    def notify(self, palavras):
        for palavra in palavras:
            for name, contador in self.contadores.items():
                contador.contar(palavra)
    
    def quebrar(self, frase: str):
        palavras = frase.split(" ")
        self.notify(palavras)
        return palavras


if __name__ == "__main__":
    print("Contador de palavras \n")
    quebrador = QuebradorPalavras()
    frase = "o Rato roeu a roupa do Rei de Roma"
    quebrador.adicionaContador("SIMPLES", ContadorSimples())
    quebrador.adicionaContador("PAR", ContadorPar())

    palavras = quebrador.quebrar(frase)
    print(palavras)

    print("Contador simples: ", quebrador.getContagem("SIMPLES"))
    print("Contador par: ", quebrador.getContagem("PAR"))