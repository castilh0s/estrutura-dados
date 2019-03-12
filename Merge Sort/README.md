
# Merge Sort

O Merge Sort é um algoritmo de divisão e conquista. Ele consiste, basicamente, em dividir uma lista pela metade até restar apenas um índice em cada vetor. Após fazer os cálculos de divisão e não restar mais nenhum problema, é feito o que se chama de conquistar, que realiza um merge (junção) sequencial dos vetores, ordenando os valores e voltando a ser uma única lista com o mesmo tamanho inicial, porém ordenada.

## Exemplo de um merge sort
![Animated Merge Sort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

> Exemplo simplificado. [Fonte. Acesso em 10/03/2019](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

![Detailed Merge Sort](https://cdn.kastatic.org/ka-perseus-images/ace963383bea8d154f6abd1322a06a73b56b4628.png)

> Exemplo detalhado. [Fonte. Acesso em 12/03/2019](https://cdn.kastatic.org/ka-perseus-images/ace963383bea8d154f6abd1322a06a73b56b4628.png)
## Algoritmo

Para rodar o algoritmo de merge sort é necessário compilar o mesmo e rodar passando dois parametros à ele, sendo o primeiro o tamanho do array e o segundo o maior valor possível desse array.

### Exemplo

```bash
$ #Compilar o programa
$ javac MergeSort.java
$ # Rodar o algoritmo
$ java MergeSort 5 10
> Array Inicial
> 7 8 9 4 9
>
> Array Final
> 4 7 8 9 9
```

## Estudantes

* Henrique de Castilhos
* Henrique Ceccagno Lorenzini
* João Vitor Seidel dos Santos
