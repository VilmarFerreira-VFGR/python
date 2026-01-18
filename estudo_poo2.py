'''
Herança        → Permite que uma classe herde atributos e métodos de outra.
Polimorfismo   → Permite que métodos tenham comportamentos diferentes 

Neste exemplo:
Herança: A classe Cachorro herda atributos da classe Animal
Polimorfismo: A função emitir_som recebe vários métodos (ações)
'''
# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome}: Som genérico')

# Classe derivada (herda de Animal)
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
cao = Cachorro('Rex')
gato = Gato('Mimi')
pinto = Pinto('Popó')

cao.emitir_som()
gato.emitir_som()
pinto.emitir_som()
