from AbstractSortStrategy import AbstractSortStrategy

class InsertionSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        length = len(elements)

        for i in range(1, length):
            value = elements[i]
            j = i - 1
            while j >= 0 and elements[j] > value:
                elements[j + 1] = elements[j]
                j = j - 1
            elements[j + 1] = value

    def __repr__(self):
        return "InsertionSortStrategy"
