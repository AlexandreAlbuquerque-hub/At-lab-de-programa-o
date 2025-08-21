class Moto:

    motos_criadas = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Moto.motos_criadas.append(self)

    def exibir_info(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

    def editar(self, modelo=None, cor=None, ano=None):
        if modelo:
            self.modelo = modelo
        if cor:
            self.cor = cor
        if ano:
            self.ano = ano

    def excluir(self):
        if self in Moto.motos_criadas:
            Moto.motos_criadas.remove(self)

    @classmethod
    def listar_motos(cls):
        return [moto.exibir_info() for moto in cls.motos_criadas]


moto1 = Moto("Honda CG 125", "Vermelha", 2024)
moto2 = Moto("Yamaha Fazer 250", "Preta", 2021)


print("Motos criadas:")
print(Moto.listar_motos())


moto1.editar(cor="Azul")
print("\nDepois de editar a cor da moto1:")
print(Moto.listar_motos())


moto2.excluir()
print("\nDepois de excluir a moto2:")
print(Moto.listar_motos())
