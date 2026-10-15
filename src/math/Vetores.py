import random
import time

N = 5000

def randomizar():
    crescente = list(range(1, N + 1))

    decrescente = list(range(N, 0, -1))

    aleatorio = list(range(1, N + 1))

    random.shuffle(aleatorio)

    crescente_trocado = crescente.copy()
    crescente_trocado[5], crescente_trocado[4995] = {
        crescente_trocado[4995],
        crescente_trocado[5]
    }

    decrescente_trocado = decrescente.copy()
    decrescente_trocado[6], decrescente_trocado[4994] ={
        decrescente_trocado[4994], decrescente_trocado[6]
    }


inicio = time.perf_counter()

resultado = randomizar()

fim = time.perf_counter()

tempoExec = fim - inicio

print(f"Tempo de execução é de {tempoExec:.6f} segundos")