from AbstractSortStrategy import AbstractSortStrategy

class QuickSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        length = len(elements)
        stack = [0, length]
        while len(stack) != 0:
            end = stack.pop()
            start = stack.pop()
            if end - start >= 2:
                p = start + int((end - start) / 2)
                p = self.__partition(elements, p, start, end)
                stack.append(p + 1)
                stack.append(end)
                stack.append(start)
                stack.append(p)

    def __partition(self, elements, position, start, end):
        l = start
        h = end - 2
        piv = elements[position]
        self._swap(position, end - 1)
        while l < h:
            if elements[l] < piv:
                l += 1
            elif elements[h] >= piv:
                h -= 1
            else:
                self._swap(l, h)

        idx = h
        if elements[h] < piv:
            idx += 1

        self._swap(end - 1, idx)
        return idx

    def __repr__(self):
        return "QuickSortStrategy"
