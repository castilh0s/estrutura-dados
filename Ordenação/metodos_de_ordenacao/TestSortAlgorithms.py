import unittest

from random import shuffle
from Ordenação.metodos_de_ordenacao import BubbleSortStrategy, HeapSortStrategy, InsertionSortStrategy, \
    MergeSortStrategy, QuickSortStrategy, ShellSortStrategy, StrategyCommand, IStrategy


class TestSortAlgorithms(unittest.TestCase):
    size = 680000
    data = [0] * size

    def __data(self):
        strategies = [BubbleSortStrategy,
                      HeapSortStrategy,
                      InsertionSortStrategy,
                      MergeSortStrategy,
                      QuickSortStrategy,
                      ShellSortStrategy]

        for i in range(0, self.size):
            list.append(i)
        shuffle(list)

        for i in range(0, len(self.data)):
            self.data[i] = int(list[i])

        value = 8000
        tests = []
        while value <= self.size:
            for i in range(0, len(strategies)):
                tests.append([strategies[i], value])
            value *= 2

        return tests

    @staticmethod
    def __is_sorted(elements):
        cond = False
        for i in range(0, len(elements)):
            j = elements[i]
            cond = (j <= elements[i + 1]) if True else False
        return cond

    @staticmethod
    def __array_copy(source, src_pos, dest, dest_pos, length):
        for i in range(length):
            dest[i + dest_pos] = source.data[i + src_pos]

    def __sort(self, strategy, elements):
        self.__array_copy(elements, 0, self.data, 0, len(elements))
        StrategyCommand.StrategyCommand.execute(strategy)
        return elements

    def test_sort_algorithms(self):
        elements = [] * self.size
        elements = self.__sort(IStrategy, elements)
        self.assertTrue(self.__is_sorted(elements))