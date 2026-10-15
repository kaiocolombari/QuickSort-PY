import random
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def partition(lista, menor, maior):
    pivo = lista[maior]
    i = menor - 1
    for j in range(menor, maior):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[maior] = lista[maior], lista[i + 1]
    return i + 1

def quick_sort(lista, menor, maior):
    if menor < maior:
        p = partition(lista, menor, maior)
        quick_sort(lista, menor, p - 1)
        quick_sort(lista, p + 1, maior)

arr = [random.randint(1, 100) for _ in range(10000)]
print("Original array:", arr)
input("Press Enter to sort the array...")

inicio = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
fim = time.perf_counter()

print("Sorted array:", arr)
print(f"Tempo de execução do Quick Sort: {fim - inicio:.6f} segundos")