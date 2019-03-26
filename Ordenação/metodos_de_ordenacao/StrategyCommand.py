from Ordenação.metodos_de_ordenacao import AbstractSortStrategy

class StrategyCommand:
    @staticmethod
    def execute(strategy: AbstractSortStrategy):
        strategy.set_elements()
        strategy.sort()
