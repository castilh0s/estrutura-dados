from AbstractSortStrategy import AbstractSortStrategy

class BubbleSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        lenght = len(elements)
        until = lenght - 1

        for i in range(0, lenght):
            for j in range(0, until):
                k = j + 1
                if elements[j] > elements[k]:
                    self._swap(j, k)

    def __repr__(self):
        return "BubbleSortStrategy"
