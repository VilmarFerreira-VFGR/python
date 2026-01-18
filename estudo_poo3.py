'''
Usando __str__
'''

# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print('Som genérico')
    
    # Representação textual do objeto
    def __str__(self):
        return f'Animal: {self.nome}'
    
# Classe derivada
class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} diz: Au Au!')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} diz: Mial!')

class Pinto(Animal):
    def emitir_som(self):
        print(f'{self.nome} diz: Piu!')

# Criando objetos
cachorro = Cachorro('Rex')
gato = Gato('Mimi')
pinto = Pinto('Popó')

# Usando print diretamente
print(cachorro)
print(gato)
print(pinto)

# Usando métodos
cachorro.emitir_som()
gato.emitir_som()
pinto.emitir_som()