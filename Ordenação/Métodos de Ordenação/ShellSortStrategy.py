from AbstractSortStrategy import AbstractSortStrategy

class ShellSortStrategy(AbstractSortStrategy):
    def sort(self):
        elements = self.get_elements()
        length = len(elements)

        h = 1
        while h <= int(length / 3):
            h = h * 3 + 1

        while h > 0:
            for outer in range(h, length):
                temp = elements[outer]
                inner = outer

                while inner > (h - 1) and elements[inner - h] >= temp:
                    elements[inner] = elements[inner - h]
                    inner -= h

                elements[inner] = temp
            h = int((h - 1) / 3)

    def __repr__(self):
        return "ShellSortStrategy"
