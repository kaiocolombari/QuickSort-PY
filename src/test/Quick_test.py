import sys

def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        pivo = particionar(vetor, inicio, fim)

        quick_sort(vetor, inicio, pivo - 1)
        quick_sort(vetor, pivo + 1, fim)


def particionar(vetor, inicio, fim):
    pivo = vetor[fim]
    limite = inicio - 1

    for atual in range(inicio, fim):
        if vetor[atual] <= pivo:
            limite += 1
            vetor[limite], vetor[atual] = (
                vetor[atual],
                vetor[limite]
            )

    posicao = limite + 1
    vetor[posicao], vetor[fim] = vetor[fim], vetor[posicao]

    return posicao


if __name__ == "__main__":
    print("Limite de recursão:", sys.getrecursionlimit())

    vetor = list(range(2000))

    try:
        quick_sort(vetor, 0, len(vetor) - 1)
        print("Ordenação concluída!")
    except RecursionError:
        print("ERRO: limite de recursão excedido!")