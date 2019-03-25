from AbstractSortStrategy import AbstractSortStrategy

class HeapSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        n = len(elements)

        i = int(n / 2 - 1)
        while i >= 0:
            self.__heapify(elements, n, i)
            i -= 1

        i = n - 1
        while i >= 0:
            self._swap(0, i)

            self.__heapify(elements, i, 0)
            i -= 1

    def __heapify(self, elements, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and elements[l] > elements[largest]:
            largest = l

        if r < n and elements[r] > elements[largest]:
            largest = r

        if largest != i:
            swap = elements[i]
            elements[i] = elements[largest]
            elements[largest] = swap

            self.__heapify(elements, n, largest)

    def __repr__(self):
        return "HeapSortStrategy"
