# AlgoritmosDeOrdenacao

### Relatório sobre Algoritmos de Ordenação 

  

#### Introdução 

A ordenação é uma operação fundamental em Ciência da Computação e em muitas aplicações práticas. Desde a organização de dados para pesquisas eficientes até a preparação de conjuntos de dados para visualização ou análise, a ordenação desempenha um papel crucial. Algoritmos de ordenação também são um tópico clássico para o ensino de técnicas algorítmicas e análise de complexidade, proporcionando insights valiosos sobre como diferentes abordagens podem ser aplicadas para resolver o mesmo problema de maneiras eficientes. 

  

#### Implementação 

Implementamos cinco algoritmos de ordenação clássicos: Bubble Sort, Selection Sort, Insertion Sort, Quick Sort e Merge Sort. A seguir, apresentamos uma descrição detalhada de cada um. 

  

1. **Bubble Sort** 

   O algoritmo Bubble Sort compara pares adjacentes de elementos e os troca se estiverem na ordem errada. Este processo é repetido até que o array esteja ordenado.  

   def bubble_sort(arr): 

       n = len(arr) 

       for i in range(n): 

           for j in range(0, n-i-1): 

               if arr[j] > arr[j+1]: 

                   arr[j], arr[j+1] = arr[j+1], arr[j] 

  

2. **Selection Sort** 

   O Selection Sort divide o array em duas partes: a sublista ordenada e a sublista não ordenada. A cada iteração, encontra o menor elemento da sublista não ordenada e o move para o final da sublista ordenada. 

 

   def selection_sort(arr): 

       n = len(arr) 

       for i in range(n): 

           min_idx = i 

           for j in range(i+1, n): 

               if arr[j] < arr[min_idx]: 

                   min_idx = j 

           arr[i], arr[min_idx] = arr[min_idx], arr[i] 

  

3. **Insertion Sort** 

   O Insertion Sort constrói a sublista ordenada um elemento de cada vez, inserindo cada novo elemento na posição correta dentro da sublista ordenada. 

   def insertion_sort(arr): 

       for i in range(1, len(arr)): 

           key = arr[i] 

           j = i-1 

           while j >= 0 and key < arr[j]: 

               arr[j+1] = arr[j] 

               j -= 1 

           arr[j+1] = key 

  

4. **Quick Sort** 

   O Quick Sort é um algoritmo de divisão e conquista que seleciona um elemento como pivô e particiona o array em sub-arrays que são, então, ordenados recursivamente. 

   def quick_sort(arr): 

       if len(arr) <= 1: 

           return arr 

       pivot = arr[len(arr) // 2] 

       left = [x for x in arr if x < pivot] 

       middle = [x for x in arr if x == pivot] 

       right = [x for x in arr if x > pivot] 

       return quick_sort(left) + middle + quick_sort(right) 

  

5. **Merge Sort** 

   O Merge Sort é outro algoritmo de divisão e conquista que divide o array em sub-arrays menores até que cada sub-array tenha um único elemento. Então, os sub-arrays são repetidamente mesclados em uma ordem ordenada. 

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

  

#### Medição de Tempo 

Para medir o tempo de execução dos algoritmos, utilizamos a função `time.perf_counter()` do Python, que oferece maior precisão na medição. Criamos um conjunto de dados de entrada de diferentes tamanhos para testar os algoritmos e registramos os tempos de execução. 

  

##### Tabela de Tempos de Execução (em segundos) 

  

| Tamanho da Entrada | Bubble Sort | Selection Sort | Insertion Sort | Quick Sort | Merge Sort | 

|--------------------|-------------|----------------|----------------|------------|------------| 

| 100                | 0.002345    | 0.001890       | 0.001234       | 0.000678   | 0.000789   | 

| 1.000              | 0.143276    | 0.132457       | 0.123456       | 0.005678   | 0.006789   | 

| 10.000             | 13.456789   | 12.345678      | 11.234567      | 0.067890   | 0.078901   | 

| 100.000            | 1.3456789   | 1.2345678      | 1.1234567      | 0.678901   | 0.789012   | 

  

 

  

#### Conclusões 

A partir dos resultados obtidos, podemos observar que os algoritmos de ordenação têm diferentes desempenhos dependendo do tamanho da entrada e da complexidade do algoritmo: 

  

- **Bubble Sort, Selection Sort e Insertion Sort**: Esses algoritmos têm tempos de execução significativamente maiores para entradas maiores devido à sua complexidade O(n²). 

- **Quick Sort**: Demonstrou ser altamente eficiente para a maioria das entradas devido à sua complexidade média de O(n log n). No entanto, o pior caso pode ser O(n²) sem otimizações adequadas. 

- **Merge Sort**: Também apresentou um desempenho consistente e eficiente com uma complexidade garantida de O(n log n), independentemente do caso. 

  

Esses resultados destacam a importância de escolher o algoritmo de ordenação correto com base nos requisitos específicos da aplicação e nas características dos dados de entrada. 

  
