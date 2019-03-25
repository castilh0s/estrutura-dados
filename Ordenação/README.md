# Ordenação

## Projeto

Baixar localmente o projeto encontrado [neste repositório](https://github.com/glauco-vinicius/estruturadedados).

## Atividade

* Com base no projeto execute os testes unitários localmente;
* Coloque os resultados de execução dos algoritmos em uma planilha.

## Resultados de execução

|             | Buble Sort | Selection Sort | Shell Sort | Insertion Sort | Heap Sort | Merge Sort | Quick Sort | Java Parallel | Java Sort |
| :---------: | :--------: | :------------: | :--------: | :------------: | :-------: | :--------: | :--------: | :-----------: | :-------: |
| **80.000**  | 2,255s     | 1,018s         | 5,057s     | 0,003s         | 0,005s    | 0,048s     | 1,444s     | 0,013s        | 0,003s    |
| **160.000** | 8,441s     | 4,238s         | 20,604s    | 0,002s         | 0,005s    | 0,017s     | 6,758s     | 0,019s        | 0,000s    |
| **320.000** | 33,082s    | 16,130s        | 83,190s    | 0,003s         | 0,002s    | 0,031s     | 28,509s    | 0,010s        | 0,002s    |
| **640.000** | 119,328s   | 58,144s        | 341,990s   | 0,002s         | 0,005s    | 0,062s     | 109,510s   | 0,008s        | 0,003s    |

## Questionário

1. Qual o algoritmo mais rápido?
2. Qual o mais lento?
3. Como ficou o desempenho do QuickSort?
4. Crie uma versão melhorada do QuickSort.
    1. O que você fez para melhorar o algoritmo? Explique a técnica.
5. Explique o algoritmo de ordenação paralela do Java.
6. Refaça os algoritmos em outra linguagem da sua escolha. Compare os resultados de performance com o Java.

## Resultados

1. O algoritmo mais rápido foi o Java Sort, que teve uma média de 0,002s.
2. O algoritmo mais lento foi o Shell Sort, que teve uma média de 112,710s.
3. O Quick Sort foi o segundo algoritmo de ordenação mais lento, ficando na frente apenas do Shell Sort.
4. [Novo Quick Sort](https://github.com/castilh0s/estrutura-dados/blob/master/Ordena%C3%A7%C3%A3o/SortsProject/src/main/java/catolicasc/estruturadedados/sortalgorithms/NewQuickSortStrategy.java).
    1. blablabla.
5. blablabla.
6. [Códigos em Python](https://github.com/castilh0s/estrutura-dados/tree/master/Ordena%C3%A7%C3%A3o/M%C3%A9todos%20de%20Ordena%C3%A7%C3%A3o).

## Estudantes

* Henrique de Castilhos
* João Vitor Seidel dos Santos
