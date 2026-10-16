
import random
from dataclasses import dataclass
from time import perf_counter


N = 5000

@dataclass
class Estatisticas:
    iteracoes: int = 0
    trocas: int = 0
    chamadas_recursivas: int = 0
    particoes: int = 0
    profundidade_max: int = 0

def trocar(vetor, i, j, estatisticas):
    """Troca dois elementos e contabiliza a operação."""
    if i != j:
        vetor[i], vetor[j] = vetor[j], vetor[i]
        estatisticas.trocas += 1

def particionar(vetor, inicio, fim, estatisticas):
    """
    Escolhe o pivô central e o desloca para o final.
    Ao terminar, retorna sua posição definitiva.
    
    """
    meio = (inicio + fim) // 2
    trocar(vetor, meio, fim, estatisticas)

    pivo = vetor[fim]
    limite_menores = inicio - 1

    for atual in range(inicio, fim):
        estatisticas.iteracoes += 1

        if vetor[atual] <= pivo:
            limite_menores += 1
            trocar(vetor, limite_menores, atual, estatisticas)

    posicao_pivo = limite_menores + 1
    trocar(vetor, posicao_pivo, fim, estatisticas)

    estatisticas.particoes += 1
    return posicao_pivo


def quick_sort(vetor, inicio, fim, estatisticas, profundidade=1):
    """
    Quick Sort com partição tradicional.
    A menor região é processada recursivamente;
    a maior é processada pelo laço externo.
    """
    estatisticas.chamadas_recursivas += 1

    estatisticas.profundidade_max = max(
        estatisticas.profundidade_max,
        profundidade
    )

    while inicio < fim:
        pivo = particionar(vetor, inicio, fim, estatisticas)

        tamanho_esquerda = pivo - inicio
        tamanho_direita = fim - pivo

        if tamanho_esquerda < tamanho_direita:
            quick_sort(vetor, inicio, pivo - 1, estatisticas, profundidade + 1)

            inicio = pivo + 1

        else:
            quick_sort(vetor, pivo + 1, fim, estatisticas, profundidade + 1)

            fim = pivo - 1


def verificar_ordenacao(vetor):
    """Confere se o vetor está em ordem crescente."""
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True


def casos_test():
    """Reproduz os cinco casos fornecidos pelo professor."""
    crescente = list(range(1, N + 1))

    decrescente = list(range(N, 0, -1))

    aleatorio = list(range(1, N + 1))
    random.shuffle(aleatorio)

    crescente_trocado = crescente.copy()
    crescente_trocado[5], crescente_trocado[4995] = (
        crescente_trocado[4995],
        crescente_trocado[5]
    )

    decrescente_trocado = decrescente.copy()
    decrescente_trocado[6], decrescente_trocado[4994] = (
        decrescente_trocado[4994],
        decrescente_trocado[6]
    )

    return [
        ("Caso 001 - Crescente", crescente),
        ("Caso 002 - Decrescente", decrescente),
        ("Caso 003 - Aleatório", aleatorio),
        ("Caso 004 - Crescente trocado", crescente_trocado),
        ("Caso 005 - Decrescente trocado", decrescente_trocado),
    ]

def casos_range(tamanho):
    """Gera um único caso aleatório com tamanho variável."""
    aleatorio = list(range(1, tamanho + 1))
    random.shuffle(aleatorio)

    return [
        (f"Caso Aleatório - Tamanho {tamanho}", aleatorio)
    ]


def executar_caso(nome, original):
    vetor = original.copy()
    estatisticas = Estatisticas()

    print("\n" + "=" * 70)
    print(nome)
    print(f"Quantidade de elementos: {len(vetor)}")

    print("\nVetor antes da ordenação:")
    print(vetor)

    inicio = perf_counter()

    quick_sort(
        vetor, 0, len(vetor) - 1, estatisticas
    )

    fim = perf_counter()

    print("\nVetor depois da ordenação:")
    print(vetor)

    print("\nResultados:")
    print(f"Iterações: {estatisticas.iteracoes}")
    print(f"Trocas: {estatisticas.trocas}")
    print(
        "Chamadas de processamento: "
        f"{estatisticas.chamadas_recursivas}"
    )
    print(f"Partições: {estatisticas.particoes}")
    print(f"Profundidade máxima: {estatisticas.profundidade_max}")
    print(f"Tempo: {fim - inicio:.6f} segundos")
    print(f"Ordenação correta: {verificar_ordenacao(vetor)}")

    return estatisticas, fim - inicio


def main():
    resultados = []
    print("[1] Quick Sort - Casos fornecidos pelo professor")
    print("[2] Quick Sort - Personalizar casos de teste")
    
    escolha = input(
        "Escolha uma opção (01 ou 02): "
    ).strip().upper()
    
    if escolha == "2":
        vetor_tamanho = int(input("Digite o tamanho do vetor: "))
        
        if vetor_tamanho < 1:
                print("O tamanho mínimo deve ser pelo menos 1.")
                return
            
        casos = casos_range(vetor_tamanho)
        
    else:
        casos = casos_test()

    for nome, vetor in casos:
        estatisticas, tempo = executar_caso(nome, vetor)
        resultados.append((nome, estatisticas, tempo))
        input('Enter para continuar...')

    print("\n" + "=" * 70)
    print("RESUMO FINAL")

    print(
        f"{'Caso':<32}"
        f"{'Iterações':>12}"
        f"{'Trocas':>10}"
        f"{'Tempo (s)':>13}"
    )

    for nome, estatisticas, tempo in resultados:
        print(
            f"{nome:<32}"
            f"{estatisticas.iteracoes:>12}"
            f"{estatisticas.trocas:>10}"
            f"{tempo:>13.6f}"
        )
        with open("resultados_quick_v2.txt", "a") as arquivo:
            arquivo.write(
                f"{'Caso':<32}"
                f"{'Iterações':>12}"
                f"{'Trocas':>10}"
                f"{'Tempo (s)':>13}\n"
            )
            arquivo.write(
                f"{nome:<32}"
                f"{estatisticas.iteracoes:>12}"
                f"{estatisticas.trocas:>10}"
                f"{tempo:>13.6f}\n"
            )


if __name__ == "__main__":
    main()
