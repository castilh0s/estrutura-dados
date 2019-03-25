class IStrategy:
    """
    Interface implementada pelos algoritmos de ordenação
    """

    def sort(self):
        """
        Realiza a ordenação
        """
        raise NotImplementedError("É preciso implementar o método sort.")

    def get_elements(self):
        """
        Retorna o array com os dados
        """
        raise NotImplementedError("É preciso implementar o método get_elements.")

    def set_elements(self, elements):
        """
        Registra os elementos que serão ordenados
        """
        raise NotImplementedError("É preciso implementar o método set_elements.")
