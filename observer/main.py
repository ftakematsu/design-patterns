"""
Verificar sempre a situação da pessoa:
- peso até 60: abaixo
- peso entre 60 e 90: normal
- peso entre 90 e 100: sobrepeso
- peso acima de 100: obesidade I
- peso acima de 120: obesidade II
"""
class Dieta:
    def __init__(self, peso):
        self.peso = peso
    
    def getPeso(self):
        return self.peso
    
    def comerCalorias(self, kcal):
        # Cálculo fictício, não tem nava a ver com a realidade
        self.peso += kcal*0.05

    def exercitar(self, pesoPerdido):
        self.peso -= pesoPerdido

    def comerComida(self, kg):
        self.peso += kg
    

if __name__ == "__main__":
    pessoa = Dieta(50)
    
    
