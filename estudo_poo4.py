# Criando a classe Carro
class Carro:
    def __init__(self, marca, nome, detalhes, ano_fab, ano_mod):
        self.marca = marca       # Atributo
        self.nome = nome         # Atributo
        self.detalhes = detalhes # Atributo
        self.ano_fab = ano_fab   # Atributo
        self.ano_mod = ano_mod   # Atributo
    
    def descrever(self):         # Método
        print(f'{self.marca} {self.nome} {self.detalhes}, Fabricado em {self.ano_fab}, Modelo {self.ano_mod}')

# Criando objetos
c1 = Carro('Hyundai', 'Elantra', '1.8 Automático', 2012, 2013)
c2 = Carro('Honda', 'Civic', '1.8 Automático', 2006, 2007)
c3 = Carro('Ford', 'Fiesta', '1.0 Manual Hatch', 2009, 2009)

# Mostrando métodos(Ações) dos objetos
c1.descrever()
c2.descrever()
c3.descrever()