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

carros = []

for i in range(3):  # cadastra 3 carros
    print(f"\nCadastro do carro {i+1}:")
    marca = input("Digite a marca: ")
    nome = input("Digite o nome: ")
    detalhes = input("Digite os detalhes: ")
    ano_fab = int(input("Digite o ano de fabricação: "))
    ano_mod = int(input("Digite o ano do modelo: "))
    
    carro = Carro(marca, nome, detalhes, ano_fab, ano_mod)
    carros.append(carro)

print("\n--- Lista de carros cadastrados ---")
for c in carros:
    c.descrever()
