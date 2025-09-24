class Produto:
    def __init__(self, id_produto: int, nome: str, preco: float):
        self.id__produto = id_produto
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        v = (novo_nome or "").strip()
        if not v:
            raise ValueError("Nome não pode ser vazio.")
        self.__nome = v

    @property
    def preco(self):
        return self.__preco
    
   
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = novo_preco 

    def __repr__(self):
        return f"Produto(id={self.id__produto}, nome={self.__nome}, preco={self.__preco:.2f})"
    
p1 = Produto(1, "Phone", 2000)

p1.nome = "Teclado"
p1.preco = 100

print(p1.__repr__())