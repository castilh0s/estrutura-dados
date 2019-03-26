from IStrategy import IStrategy

class AbstractSortStrategy(IStrategy):
    __elements = []

    def __init__(self, elements):
        self.set_elements(elements)

    def sort(self):
        raise NotImplementedError("É preciso implementar o método sort.")

    def get_elements(self):
        return self.__elements

    def set_elements(self, elements):
        self.__elements = elements

    def _swap(self, atual, prox):
        element = self.get_elements()[atual]
        self.__elements[atual] = self.__elements[prox]
        self.__elements[prox] = element

    def _print(self):
        print(self.__elements)
