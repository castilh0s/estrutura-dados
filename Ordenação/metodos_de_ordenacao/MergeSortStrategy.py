from AbstractSortStrategy import AbstractSortStrategy

class MergeSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        length = len(elements)

        self.__merge_sort(elements, length)

    def __merge_sort(self, elements, size):
        if size < 2:
            return

        mid = int(size / 2)
        l = [0] * mid
        r = [0] * (size - mid)

        for i in range(0, mid):
            l[i] = elements[i]

        for i in range(mid, size):
            r[i - mid] = elements[i]

        self.__merge_sort(l, mid)
        self.__merge_sort(r, size - mid)

        self.__merge(elements, l, r, mid, size - mid)

    @staticmethod
    def __merge(elements, left_partition, right_partition, left, right):
        i = 0
        j = 0
        position = 0

        while i < left and j < right:
            if left_partition[i] <= right_partition[j]:
                elements[position] = left_partition[i]
                i += 1
            else:
                elements[position] = right_partition[j]
                j += 1
            position += 1

        while i < left:
            elements[position] = left_partition[i]
            position += 1
            i += 1

        while j < right:
            elements[position] = right_partition[j]
            position += 1
            j += 1

    def __repr__(self):
        return "MergeSortStrategy"
