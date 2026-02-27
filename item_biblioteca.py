class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_ano(self):
        return self.__ano

    def get_disponivel(self):
        return self.__disponivel

    # Setters simples
    def set_titulo(self, titulo):
        if titulo != "":
            self.__titulo = titulo

    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano

    # Métodos principais
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item '{self.__titulo}' emprestado com sucesso.")
        else:
            print(f"Item '{self.__titulo}' já está emprestado.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Item '{self.__titulo}' devolvido com sucesso.")
        else:
            print(f"Item '{self.__titulo}' já está disponível.")

    def exibir_detalhes(self):
        # Será sobrescrito
        pass"