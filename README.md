# Quick Sort — Análise de Desempenho em Python

Projeto acadêmico desenvolvido para implementar e analisar o algoritmo de ordenação **Quick Sort**, utilizando Python. O programa permite executar testes com diferentes tipos de vetores, medir operações realizadas pelo algoritmo e comparar seus resultados de desempenho.

## Objetivos

- Implementar o algoritmo Quick Sort em Python.
- Analisar o comportamento do algoritmo com diferentes entradas.
- Contabilizar iterações, trocas e partições realizadas.
- Medir a profundidade máxima das chamadas recursivas.
- Verificar a correção da ordenação.
- Comparar os resultados obtidos em diferentes cenários de teste.

## Tecnologias utilizadas

- **Python 3**
- `dataclasses` — organização das estatísticas do algoritmo.
- `random` — geração e embaralhamento de vetores.
- `time.perf_counter()` — medição do tempo de execução.

Todas as bibliotecas utilizadas pertencem à biblioteca padrão do Python, não sendo necessária a instalação de dependências externas.

## Funcionalidades

### 1. Casos de teste predefinidos

O programa oferece cinco cenários de teste:

- Vetor em ordem crescente.
- Vetor em ordem decrescente.
- Vetor em ordem aleatória.
- Vetor crescente com dois elementos trocados.
- Vetor decrescente com dois elementos trocados.

Os casos predefinidos utilizam vetores de 5.000 elementos.

### 2. Tamanho personalizado

É possível informar o tamanho de um vetor para executar um teste personalizado com elementos embaralhados.

### 3. Estatísticas do algoritmo

Durante a execução, são registradas as seguintes métricas:

| Métrica | Descrição |
|---|---|
| Iterações | Número de iterações do laço de partição. |
| Trocas | Número de trocas efetivas entre elementos. |
| Chamadas de processamento | Número de invocações da função `quick_sort`, incluindo a chamada inicial. |
| Partições | Quantidade de partições realizadas. |
| Profundidade máxima | Maior nível de chamadas da função `quick_sort` alcançado durante a execução. |
| Tempo de execução | Tempo gasto na ordenação, medido em segundos. |

Ao final, o programa também verifica se o vetor foi ordenado corretamente.

## Otimização implementada

Uma das características do projeto é a otimização da recursão do Quick Sort.

Em vez