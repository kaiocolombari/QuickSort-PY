import math

class ProfundidadeCalc:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.profundidade_maxima = 0

    def calcular_profundidade(self):
        if self.tamanho <= 0:
            return 0
        return math.floor(math.log2(self.tamanho)) + 1

print("Calculando a profundidade máxima para um vetor de tamanho 1_000_000_000:")
calc = ProfundidadeCalc(1_000_000_000_000)
profundidade = calc.calcular_profundidade()
print(f"Profundidade máxima: {profundidade}")
