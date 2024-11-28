import time  # Importa a biblioteca time para medir a performance dos algoritmos

# Função para ler o arquivo e retornar uma lista de números inteiros
def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return [int(num) for num in data]

# Função para medir o tempo de execução de um algoritmo
def measure_time(func, data):
    start_time = time.perf_counter()  # Inicia a medição do tempo
    func(data)  # Executa a função de ordenação
    end_time = time.perf_counter()  # Termina a medição do tempo
    return end_time - start_time  # Retorna o tempo decorrido

# Implementação do algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Implementação do algoritmo Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Implementação do algoritmo Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Implementação do algoritmo Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Implementação do algoritmo Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Função principal para executar os algoritmos de ordenação e medir o tempo
if __name__ == "__main__":
    file_path = 'exampleText.txt'  # Caminho do arquivo de entrada
    data = read_file(file_path)  # Lê os dados do arquivo

    algorithms = {  # Dicionário com os algoritmos de ordenação
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
    }

    for name, func in algorithms.items():  # Itera sobre cada algoritmo
        data_copy = data.copy()  # Faz uma cópia dos dados para não modificar o original
        duration = measure_time(func, data_copy)  # Mede o tempo de execução do algoritmo
        print(f"{name}: {duration:.6f} seconds")  # Imprime o tempo de execução
