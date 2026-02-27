from item_biblioteca import ItemBiblioteca


class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__paginas = paginas

    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"

        print(f"LIVRO | Código: {self.get_codigo()} | "
              f"Título: {self.get_titulo()} | "
              f"Autor: {self.__autor} | "
              f"Páginas: {self.__paginas} | "
              f"Ano: {self.get_ano()} | "
              f"Status: {status}")