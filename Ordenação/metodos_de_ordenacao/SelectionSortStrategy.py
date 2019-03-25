from AbstractSortStrategy import AbstractSortStrategy

class SelectionSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        length = len(elements)

        for i in range(0, length):
            min: int = i
            for j in range(i + 1, length):
                if elements[j] < elements[min]:
                    min = j
            self._swap(i, min)

    def __repr__(self):
        return "SelectionSortStrategy"
