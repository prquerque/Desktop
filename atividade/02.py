class Cliente:
    def __init__(self, id_cliente, nome, email)
        self._id_cliente = id_cliente
        self._nome = nome
        self._email = email

    @property
    def id_cliente(self):
        return self._id_cliente
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo):
        v = (novo or "").strip()
        if not v :
            raise ValueError("Nome não pode ser vazio")
        self._nome = novo

    @property
    def email(self, novo):
        return self.email
    
    @email.setter
    def email(self, novo):
        v = (novo or "").strip()
        if "@" not in v:
            reise ValueError("Email inválido")
        self.email = novo

    def __repr__(self):
        return f"id_cliente= {self._id_cliente} - nome= {self._nome}, email= {self._email}"